import streamlit as st
import pandas as pd

# Load data from Excel into a pandas DataFrame
@st.cache_data
def load_data():
    df = pd.read_excel('college_data.xlsx')
    return df

def main():
    st.title('College Predictor')

    # Load data
    df = load_data()
    
    # Debugging: Print column names to ensure they are correct
    st.write("Columns in the uploaded file:", df.columns.tolist())

    # Ensure necessary columns exist
    if 'SEAT TYPE' not in df.columns or 'INSTITUTE DISTRICT' not in df.columns:
        st.error("'SEAT TYPE' or 'INSTITUTE DISTRICT' column not found in the uploaded file.")
        return
    
    # Sidebar inputs
    st.sidebar.header('Enter Student Details')
    percentile_cutoff = st.sidebar.number_input('Enter Cutoff Percentile', min_value=0, max_value=100, value=50, format="%d")
    
    # Get sorted unique seat types
    sorted_seat_types = sorted(df['SEAT TYPE'].unique())
    # Multiselect for seat types
    seat_types = st.sidebar.multiselect('Select Seat Type', sorted_seat_types)
    
    # Get sorted unique regions (INSTITUTE DISTRICT)
    sorted_regions = sorted(df['INSTITUTE DISTRICT'].unique())
    sorted_regions.insert(0, "ALL")  # Add "ALL" option at the beginning
    # Multiselect for regions
    regions = st.sidebar.multiselect('Select Region (INSTITUTE DISTRICT)', sorted_regions)

    if st.sidebar.button('Submit'):
        # Filtering and sorting based on inputs
        if "ALL" in regions:
            filtered_data = df[
                (df['CUTOFF (PERCENTILE)'] <= percentile_cutoff) &
                (df['SEAT TYPE'].isin(seat_types))
            ]
        else:
            filtered_data = df[
                (df['CUTOFF (PERCENTILE)'] <= percentile_cutoff) &
                (df['SEAT TYPE'].isin(seat_types)) &
                (df['INSTITUTE DISTRICT'].isin(regions))
            ]

        filtered_data = filtered_data.sort_values(by='CUTOFF (PERCENTILE)', ascending=False)
        
        # Format numerical columns to not include commas
        formatted_data = filtered_data.copy()
        formatted_data['INSTITUTE CODE'] = formatted_data['INSTITUTE CODE'].astype(str)
        formatted_data['CUTOFF (RANK)'] = formatted_data['CUTOFF (RANK)'].apply(lambda x: '{:.0f}'.format(x))
        formatted_data['CUTOFF (PERCENTILE)'] = formatted_data['CUTOFF (PERCENTILE)'].apply(lambda x: '{:.2f}'.format(x))

        # Display filtered results
        st.subheader('Predicted Colleges')
        st.write(formatted_data)

if __name__ == '__main__':
    main()
