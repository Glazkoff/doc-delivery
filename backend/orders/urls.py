from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # Заказы
    path('orders/', csrf_exempt(views.OrdersListView.as_view())),
    path('orders/<int:pk>/', csrf_exempt(views.OrderDetailView.as_view())),
]
