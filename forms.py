from django.forms import ModelForm
from .models import MvnsCollectedData


class AddDataForm(ModelForm):
    class Meta:
        model = MvnsCollectedData
        fields = '__all__'
        # '__all__' imports all columns in the database
        # if you only want selected columns use a list of column names


class EditDataForm(ModelForm):
    class Meta:
        model = MvnsCollectedData
        fields = ['officerName', 'motoristFirstName', 'motoristMiddleInitial', 'motoristLastName']
