from django.forms import ModelForm
from .models import Contact,Livre
from django.forms import TextInput, EmailInput, Textarea
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'email','sujet', 'message',]
        labels = {
            'nom': 'Nom',
            'email': 'Email',
            'sujet': 'Sujet',
            'message': 'Message',
           
   
        }
        widgets = {
            'nom': TextInput(attrs={'class': 'form-control','required':'required'}),
            'email': TextInput(attrs={'class': 'form-control','required':'required'}),
            'sujet': TextInput(attrs={'class': 'form-control','required':'required'}),
            'message': Textarea(attrs={'class': 'form-control','required':'required'}),
            
        }
       
class LivreOrForm(ModelForm):
    nom = forms.CharField( widget=forms.TextInput(attrs={
        'class': 'form-control','placeholder': 'Nom ou Entreprise','required':'required'
        }))
    message = forms.CharField( widget=forms.Textarea(attrs={
        'class': 'form-control','placeholder': 'Votre Commentaire','required':'required'
        }))
    class Meta:
        model = Livre
        fields = ['nom', 'message',]
        