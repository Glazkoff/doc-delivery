from django.urls import path
from . import views

urlpatterns = [
    # Заказы
    path('orders/', views.OrdersListView.as_view()),
    path('orders/<int:pk>/', views.OrderDetailView.as_view()),
]
