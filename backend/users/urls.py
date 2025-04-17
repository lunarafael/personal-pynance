from django.urls import path
from .views import RegisterUserView, UserListView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user-create'), # POST /api/users/register/
    path("list/", UserListView.as_view(), name="user-list") # GET /api/users/list/
]