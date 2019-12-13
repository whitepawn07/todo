from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string, get_template

from django.template import Context
from django.http import HttpResponse,HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMessage

from todo.forms.signupForm import SignupForm
from todo.tokens import account_activation_token
from todo.models import Person

class SignUp(TemplateView):
    template_name = "registration/register.html"

    def post(self, request):
        if request.method == 'POST':

            form = SignupForm(request.POST)
            if form.is_valid():
    
                email = form.cleaned_data.get('email')
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                subject = 'Activate Your MySite Account'
                
                context = {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                }
                content = get_template('main/account_activation_email.html').render(context)
                email = EmailMessage(subject, content,to=[email])
                email.content_subtype = 'html'
                email.send()

                return redirect('activate')
            else:
                return redirect('signup')
            
    def get(self,request):
        form = SignupForm()
        return render(request, self.template_name, {'form': form})


class ActivateAccountView(TemplateView):
    template_name="main/account_activation_sent.html"

   
class ActivateView(TemplateView):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = Person.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, user.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.is_verified = True
            user.save()

            # login(request, user)
            return redirect('login')
        else:
            return render(request, 'account_activation_invalid.html')