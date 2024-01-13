from django.urls import path
from django.urls import path
from .views import (
    user_check_authentication,
    admin_check_authentication,
    CustomTokenObtainPairView,

    AdminCreateAPIView,
    UserCreateAPIView,
    UserListAPIView,
    POIListView,

    UserRegistrationView,
    POIListByUserView,
    UserSearchView,

    POICreateView,
    POIDetailView,
)

from rest_framework_simplejwt.views import TokenRefreshView,TokenBlacklistView

urlpatterns = [
    # check use authenticated
    path('is-user-login/', user_check_authentication, name='user_check_authentication'),
    path('is-admin-login/', admin_check_authentication, name='admin_check_authentication'),

    # jwt
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    # admin
    path("admin/create-admin/", AdminCreateAPIView.as_view(), name="admin_create_admin"),
    path("admin/create-user/", UserCreateAPIView.as_view(), name="admin_create_user"),
    path("admin/list-pois/", POIListView.as_view(), name="admin_list_pois"),
    path("admin/list-users/", UserListAPIView.as_view(), name="admin_list_users"),
    path('admin/search/', UserSearchView.as_view(), name='search_user'),

    # user
    path("user/register/", UserRegistrationView.as_view(), name="user_registration"),
    path('user/pois/<int:user_id>/', POIListByUserView.as_view(), name='poi_list_by_user'),
    
    # POI
    path("create-poi/", POICreateView.as_view(), name="create_poi"),
    path("poi-detail/<int:pk>/", POIDetailView.as_view(), name="poi_detail"),
]
