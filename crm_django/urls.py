from django.contrib import admin
from django.urls import path, include

from accounts.views import *

# from accounts.urls import

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts', include('accounts.urls')),
    path('', home, name='home'),
    path('products', products, name='products'),
    path('customers/<str:pk>', customers, name='customer'),

    # path('create_order/', createOrder, name="create_order"),
    path('create_order/<str:pk>', createCustomerOrder,
         name="customer_create_order"),
    path('update_order/<str:pk>', updateOrder, name="update_order"),
    path('delete_order/<str:pk>', deleteOrder, name="delete_order")
]
