from django.conf.urls import url
from django.urls import path, include
from .views import SignUp,  HomeView
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='homepage'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUp.as_view(), name='signup')
]