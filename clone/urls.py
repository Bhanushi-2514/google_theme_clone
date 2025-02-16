from django.urls import path
from .views import home, set_theme

urlpatterns = [
    path('', home, name='home'),
    path('set-theme/<str:theme_name>/', set_theme, name='set_theme'),
]

