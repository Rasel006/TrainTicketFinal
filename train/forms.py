from django import forms
from .models import Train_list

class AddTrainForm(forms.ModelForm):
    class Meta:
        model = Train_list
        fields = ['name', 'time', 'station', 'destination', 'price', 'seat_formation']

class TrainInfoUpdateForm(forms.ModelForm):
    class Meta:
        model= Train_list
        fields = ['name', 'time', 'station','destination']