# urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include ('post.urls'))
]