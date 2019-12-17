import json
from django.http import HttpResponse,HttpResponseForbidden
from django.views.generic import TemplateView, ListView, View
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from todo.forms import addListForm
#models
from todo.models import Person, Category, List

class HomeView(TemplateView):
    template_name = "main/home.html"
    model = List
    context_object_name = 'books'
    paginate_by = 5

    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     list =self.get_queryset()
    #     page = self.request.GET.get('page')
    #     paginator = Paginator(books, self.paginate_by)

    #     try:
    #         lists = paginator.page(page)
    #     except PageNotAnInteger:
    #         lists = paginator.page(1)
    #     except EmptyPage:
    #         lists = paginator.page(paginator.num_pages)
    #     context['lists'] = lists
    #     return context

    def get(self, request):
        content = {
            'CategoryList': Category.objects.all(),
            'List': List.objects.all(),
            'categoryForm': addListForm.CustomForm(),
            'form': addListForm.ListForm()
        }

        return render(request, self.template_name, content)
    


class AddList(View):
    
    def get(self, request):
        pass

    def post(self,request):
        formList = addListForm.ListForm(request.POST)
        formCategory = addListForm.CustomForm(request.POST)
        if formList.is_valid() and formCategory.is_valid():
            response_data = {}
            
            todoList = formList.save(commit=False)
            category = formCategory.save(commit=False)
            category.person = request.user
            category.save()
            todoList.category = category
            todoList.save()

            response_data['result'] = 'Created Successfully'
            response_data['code'] = 200
            response_data['category'] = category.category_name
            response_data['categoryId'] = category.pk
            response_data['listId'] = todoList.pk
            response_data['title'] = todoList.title
            response_data['description'] = todoList.description
            response_data['created_at'] = todoList.created_at.strftime('%B %d, %Y %I:%M %p')
            
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )

        else:
            return HttpResponse([formCategory.errors.as_json,formList.errors.as_json])

class UpdateList(View):
    def get(self, request):
        pass
    
    def post(self, request):
        isDone = bool(request.POST.get('isDone'))
        listId = request.POST.get('listId')
        response_data = {}
        updateList = List.objects.get(pk=listId)
        updateList.is_done = isDone
        updateList.save()
        
        response_data['result'] = 'Updated Successfully'
        response_data['code'] = 200
        response_data['isDone'] = isDone

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

class DeleteList(View):
    def get(self, request):
        pass

    def post(self, request):
        listId = request.POST.get('listId')
        List.objects.get(pk=listId).delete()
        response_data = {}
        response_data['result'] = 'Deleted Successfully'
        response_data['code'] = 200


        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


