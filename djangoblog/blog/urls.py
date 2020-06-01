from django.urls import path
from .views import blog_list, home

urlpatterns = [
    path('', blog_list),
    path('new/', home),
]