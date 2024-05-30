# views.py
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd

def index(request):
    context = {}
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(name)

        try:
            df = pd.read_excel(fs.path(name))

            # Validate the uploaded file
            validation_result = validate_uploaded_file(df)
        except Exception as e:
            validation_result = f"Validation failed: {str(e)}"

        context = {
            'file_url': file_url,
            'validation_result': validation_result
        }

    return render(request, 'index.html', context)

def validate_uploaded_file(df):
    if 'Value A' not in df.columns or 'Value B' not in df.columns:
        return "Validation failed: Columns 'Value A' and 'Value B' are required."

    values_a = df['Value A'].tolist()
    sum_tolerance = 0.0001
    sum_value_a = sum(values_a)
    is_sum_valid = abs(sum_value_a - 1) < sum_tolerance
    is_numeric_value_a = all(isinstance(x, (int, float)) for x in values_a)
    is_numeric_value_b = all(isinstance(x, (int, float)) for x in df['Value B'].tolist())

    if is_sum_valid and is_numeric_value_a and is_numeric_value_b:
        return "File is valid."
    else:
        return "Validation failed: 'Value A' must sum to 1 and both columns must contain only numeric values."
