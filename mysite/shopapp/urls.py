from django.urls import path
from . import views

add_name = "shopapp"
urlpatterns = [
    path("", views.shop_index, name="shop"),
    path("groups/", views.groups_list, name="groups"),
    path("products/", views.products_list, name="products"),
    path("order/", views.order_list, name="order")
]
