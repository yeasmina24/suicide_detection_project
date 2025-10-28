from django.shortcuts import render
from django.conf import settings
import os
import pandas as pd

def home(request):
    csv_path = os.path.join(settings.BASE_DIR, 'data', 'Suicide_Detection.csv')
    df = pd.read_csv(csv_path)
    data = df.to_dict(orient='records')
    columns = df.columns.tolist()
    return render(request, 'suicide_app/home.html', {'data': data, 'columns': columns})
