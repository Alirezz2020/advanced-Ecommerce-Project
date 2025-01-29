from django.urls import path
from . import views

app_name = 'orders'

urlpatterns=[

    path('create/', views.OrderCreateView.as_view(), name='orders_create'),
    path('detail/<int:product_id>/', views.OrderDetailView.as_view(), name='orders_detail'),
]