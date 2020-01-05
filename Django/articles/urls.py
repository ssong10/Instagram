from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create),
    path('create/<int:user_id>/',views.user_create)
]