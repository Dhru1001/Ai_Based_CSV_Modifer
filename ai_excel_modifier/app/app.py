from flask import Flask, render_template, request, send_file,session
import os
import uuid
from utils import load_data, save_data, remove_duplicates, apply_custom_rule, modify_rows

app = Flask(__name__)
app.secret_key = '6d85dc0f1a01d8bc75ccf43da6d16cc895ee07eb6735c76d   '

# Ensure log directory exists
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Assign session ID
@app.before_request
def assign_session_id():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())


# Route to the home page (where users can upload a file)
@app.route('/')
def index():
    return render_template('index.html')

# Route to upload file
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    
    if not os.path.exists('data'):
        os.makedirs('data')
    
    file_path = os.path.join('data', file.filename)
    temp_file_path = 'data/temp.csv'
    
    # Save the uploaded file
    file.save(file_path)
    
    # **Erase temp.csv if it exists**
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
    
    # Load data into DataFrame
    df = load_data(file_path)
    if df is None:
        return "Error loading file."
    
    # Render the modify page with options to process data
    return render_template('modify.html', columns=df.columns, data=df.to_html(classes="table table-striped", index=False))

# Route to process the file after upload (remove duplicates, apply filter, etc.)
@app.route('/process', methods=['POST'])
def process_file():
    try:
        global columns_order
        operation = request.form['operation']

        temp_file_path = 'data/temp.csv'
        uploaded_file = request.files.get('file')

        if uploaded_file:
            file_path = os.path.join('data', uploaded_file.filename)
            df = load_data(file_path)
            if df is None:
                raise Exception("Error loading data file.")
            
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)
            
            columns_order = df.columns.tolist()

        elif os.path.exists(temp_file_path):
            df = load_data(temp_file_path)
        else:
            file_path = 'data/input.csv'
            df = load_data(file_path)
            if df is None:
                raise Exception("Error loading data file.")

        if 'columns_order' not in globals():
            columns_order = df.columns.tolist()

        # Process based on operation
        if operation == 'remove_duplicates':
            df = remove_duplicates(df)
            if df is None:
                return render_template('modify.html', error_message="Error removing duplicates.", columns=columns_order)
        elif operation == 'apply_filter':
            column = request.form['column']
            condition = request.form['condition']
            df, error_message = apply_custom_rule(df, column, condition)
            if error_message:
                return render_template(
                    'modify.html',
                    columns=columns_order,
                    data=df.to_html(classes="table table-striped", index=False),
                    error_message=error_message
                )
        elif operation == 'modify_rows':
            modify_operation = request.form['modify_operation']
            if modify_operation == "add":
                row_data = {
                    'ID': request.form['id'],
                    'Name': request.form['name'],
                    'Age': request.form['age']
                }
                df = modify_rows(df, 'add', row_data=row_data)
                if df is None:
                    return render_template('modify.html', error_message="Error adding row.")
            elif modify_operation == "delete":
                column = request.form['delete_column']
                value = request.form['delete_value']
                df = modify_rows(df, 'delete', column=column, value=value)
                if df is None:
                    return render_template('modify.html', error_message="Error deleting row.")

        # Restore original column order
        df = df[columns_order]

        # Save the updated DataFrame to the temporary file
        if not save_data(df, temp_file_path):
            return render_template('modify.html', error_message="Error saving temporary data.")

        # Render the processed data on the page
        return render_template('modify.html', columns=columns_order, data=df.to_html(classes="table table-striped", index=False))

    except Exception as e:
        return render_template('modify.html', error_message=str(e))

# Route to download the processed file
@app.route('/download_output', methods=['GET'])
def download_file():
    temp_file_path = 'data/temp.csv'
    if os.path.exists(temp_file_path):
        # Send the file to the user for download
        return send_file(temp_file_path, as_attachment=True, download_name='processed_file.csv')
    else:
        return "File not found. Please process a file first."
    
# Download log
@app.route('/download_log', methods=['GET'])
def download_log():
    session_id = session.get('session_id')
    log_file = f"{LOG_DIR}/{session_id}_modification.log"
    if os.path.exists(log_file):
        return send_file(log_file, as_attachment=True, download_name='operation_log.log')
    return "No log available."

if __name__ == '__main__':
    app.run(debug=True)
