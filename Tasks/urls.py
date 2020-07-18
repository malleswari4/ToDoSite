from django.urls import path
from Tasks import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('edit/<str:pk>',views.edit,name="edit"),
    path('delete/<str:pk>',views.delete,name='delete')
]