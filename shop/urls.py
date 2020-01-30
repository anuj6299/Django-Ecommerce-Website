from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('<int:category_id>/', views.detail, name='detail'),
    path('cart/', views.cart, name='cart'),

]
