from django import forms
from todo.models import Category, List

class MultipleForm(forms.Form):
    """
       actions
    """
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())
    # category = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')

class CategoryForm(MultipleForm):
    category =  forms.CharField(max_length=150)

    class Meta:
        model = Category
        fields = ("category",)


class ListForm(MultipleForm):
    todolist = forms.CharField(max_length=200)
    
    class Meta:
        model = List
        fields = ("todolist",)