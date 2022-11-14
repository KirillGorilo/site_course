from django.contrib import admin
from django.urls import path, include
from burger_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('burger_app.urls'))
]
