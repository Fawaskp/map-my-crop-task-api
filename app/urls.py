from django.urls import path
from .views import POIListCreateView, POIDetailView
from django.urls import path
from .views import UserRegistrationView, AdminRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('user/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('admin/register/', AdminRegistrationView.as_view(), name='admin-registration'),
    path('admin/all-poi/', AdminRegistrationView.as_view(), name='admin-registration'),
    path("create-poi/", POIListCreateView.as_view()),
    path("get-poi/<int:pk>/", POIDetailView.as_view()),
]
