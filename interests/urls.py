from django.urls import path
from .views import InterestListView

urlpatterns = [
    path('', InterestListView.as_view())
]
