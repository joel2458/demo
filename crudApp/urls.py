from crudApp import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.addproduct,name='addproduct'),
    path('add_product_details',views.add_product_details,name='add_product_details'),
    path('show_products',views.show_products,name='show_products'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('edit_product_details/<int:pk>',views.edit_product_details,name='edit_product_details'),
    path('delete_product/<int:pk>',views.delete_product,name='delete_product'),

    path('load_demo',views.load_demo,name="load_demo")


]