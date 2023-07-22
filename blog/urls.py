from django.urls import path
from .views import*

urlpatterns = [
    path('', HomeView.as_view()),
    path('<int:id>/', BlogDetail.as_view()),
]