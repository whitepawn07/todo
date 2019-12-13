

from django.views.generic import TemplateView
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from todo.forms import addListForm, multiForms

from todo.models import Person, Category, List

class HomeView(TemplateView):
    template_name = "main/home.html"
  
    def get(self, request):
        content = {
            'CategoryList': Category.objects.all(),
            'List': List.objects.all()
        }
        return render(request, self.template_name, content)
    
    def post(self,request):
        pass



