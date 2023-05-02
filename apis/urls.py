from django.urls import path
from .views import OrderDetail,OrderList
urlpatterns = [
    path("<int:pk>/", OrderDetail.as_view(), name="order_detail"),
    path("", OrderList.as_view(), name="order_list"),
]