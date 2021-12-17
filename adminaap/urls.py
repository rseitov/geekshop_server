import adminaap.views as adminaap
from django.urls import path

app_name = 'adminaap'

urlpatterns = [
    path('users/create/', adminaap.user_create, name='user_create'),
    path('users/read/', adminaap.users, name='users'),
    path('users/update/<int:pk>/', adminaap.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminaap.user_delete, name='user_delete'),

    path('categories/create/', adminaap.category_create, name='category_create'),
    path('categories/read/', adminaap.categories, name='categories'),
    path('categories/update/<int:pk>/', adminaap.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', adminaap.category_delete, name='category_delete'),

    path('products/create/category/<int:pk>/', adminaap.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', adminaap.products, name='products'),
    path('products/read/<int:pk>/', adminaap.product_read, name='product_read'),
    path('products/update/<int:pk>/', adminaap.product_update, name='product_update'),
    path('products/delete/<int:pk>/', adminaap.product_delete, name='product_delete'),
]

