from django.urls import path
from .views import (SnackListView, 
                                  SnackDateView,
                                  SnackCreateView,
                                  SnackDeleteView,
                                  SnackUpdateView)

urlpatterns = [
    path("", SnackListView.as_view(), name = 'snack_list'),
    path("<int:pk>", SnackDateView.as_view(), name = 'snack_detail'),
    path("create/", SnackCreateView.as_view(), name = 'snack_create'),
    path("delete/<int:pk>", SnackDeleteView.as_view(), name = 'snack_delete'),
    path("update/<int:pk>", SnackUpdateView.as_view(), name = 'snack_update'),
]
