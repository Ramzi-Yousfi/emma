from django.contrib import admin
from .models import *

# Register your models here.
class PublicationImageInline(admin.StackedInline):
    model = PublicationImage
    extra = 1
class PublicationAdmin(admin.ModelAdmin):
    inlines = [PublicationImageInline]
    class Meta:
        model = Publication

class GaleriesImageInline(admin.StackedInline):
    model = GaleriesImage
    extra = 1
class GaleriesAdmin(admin.ModelAdmin):
    
    list_display = ['slug']
    inlines = [GaleriesImageInline]
    class Meta:
        model = Galeries


class LivreAdmin(admin.ModelAdmin):
    list_display = ['nom', 'date_update','status']
    

admin.site.register(Contact)
admin.site.register(Livre, LivreAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(PresentationCard)
admin.site.register(Presentation)
admin.site.register(Galeries, GaleriesAdmin)