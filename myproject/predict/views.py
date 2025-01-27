from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import PredictionDataForm
from .models import PredictionData
import joblib

def data_input_view(request):
    if request.method == 'POST':
        form = PredictionDataForm(request.POST)
        if form.is_valid():
             prediction_data = form.save()
             # モデルの読み込み
             model = joblib.load("../結果データ/route_model.pkl")
             # 新しいデータの予測
             new_data = [[prediction_data.weather, prediction_data.time, prediction_data.road, prediction_data.package]]
             predicted_route = model.predict(new_data)[0]

             return render(request, 'predict/prediction_result.html', {'predicted_route': predicted_route})

            
    else:
        form = PredictionDataForm()
    return render(request, 'predict/data_input.html', {'form': form})

def data_list_view(request):
    data_list = PredictionData.objects.all()
    return render(request, 'predict/data_list.html', {'data_list': data_list})