from django.urls import path

from .views import blog, blog_add


urlpatterns = [

    path("",blog),
    path("add/", blog_add)
   
]