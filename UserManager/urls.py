from django.urls import path
from .views import UserListView, UserDetailView

urlpatterns = [
    path('list/', UserListView.as_view(), name="user-list"),
    path('detail/<int:pk>/', UserDetailView.as_view(), name="user-detail")
]
