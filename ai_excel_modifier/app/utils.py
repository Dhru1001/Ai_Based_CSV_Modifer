import os
import pandas as pd
import logging
from flask import session

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Function to initialize the log file for a specific session
def get_log_file():
    session_id = session.get('session_id')
    if not session_id:
        raise Exception("Session ID is missing.")
    log_file = f"{LOG_DIR}/{session_id}_modification.log"
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            f.write("Log initialized for session.\n")
    return log_file

# Function to write logs
def write_log(message):
    try:
        log_file = get_log_file()
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')
        logging.info(message)
    except Exception as e:
        print(f"Error writing log: {e}")

def load_data(file_path):
    """Load data from the input file."""
    if not os.path.exists(file_path):
        write_log(f"Input file not found: {file_path}")
        print(f"Error: {file_path} not found.")
        return None
    try:
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            df = pd.read_csv(file_path)
        write_log(f"Input file loaded successfully: {file_path}")
        return df
    except Exception as e:
        write_log(f"Error loading input file: {e}")
        print(f"Error loading input file: {e}")
        return None

def remove_duplicates(df, subset=None):
    """Remove duplicate rows based on specific columns, treating case variations as duplicates."""
    print("\nRemoving duplicate rows...")
    original_length = len(df)

    # Normalize 'Name' column to lowercase to handle case variations
    df.loc[:, 'Name'] = df['Name'].str.strip().str.lower()  # Convert 'Name' to lowercase and strip spaces

    # Remove duplicates based on 'Name' column (case-insensitive)
    df = df.drop_duplicates(subset=['Name'], inplace=False)
    
    # Restore 'Name' column to original case
    df.loc[:, 'Name'] = df['Name'].str.title()  # Capitalize the first letter for the 'Name' column

    cleaned_length = len(df)
    removed_count = original_length - cleaned_length
    
    write_log(f"Removed {removed_count} duplicate rows.")
    print(f"Removed {removed_count} duplicate rows.")
    return df

def apply_custom_rule(df, column, condition):
    """Apply user-defined filtering rules to the data."""
    try:
        # Split the condition into operator and value
        condition_parts = condition.split(' ')
        if len(condition_parts) != 2:
            raise ValueError("Condition must be in the format: Operator Value (e.g., > 5 or == 'John')")

        operator, value = condition_parts

        # Check if the column exists in the dataframe
        if column not in df.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")

        # Check if the column is numeric or string
        if df[column].dtype == 'O':  # Object (string) column
            # Handle string condition
            if operator == '==' and value.startswith("'") and value.endswith("'"):
                value = value[1:-1]  # Remove quotes around the string

            # Handle cases where a numeric condition is provided for a string column
            if operator in ['>', '<', '>=', '<=', '!='] and value.replace('.', '', 1).isdigit():
                raise TypeError(f"Cannot apply numeric condition to a string column. Please check your condition for '{column}'.")

            # Create a valid query for string values
            query = f"{column} {operator} {repr(value)}"
        else:  # Numeric column
            try:
                value = float(value)  # Convert to float for numeric comparison
                # Create a valid query for numeric values
                query = f"{column} {operator} {value}"
            except ValueError:
                raise TypeError(f"Invalid value '{value}' for numeric comparison. Please provide a valid number.")

        # Apply the query to filter the DataFrame
        filtered_df = df.query(query)

        # If no rows match, return the original dataframe
        return filtered_df if not filtered_df.empty else df, None

    except ValueError as e:
        return df, f"ValueError: {e}"  # Return the original DataFrame and error message
    except TypeError as e:
        return df, f"TypeError: {e}"  # Return the original DataFrame and error message
    except Exception as e:
        return df, f"Error applying filter: {e}"  # Return the original DataFrame and error message

def filter_logs(criteria):
    """Filter logs based on the given criteria."""
    filtered_logs = []
    try:
        with open('logs/modification.log', 'r') as log_file:
            for line in log_file:
                if criteria in line:
                    timestamp, message = line.split(' - ', 1)
                    filtered_logs.append({'timestamp': timestamp, 'message': message.strip()})
    except Exception as e:
        write_log(f"Error filtering logs: {e}")
    return filtered_logs

def modify_rows(df, operation, row_data=None, column=None, value=None, log=True):
    """Add or delete rows in the data."""
    
    if operation == "add":
        # Add a new row if row_data is provided
        if row_data:
            # Ensure row_data keys match column names
            if set(row_data.keys()) == set(df.columns):
                df = pd.concat([df, pd.DataFrame([row_data])], ignore_index=True)
                write_log("Added a new row.")
                print("Added a new row.")
            else:
                print("Row data keys do not match column names.")
        else:
            print("No row data provided to add.")
    
    elif operation == "delete":
        # Delete rows that match the condition
        if column and value:
            try:
                # Ensure the column is string type to avoid issues with .str methods
                df[column] = df[column].astype(str)

                # Perform the delete operation
                df_before_deletion = df.copy()
                df = df[df[column].str.strip().str.lower() != value.lower()]

                deleted_count = len(df_before_deletion) - len(df)
                write_log(f"Deleted {deleted_count} rows where {column} == {value}.")
                print(f"Deleted {deleted_count} rows where {column} == {value}.")
            except KeyError:
                print(f"Error: Column '{column}' not found.")
            except Exception as e:
                print(f"An error occurred while deleting rows: {e}")
        else:
            print("Column or value missing for deletion.")
    
    return df

def validate_row(row_data, columns):
    """Validate the new row data against expected columns."""
    return all(col in columns for col in row_data.keys())

def save_data(df, file_path):
    """Save the modified data to an output file."""
    try:
        if df.empty:
            print("Error: DataFrame is empty. No data to save.")
            return False
        
        if file_path.endswith('.xlsx'):
            df.to_excel(file_path, index=False)
        elif file_path.endswith('.json'):
            df.to_json(file_path, orient='records', lines=True)
        else:
            df.to_csv(file_path, index=False)
        
        print(f"Modified file saved successfully as: {file_path}")
        return True
    except Exception as e:
        print(f"Error saving output file: {e}")
        return False

