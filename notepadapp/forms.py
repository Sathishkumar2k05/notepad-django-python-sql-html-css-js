from django import forms
from .models import *

class NotePadForm(forms.ModelForm):

    class Meta:

        model = NotePad
        fields = ['title','body']

        widgets = {
            'title':forms.TextInput(attrs={
                'class':"form-control",
                'style':'width:300px;',
            }),
            'body':forms.Textarea(attrs={
                'style':'width:100%; min-height:100%; overflow:hidden;',
                'oninput':'this.style.height="auto"; this.style.height=this.scrollHeight + "px";'
            })
        }