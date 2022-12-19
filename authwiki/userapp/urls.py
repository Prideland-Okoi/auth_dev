from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='userapp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('profile/', views.profileview, name='profile'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('emailverification/', views.emailverification, name='emailverification'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)