from django.contrib import admin
from .models import Blog , StoneType , Stone , CarouselCategory , CarouselImages
# Register your models here. 

admin.site.register(Blog)
admin.site.register(StoneType)
admin.site.register(Stone)
admin.site.register(CarouselCategory)
admin.site.register(CarouselImages)