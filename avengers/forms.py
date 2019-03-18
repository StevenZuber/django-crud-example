from django import forms
from avengers.models import Avenger


class AvengerForm(forms.ModelForm):
    class Meta:
        model = Avenger
        fields = ('avenger_name',)
