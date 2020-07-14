from django.urls import path
from Tasks import views

urlpatterns = [
    path('',views.home,name='home'),
    path('edit/<str:pk>',views.edit,name="edit"),
    path('delete/<str:pk>',views.delete,name='delete')
]