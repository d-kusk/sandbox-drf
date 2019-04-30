from django.urls import path
from .views import UserListView, UserDetailView, UserCreateView, UserUpdateView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name="user-create"),
    path('list/', UserListView.as_view(), name="user-list"),
    path('update/<int:pk>', UserUpdateView.as_view(), name="user-update"),
    path('detail/<int:pk>/', UserDetailView.as_view(), name="user-detail")
]
