
from distutils.log import error
import django
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
from .form import ContactForm , LivreOrForm
from django.core.mail import send_mail
from .models import *
from django.contrib import messages
import os
from django.core.paginator import Paginator




def base(request):
    submenu = Galeries.objects.all()
    return  {'submenu': submenu}


def index(request):
    return render(request, 'home.html')





def publication (request):
    publications = Publication.objects.all().order_by('-id')
    paginator = Paginator(publications, 3 )# Show 25 contacts per page
    page = request.GET.get('page')
    publication = paginator.get_page(page)
    return render(request, 'publication.html', {'publications': publication})
    

def livre(request):
    comments  = Livre.objects.all().order_by('-id')
    return render(request, 'livre_or/index.html',{'comments': comments}) 


def livreAdd(request):
    form = LivreOrForm()
    if  request.method == 'POST':
        form = LivreOrForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre commentaire a été envoyé avec succès il sera publié après validation de l\'administrateur')
            return HttpResponseRedirect('/livre-or')
    return render(request, 'livre_or/add.html', {'form': form})


def presentation (request):
    cards = PresentationCard.objects.all()
    presentation = Presentation.objects.first()
    
    return render(request, 'presentation.html', {'cards': cards, 'presentation': presentation})


def galerie(request, slug):
    galeries_images = GaleriesImage.objects.filter(galeries__slug=slug).order_by('-id')
    galerie = Galeries.objects.filter(slug=slug).first()
    page = request.GET.get('page')
    paginator = Paginator(galeries_images, 9)
    galeries_images = paginator.get_page(page)

    return render(request, 'galeries.html', {'galeries_images': galeries_images, 'galerie': galerie,'pages':page})



from mailjet_rest import Client
api_key = '3294c0d31c183483bc8383f9ea0f41ae'
api_secret = 'e78726c4090e32d546810ff46f3fe5c9'
def contact(request):
    presentation = Presentation.objects.first()
    form = ContactForm()
    if  request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            #form.save()
            mailjet = Client(auth=(api_key, api_secret), version='v3.1')
            data = {
            'Messages': [
                    {
                        "From": {
                              "Email": request.POST.get('email'),
                              "Name": request.POST.get('nom')
                        },
                        "To": [
                            {
                                "Email": "emma.Rivoal.pro@gmail.com",
                                "Name": "Emma"
                            }
                        ],
                       	"TemplateID": 4006209,
			            "TemplateLanguage": True,
			            "Subject": "[[data:country:""France""]]",
                        "Variables": {
                "nom":request.POST.get('nom') ,
                "email": request.POST.get('email') ,
                "sujet": request.POST.get('sujet') ,
                "message": request.POST.get('message') ,
            }
                    }
                ]
            }
            result = mailjet.send.create(data=data)
            print (result.status_code)
            print (result.json())
          

            form = ContactForm()
            message = ('Votre message a été envoyé avec succès')
            return render (request ,'contact.html' , {'message': message,'form': form,'presentation': presentation})
        else: 
            error = ('Votre message n\'a pas pu être envoyé  merci de vérifier vos informations ou de ressayer ultérieurement')
            return render (request ,'contact.html' ,{'error': error ,'form': form ,'presentation': presentation})
    return render(request, 'contact.html', {'form': form,'presentation': presentation})


