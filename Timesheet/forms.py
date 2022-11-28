from django import forms
from .models import Checkin


class CheckinForm(forms.ModelForm):
    class Meta:
        model = Checkin
        fields = ['user', 'date_checkin', 'hours', 'project']
