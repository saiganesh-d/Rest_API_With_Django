from django.urls import path

from . import views
from . import views2

urlpatterns = [
    path('',views.api_home),
    path('generic/<int:pk>/', views2.ProductDetailAPIView.as_view())
]