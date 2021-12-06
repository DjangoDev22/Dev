from django import forms
from newsletter.models import Subscripers, MailMessages

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscripers
        fields = ['email',]

        widgets= {
            'email': forms.EmailInput(attrs= {'class' : 'subscribe', 'placeholder': 'Enter Your Email'})
        }



class MailMessagesForm(forms.ModelForm):
    class Meta:
        model = MailMessages
        fields = ['title', 'message']

        widgets= {
            'title': forms.TextInput(attrs= {'class' : 'email', 'placeholder': 'Title Here'}),
            'message': forms.Textarea(attrs= {'class' : 'message', 'placeholder': 'Message Here'})
        }
