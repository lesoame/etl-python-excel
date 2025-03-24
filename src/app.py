import pandas as pd
import streamlit as st
from validator import SalesSheet
from datetime import datetime
from pydantic import ValidationError

def validate_row(row):
    try:
        # Convert date string to date object
        row['Date'] = datetime.strptime(row['Date'], '%Y-%m-%d').date()
        
        # Convert numeric columns to appropriate types
        row['Amount_spent'] = float(row['Amount_spent'])
        row['Impressions'] = int(row['Impressions'])
        if pd.notna(row['Link_clicks']):
            row['Link_clicks'] = int(row['Link_clicks'])
        if pd.notna(row['Conversions']):
            row['Conversions'] = int(row['Conversions'])
            
        # Validate using Pydantic model
        user = SalesSheet(**row)
        return True, None
    except ValidationError as e:
        return False, str(e)
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def main():
    st.title("CSV Data Validator")
    st.write("Upload your CSV file to validate against the data model")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Preview of uploaded data:")
            st.dataframe(df.head())

            # Validation results containers
            valid_rows = []
            invalid_rows = []
            
            # Progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Validate each row
            total_rows = len(df)
            for index, row in df.iterrows():
                progress = (index + 1) / total_rows
                progress_bar.progress(progress)
                status_text.text(f"Processing row {index + 1} of {total_rows}")
                
                is_valid, error = validate_row(row.to_dict())
                if is_valid:
                    valid_rows.append(index)
                else:
                    invalid_rows.append((index, error))
            
            # Display results
            st.success(f"Validation complete! Valid rows: {len(valid_rows)}")
            if invalid_rows:
                st.error(f"Invalid rows found: {len(invalid_rows)}")
                st.write("Details of invalid rows:")
                for row_index, error in invalid_rows:
                    st.write(f"Row {row_index + 1}: {error}")
            
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()