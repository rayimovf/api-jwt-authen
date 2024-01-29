from django.urls import path
from .views import GetProduct, PostProduct
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('get-product/', GetProduct.as_view(), name='get-product'),
    path('post-product/', PostProduct.as_view(), name='post-product'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]