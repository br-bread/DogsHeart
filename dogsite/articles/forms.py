from django import forms

from .models import Breed


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed

        fields = ('size', 'activity', 'cost',
                  'friendliness', 'intellect', 'noise',)

        labels = {
            'size': 'Размер',
            'activity': 'Активность',
            'cost': 'Стоимость содержания',
            'friendliness': 'Дружелюбность',
            'intellect': 'Интеллект',
            'noise': 'Шум',
        }

        widgets = {
            'size': forms.Select(
                attrs={'class': 'form-control',
                       'required': False}),
            'activity': forms.Select(
                attrs={'class': 'form-control',
                       'required': False}),
            'cost': forms.Select(
                attrs={'class': 'form-control',
                       'required': False}),
            'friendliness': forms.Select(
                attrs={'class': 'form-control',
                       'required': False}),
            'intellect': forms.Select(
                attrs={'class': 'form-control',
                       'required': False}),
            'noise': forms.Select(
                attrs={'class': 'form-control',
                       'required': False}),
        }
