import pandas as pd
import streamlit as st
from src.validator import SalesSheet
from pydantic import ValidationError

def validate_data(df):
    errors = []
    validated_data = []
    
    for index, row in df.iterrows():
        try:
            # Convert DataFrame row to dictionary
            data = row.to_dict()
            
            # Validate data using the SalesSheet model
            validated_record = SalesSheet(**data)
            validated_data.append(validated_record)
            
        except ValidationError as e:
            errors.append(f"Error in row {index + 2}: {str(e)}")
    
    return validated_data, errors

def main():
    st.title("Campaign Data Validator")
    st.write("Upload CSV file for validation")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            # Read CSV file
            df = pd.read_csv(uploaded_file)
            
            st.write("Data Preview:")
            st.dataframe(df.head())
            
            if st.button("Validate Data"):
                with st.spinner("Validating data..."):
                    validated_data, errors = validate_data(df)
                    
                    if errors:
                        st.error("Validation errors were found:")
                        for error in errors:
                            st.write(error)
                    else:
                        st.success("All data was successfully validated!")
                        
                        # Show number of validated records
                        st.write(f"Total validated records: {len(validated_data)}")
                        
                        # Option to download validated data
                        df_validated = pd.DataFrame([data.dict() for data in validated_data])
                        st.download_button(
                            label="Download validated data",
                            data=df_validated.to_csv(index=False),
                            file_name="validated_data.csv",
                            mime="text/csv"
                        )
                    
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()