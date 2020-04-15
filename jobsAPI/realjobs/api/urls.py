from realjobs.api.views import JobOfferListView, JobOfferDetailView
from django.urls import path

urlpatterns = [
    path("jobs/", JobOfferListView.as_view(), name="job-list"),
    path("jobs/<int:pk>", JobOfferDetailView.as_view(), name="job-detail")
]
