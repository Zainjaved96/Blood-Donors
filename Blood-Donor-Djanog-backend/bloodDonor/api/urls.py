from django.contrib import admin
from django.urls import path, include
from .views import ListBloodDonorsView, \
    CreateBloodDonorView, BloodDonorDetailView, \
    DeleteBloodDonorView, UpdateBloodDonorView

urlpatterns = [
    path('create', CreateBloodDonorView.as_view(), name="Creating blood donor"),
    path('all', ListBloodDonorsView.as_view(), name="Listing all blood donors"),
    path('<int:pk>', BloodDonorDetailView.as_view(), name="Listing Specific Donors"),
    path('delete/<int:pk>', DeleteBloodDonorView.as_view(), name="Delete Blood Donor View"),
    path('update/<int:pk>', UpdateBloodDonorView.as_view(), name="Updating blood donor"),
]
