from django.urls import path
from django.conf.urls import url
from .views import Signup, ProfileDetail, AccountDelete, ProfileUpdate
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    url(r'^detail/(?P<slug>[-\w]+)/$', ProfileDetail.as_view(), name='detail'),
    url(r'^delete/(?P<slug>[-\w]+)/$', AccountDelete.as_view(), name='delete'),
    url(r'^update/(?P<slug>[-\w]+)/$', ProfileUpdate.as_view(), name='update'),
]

