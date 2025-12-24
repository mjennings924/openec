
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('items/', include('items.urls')),
    path('users/', include('users.urls'))
]
