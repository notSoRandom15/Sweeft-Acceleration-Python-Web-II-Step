from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_random_url, name="create_random_url"),
    path("create/<str:short_name>/", views.create_custom_url,  name="create_custom_url"),
    path("<str:short_name>/", views.redirect_url, name="redirect_url"),
    path('', views.homePage, name='home'),

    
]
