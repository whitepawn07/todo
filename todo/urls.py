from django.conf.urls import url
from django.urls import path, include
from .views import SignUp, HomeView, ActivateView, ActivateAccountView
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='homepage'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUp.as_view(), name='signup'),
    path('account/activate/',ActivateAccountView.as_view(), name='activate'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                ActivateView.as_view(), name='activate'),
    
]