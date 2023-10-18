from django.urls import path
from . import views
from .views import MyTokenObtainPairView, user_list_view, user_inspection_count

from rest_framework_simplejwt.views import (

    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('users-list/', user_list_view.as_view(),
         name='users-list'),
    path('users-inspection-count/', user_inspection_count.as_view(),
         name='users-inspection-count'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
