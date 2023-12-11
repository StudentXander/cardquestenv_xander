from django.urls import path
from django.views import HomePageView
from cardquest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name = 'home'),
]