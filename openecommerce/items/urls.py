from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'items'

urlpatterns = [
    path('', views.items_list, name="list"),
    path('new-item/', views.item_new, name="new-item"),
    path('<int:pk>/', views.item_page, name="page")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)