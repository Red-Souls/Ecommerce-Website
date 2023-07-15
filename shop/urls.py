from django.urls import path
from .views import*

urlpatterns = [
    path('', HomeView.as_view()),
    path('<int:id>/', OrderView.as_view()),
    path('search/', SearchView.as_view()),
    path('cart/', CartView.as_view()),
    path('remove-all-cart-item/', RemoveAllCartItem.as_view()),
    path('delete-cart-item/<int:id>/', DeleteCartItem.as_view()),
]