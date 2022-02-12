from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('about_us/', views.about_us),
    path('courses/<int:id>', views.course),
]
