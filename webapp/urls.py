from django.urls import path
from . import views



urlpatterns = [
    path('livre-or/', views.livre, name='webapp-livre-or'),
    path('livre-or/add/', views.livreAdd, name= 'webapp-livre-add'),
    path('contact/', views.contact , name = 'webapp-contact'),
    path('publication/', views.publication , name = 'webapp-publication'),
    path('presentation/', views.presentation , name = 'webapp-presentation'),
    path('galerie/<slug:slug>/', views.galerie , name = 'webapp-galerie'),
    path('', views.index , name = 'webapp-index'),
]
