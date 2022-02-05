from django.urls                import path, include
from rest_framework.routers     import DefaultRouter
from .views                     import ProductView, ProductDetailView


urlpatterns = [
    path('', ProductView.as_view()),
	path('<int:id>', ProductDetailView.as_view()), 
]