from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import*

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view(template_name = 'pages/login.html')),
    path('logout/', LogoutView.as_view(next_page = '/')),
]