from django.contrib import admin
from .models import *


# Register your models here.
class PublicationImageInline(admin.StackedInline):
    model = PublicationImage
    extra = 1
    actions=None
class PublicationAdmin(admin.ModelAdmin):
    inlines = [PublicationImageInline]
    class Meta:
        model = Publication

class GaleriesImageInline(admin.StackedInline):
    model = GaleriesImage
    extra = 1
    actions=None
    def has_change_permission(self, request, obj) -> bool:
        
        return None
    
    fields = ( 'image_tag','photo' )
    readonly_fields = ('image_tag',)

   
class GaleriesAdmin(admin.ModelAdmin):
    
    list_display = ['slug', 'titre', ]
    actions=None
    fields= ('titre', 'slug', 'background_photo', 'image_tag')
    readonly_fields = ('slug','image_tag',)
    inlines = [GaleriesImageInline]
    class Meta:
        model = Galeries


class LivreAdmin(admin.ModelAdmin):
    list_display = ['nom', 'date_update','status']
    actions=None
    

class PresentationCardAdmin(admin.ModelAdmin):
    readonly_fields = ('card_image','titre',)
    actions=None
    
    
    class Meta:
        model = PresentationCard
        


    
    

admin.site.register(Contact)
admin.site.register(Livre, LivreAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(PresentationCard, PresentationCardAdmin)
admin.site.register(Presentation)
admin.site.register(Galeries, GaleriesAdmin)