from django import forms
from todo.models import Category, List




class CustomForm(forms.ModelForm):
  
    category =  forms.CharField(max_length=200, label='Category',widget=forms.TextInput())
    
    class Meta:
        model = Category
        fields = ('category',)

    def save(self, commit=True):
        # save the provided password and encrypt
        category = super(CustomForm, self).save(commit=False)
        if commit:
            category.save()
        return category
    

class ListForm(forms.ModelForm):
    title = forms.CharField(max_length=200, label='List')
    description = forms.CharField(max_length=200, label='Description')
    
    class Meta:
        model = List
        fields = ('title','description')
        

    def save(self, commit=True):
        todo = super(ListForm, self).save(commit=False)
        if commit:
            todo.save()
        return todo