from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','message','job']
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'İsim'}),
            'email':forms.EmailInput(attrs={'placeholder':'E-mail adresi'}),
            'message':forms.Textarea(attrs={'placeholder':'Mesajınız','cols':'26'})
        }