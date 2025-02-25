from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    """Form to create a new message."""
    class Meta:
        model = Message
        fields = ['content']
