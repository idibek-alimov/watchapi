from django.urls import path
from .views import OrderDetail,OrderList,ProductDetail,ProductList,DiscountList
urlpatterns = [
    path("<int:pk>/", OrderDetail.as_view(), name="order_detail"),
    path("", OrderList.as_view(), name="order_list"),
    path("product/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("product/", ProductList.as_view(), name="product_list"),
    path("discount/",DiscountList.as_view(),name="discount_list")
]