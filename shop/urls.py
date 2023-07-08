from django.urls import path
from .views import*

urlpatterns = [
    path('', HomeView.as_view()),
    path('<int:id>/', OrderView.as_view()),
    path('search/', SearchView.as_view()),
    path('cart/', CartView.as_view()),
]