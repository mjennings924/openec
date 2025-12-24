from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.items_list, name="list"),
    path('new-item/', views.item_new, name="new-item"),
    path('<int:pk>/', views.item_page, name="page")
]