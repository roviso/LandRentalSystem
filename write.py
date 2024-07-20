import os

def write_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for entry in data:
                file.write(', '.join(entry) + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def generate_invoice(invoice_data, file_name, folder_path):
    try:
        # Create the folder relative to the project directory
        absolute_folder_path = os.path.abspath(folder_path)
        os.makedirs(absolute_folder_path, exist_ok=True)
        
        
        with open(os.path.join(folder_path, file_name), 'w') as file:
            for key, value in invoice_data.items():
                file.write(f"{key}: {value}\n")
    except Exception as e:
        print(f"An error occurred while generating the invoice: {e}")