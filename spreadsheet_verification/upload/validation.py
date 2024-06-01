import pandas as pd

def validate_excel(file_path):
    errors = []

    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        return f"Error reading the file: {str(e)}"

    required_columns = ['Value A', 'Value B']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        errors.append(f"Missing required columns: {', '.join(missing_columns)}")

    extra_columns = [col for col in df.columns if col not in required_columns]
    if extra_columns:
        errors.append(f"File contains extra columns: {', '.join(extra_columns)}")

    if not pd.api.types.is_numeric_dtype(df['Value A']):
        errors.append("Column 'Value A' contains non-numeric values.")

    if not pd.api.types.is_numeric_dtype(df['Value B']):
        errors.append("Column 'Value B' contains non-numeric values.")

    if not abs(df['Value A'].sum() - 1.0) < 1e-6:
        errors.append("The values in 'Value A' do not add up to 1.")

    if errors:
        return "Validation failed: " + "; ".join(errors)

    return "File is valid."
