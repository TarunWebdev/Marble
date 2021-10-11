from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index , name = 'index'),
    path('thecompany', views.thecompany , name = 'thecompany')
]
