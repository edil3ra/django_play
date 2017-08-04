from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class MessageForm(forms.Form):
    recipient = forms.ModelChoiceField(
        label=_('Recipient'), queryset=User.objects.all(), required=True)

    message = forms.CharField(
        label=_('Message'), widget=forms.Textarea, required=True)

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.fields['recipient'].queryset = self.fields[
            'recipient'].queryset.exclude(pk=request.user.pk)
