from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index , name = 'index'),
    path('thecompany', views.thecompany , name = 'thecompany'),
    path('management', views.management , name = 'management'),
    path('capacity', views.capacity , name = 'capacity'),

    path('stonecollection', views.stonecollection , name = 'stonecollection'),
    path('blogs', views.blogs , name = 'blogs'),

    path('contact', views.contact , name = 'contact'),
    path('stonecraft', views.stonecraft , name = 'stonecraft'),
    path('whysmg', views.whysmg , name = 'whysmg'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
