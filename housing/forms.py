from django import forms
import joblib

values_dict = joblib.load('values_dict.joblib')

class HouseForm(forms.Form):
	property_type = forms.ChoiceField(label='Тип жилья', choices=values_dict['property_type'], widget=forms.Select(attrs={'class': 'form-control input-lg', 'placeholder': "Выберете тип жилья"}))
	bed_type = forms.ChoiceField(label='Тип спальных мест', choices=values_dict['bed_type'], widget=forms.Select(attrs={'class': 'form-control input-lg', 'placeholder': "Выберете тип спальных мест"}))
	room_type = forms.ChoiceField(label='Тип комнат', choices=values_dict['room_type'], widget=forms.Select(attrs={'class': 'form-control input-lg', 'placeholder': "Выберете тип комнат"}))
	neighbourhood_cleansed = forms.ChoiceField(label='Район', choices=values_dict['neighbourhood_cleansed'], widget=forms.Select(attrs={'class': 'form-control input-lg', 'placeholder': "Выберете район"}))

	accommodates = forms.DecimalField(label='Количество гостей', min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control input-lg', 'placeholder': "Введите количество гостей"}))
	bathrooms = forms.DecimalField(label='Количество ванных комнат', min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control input-lg', 'placeholder': "Введите количество ванных комнат"}))
	bedrooms = forms.DecimalField(label='Количество спален', min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control input-lg', 'placeholder': "Введите количество спален"}))
	beds = forms.DecimalField(label='Количество спальных мест', min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control input-lg', 'placeholder': "Введите количество спальных мест"}))
	minimum_nights = forms.DecimalField(label='Минимальное количество ночей', min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control input-lg', 'placeholder': "Введите минимальное количество ночей"}))
