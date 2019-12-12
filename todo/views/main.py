from django.contrib.auth import login, authenticate

from todo.forms.signupForm import SignupForm

from django.views.generic import TemplateView
from django.shortcuts import render,redirect 
from django.http import HttpResponse

from todo.models import Person


class HomeView(TemplateView):
    template_name = "main/home.html"


class SignUp(TemplateView):
    template_name = "registration/register.html"

    def post(self, request):
        if request.method == 'POST':

            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                user = authenticate(email=email, password=password)
                login(request, user)
                return redirect('/')
            else:
                return redirect('signup')
            
    def get(self,request):
        form = SignupForm()
        return render(request, self.template_name, {'form': form})
   
   