from django.urls import path
from django.views.generic import DetailView

from profiles.views import HomeView, ProfileDetailView, ProfileDeleteView

app_name = 'profiles'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('details/', ProfileDetailView.as_view(), name='detail'),
    path('delete/', ProfileDeleteView.as_view(), name='delete'),
]