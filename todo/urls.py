from django.conf.urls import url
from django.urls import path, include
from .views import SignUp, HomeView, ActivateView, ActivateAccountView, AddList, UpdateList, LoginView, DeleteList
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', login_required(HomeView.as_view()), name='homepage'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', SignUp.as_view(), name='signup'),
    path('account/activate/',ActivateAccountView.as_view(), name='activate'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                ActivateView.as_view(), name='activate'),
    path('add/list', AddList.as_view() , name="add-list"),
    path('update/list', UpdateList.as_view(), name="update-list"),
    path('delete/list', DeleteList.as_view(), name="delete-list")
    
]