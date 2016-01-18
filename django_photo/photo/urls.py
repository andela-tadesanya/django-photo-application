from django.conf.urls import url
from .views import HomePageView, DashboardView, ImageUploadView, DeleteImageView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^user/', DashboardView.as_view(), name='user_home'),
    url(r'^upload/', ImageUploadView.as_view(), name='upload'),
    url(r'^delete/', DeleteImageView.as_view(), name='delete'),
]
