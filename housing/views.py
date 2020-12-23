from django.shortcuts import render
from housing.forms import HouseForm
from pandas import DataFrame
import joblib

model = joblib.load('model.joblib')

features = ['property_type', 'bed_type', 'room_type', 'neighbourhood_cleansed', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'minimum_nights']

def index(request):

	if request.POST:
		form = HouseForm(request.POST)
		data = dict()
		for ft in features:
			data[ft] = [request.POST.get(ft),]
		data = DataFrame(data, columns=features)
		price = round(model.predict(data)[0], 1)
		return render(request, 'index.html', {'form': form, 'price': price})
	else:
		form = HouseForm()
	return render(request, 'index.html', {'form': form, 'price': 0})