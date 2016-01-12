from django.conf.urls import url
from .views import HomePageView, DashboardView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^user/', DashboardView.as_view(), name='user_home'),
]
