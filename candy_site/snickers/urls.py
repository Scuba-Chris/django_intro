from django.urls import path
from .views import HomePageView, AboutSnickersView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about_snickers/', AboutSnickersView.as_view(), name='about_snickers')
]