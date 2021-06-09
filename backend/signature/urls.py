from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # Заказы
    path('signature/', csrf_exempt(views.AddSignatureView.as_view())),
]
