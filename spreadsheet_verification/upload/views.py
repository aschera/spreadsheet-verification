from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd
from .models import Upload
import logging

logger = logging.getLogger(__name__)

def index(request):
    context = {}
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)

        try:
            df = pd.read_excel(fs.path(name))

            # Convert the DataFrame to HTML for display
            file_content_html = df.to_html()
            context['file_content_html'] = file_content_html

            # Validate the uploaded file
            validation_result, is_valid = validate_uploaded_file(df)
        except Exception as e:
            validation_result = f"Validation failed: {str(e)}"
            is_valid = False
            logger.error(f"Exception during file validation: {e}")

        # Save the file info, validation result, and validation status to the database
        upload_instance = Upload.objects.create(file=uploaded_file, file_name=uploaded_file.name, validation_result=validation_result, is_valid=is_valid)

        # Include file name, validation result, and validation status in context
        context['file_name'] = uploaded_file.name
        context['validation_result'] = validation_result
        context['is_valid'] = is_valid

    return render(request, 'index.html', context)


def validate_uploaded_file(df):
    required_columns = ['Value A', 'Value B']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        return f"Validation failed: Missing columns {', '.join(missing_columns)}", False

    values_a = df['Value A'].tolist()
    values_b = df['Value B'].tolist()

    # Check if columns contain only numeric values
    is_numeric_value_a = all(isinstance(x, (int, float)) for x in values_a)
    is_numeric_value_b = all(isinstance(x, (int, float)) for x in values_b)
    
    if not is_numeric_value_a or not is_numeric_value_b:
        return "Validation failed: Both 'Value A' and 'Value B' must contain only numeric values.", False

    # Check if 'Value A' sums to 1 within tolerance
    sum_tolerance = 0.0001
    sum_value_a = sum(values_a)
    is_sum_valid = abs(sum_value_a - 1) < sum_tolerance
    
    if not is_sum_valid:
        return f"Validation failed: 'Value A' sums to {sum_value_a}, which is not within tolerance of 1.", False

    return "File is valid.", True
