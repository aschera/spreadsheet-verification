import pandas as pd

def validate_excel(file_path):
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        return f"Error reading the file: {str(e)}"

    required_columns = ['Value A', 'Value B']
    if not all(column in df.columns for column in required_columns):
        return "Missing required columns."

    if not all(column in required_columns for column in df.columns):
        return "File contains extra columns."

    if not pd.api.types.is_numeric_dtype(df['Value A']):
        return "Column 'Value A' contains non-numeric values."

    if not pd.api.types.is_numeric_dtype(df['Value B']):
        return "Column 'Value B' contains non-numeric values."

    if not abs(df['Value A'].sum() - 1.0) < 1e-6:
        return "The values in 'Value A' do not add up to 1."

    return "File is valid."
