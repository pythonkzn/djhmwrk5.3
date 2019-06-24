from django import forms

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    cityout = forms.CharField(label='Город отправления')
    cityin = forms.ChoiceField(widget=AjaxInputWidget(url='api/city_ajax', attrs={'class': 'inline right-margin'}),
                             label='Город прибытия')
    dateflight = forms.DateField(label='Дата', widget=forms.SelectDateWidget())
