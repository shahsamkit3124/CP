import streamlit as st
import pandas as pd

# Load data from Excel into a pandas DataFrame
@st.cache_data
def load_data():
    df = pd.read_excel('college_data.xlsx')
    return df

def main():
    st.set_page_config(layout="wide")  # Adjust layout for wider view

    # Custom CSS to disable right-click
    st.markdown("""
        <style>
            body {
                -webkit-user-select: none;  /* Chrome/Safari */        
                -moz-user-select: none;     /* Firefox */
                -ms-user-select: none;      /* IE10+ */
                user-select: none;          /* Standard */
            }
            table {
                pointer-events: none;       /* Disable click events */
            }
        </style>
    """, unsafe_allow_html=True)

    st.title('College Predictor')

    # Load data
    df = load_data()

    # Ensure necessary columns exist
    required_columns = ['SEAT TYPE', 'INSTITUTE DISTRICT', 'CUTOFF (PERCENTILE)', 'BRANCH NAME']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        st.error(f"Missing columns in the uploaded file: {', '.join(missing_columns)}")
        return

    # Instructions and seat category information
    with st.expander("Instructions"):
        st.markdown("""
        **Seat Category Information:**

        - **AI**: All India
        - **DEFOBCS**: Defense Other Backward Class (State Level)
        - **DEFOPENS**: Defense Open (State Level)
        - **DEFRNT1S**: Defense NT1 (State Level)
        - **DEFRNT2S**: Defense NT2 (State Level)
        - **DEFRNT3S**: Defense NT3 (State Level)
        - **DEFROBCS**: Defense OBC (State Level)
        - **DEFRSCS**: Defense SC (State Level)
        - **DEFRVJS**: Defense VJ (State Level)
        - **DEFSCS**: Defense SC (State Level)
        - **EWS**: Economically Weaker Section
        - **GNT1H**: General NT1 (Home University)
        - **GNT1O**: General NT1 (Other Than Home University)
        - **GNT1S**: General NT1 (State Level)
        - **GNT2H**: General NT2 (Home University)
        - **GNT2O**: General NT2 (Other Than Home University)
        - **GNT2S**: General NT2 (State Level)
        - **GNT3H**: General NT3 (Home University)
        - **GNT3O**: General NT3 (Other Than Home University)
        - **GNT3S**: General NT3 (State Level)
        - **GOBCH**: General OBC (Home University)
        - **GOBCO**: General OBC (Other Than Home University)
        - **GOBCS**: General OBC (State Level)
        - **GOPENH**: General Open (Home University)
        - **GOPENO**: General Open (Other Than Home University)
        - **GOPENS**: General Open (State Level)
        - **GSCH**: General SC (Home University)
        - **GSCO**: General SC (Other Than Home University)
        - **GSCS**: General SC (State Level)
        - **GSTH**: General ST (Home University)
        - **GSTO**: General ST (Other Than Home University)
        - **GSTS**: General ST (State Level)
        - **GVJH**: General VJ (Home University)
        - **GVJO**: General VJ (Other Than Home University)
        - **GVJS**: General VJ (State Level)
        - **LNT1H**: Ladies NT1 (Home University)
        - **LNT1O**: Ladies NT1 (Other Than Home University)
        - **LNT1S**: Ladies NT1 (State Level)
        - **LNT2H**: Ladies NT2 (Home University)
        - **LNT2O**: Ladies NT2 (Other Than Home University)
        - **LNT2S**: Ladies NT2 (State Level)
        - **LNT3H**: Ladies NT3 (Home University)
        - **LNT3O**: Ladies NT3 (Other Than Home University)
        - **LNT3S**: Ladies NT3 (State Level)
        - **LOBCH**: Ladies OBC (Home University)
        - **LOBCO**: Ladies OBC (Other Than Home University)
        - **LOBCS**: Ladies OBC (State Level)
        - **LOPENH**: Ladies Open (Home University)
        - **LOPENO**: Ladies Open (Other Than Home University)
        - **LOPENS**: Ladies Open (State Level)
        - **LSCH**: Ladies SC (Home University)
        - **LSCO**: Ladies SC (Other Than Home University)
        - **LSCS**: Ladies SC (State Level)
        - **LSTH**: Ladies ST (Home University)
        - **LSTO**: Ladies ST (Other Than Home University)
        - **LSTS**: Ladies ST (State Level)
        - **LVJH**: Ladies VJ (Home University)
        - **LVJO**: Ladies VJ (Other Than Home University)
        - **LVJS**: Ladies VJ (State Level)
        - **MI**: Minority
        - **ORPHAN**: Orphan
        - **PWDOBCH**: Person With Disability OBC (Home University)
        - **PWDOBCS**: Person With Disability OBC (State Level)
        - **PWDOPENH**: Person With Disability Open (Home University)
        - **PWDOPENS**: Person With Disability Open (State Level)
        - **PWDRNT1H**: Person With Disability NT1 (Home University)
        - **PWDRNT1S**: Person With Disability NT1 (State Level)
        - **PWDRNT2H**: Person With Disability NT2 (Home University)
        - **PWDRNT2S**: Person With Disability NT2 (State Level)
        - **PWDRNT3S**: Person With Disability NT3 (State Level)
        - **PWDROBCH**: Person With Disability OBC (Home University)
        - **PWDROBCS**: Person With Disability OBC (State Level)
        - **PWDRSCH**: Person With Disability SC (Home University)
        - **PWDRSCS**: Person With Disability SC (State Level)
        - **PWDRSTH**: Person With Disability ST (Home University)
        - **PWDRSTS**: Person With Disability ST (State Level)
        - **PWDRVJH**: Person With Disability VJ (Home University)
        - **PWDRVJS**: Person With Disability VJ (State Level)
        - **PWDSCH**: Person With Disability SC (Home University)
        - **PWDSCS**: Person With Disability SC (State Level)
        - **TFWS**: Tuition Fee Waiver Scheme
        """)
        st.header('Enter Student Details')

    # Get sorted unique seat types
    sorted_seat_types = sorted(df['SEAT TYPE'].unique())
    # Multiselect for seat types
    seat_types = st.multiselect('Select Seat Type', sorted_seat_types)
    
    # Get sorted unique regions (INSTITUTE DISTRICT)
    sorted_regions = sorted(df['INSTITUTE DISTRICT'].unique())
    sorted_regions.insert(0, "ALL")  # Add "ALL" option at the beginning
    # Multiselect for regions
    regions = st.multiselect('Select Region (INSTITUTE DISTRICT)', sorted_regions)

    # Branch options
    branches = [
        'Civil Engineering', 'Computer Science and Engineering', 'Electrical Engineering',
        'Electronics and Telecommunication Engg', 'Information Technology', 'Computer Engineering',
        'Mechanical Engineering', 'Chemical Engineering',
        'Computer Science and Engineering(Artificial Intelligence and Machine Learning)',
        'Artificial Intelligence (AI) and Data Science', 'Computer Science and Design',
        'Electronics and Computer Engineering', 'Artificial Intelligence and Data Science',
        'Electronics Engineering', 'Production Engineering[Sandwich]', 'Textile Technology',
        'Computer Science and Technology', 'Dyestuff Technology', 'Fibres and Textile Processing Technology',
        'Food Engineering and Technology', 'Oil,Oleochemicals and Surfactants Technology',
        'Pharmaceuticals Chemistry and Technology', 'Polymer Engineering and Technology',
        'Surface Coating Technology', 'Mechatronics Engineering', 'Electronics and Computer Science',
        'Computer Science and Engineering (Internet of Things and Cyber Security Including Block Chain Technology)',
        'Data Science', 'Computer Science and Engineering(Data Science)', 'Instrumentation Engineering',
        'Computer Science', 'Cyber Security', 'Petro Chemical Technology', 'Aeronautical Engineering',
        'Computer Science and Engineering (IoT)', 'Computer Technology', 'Instrumentation and Control Engineering',
        'Robotics and Automation', 'Automation and Robotics', 'Manufacturing Science and Engineering',
        'Metallurgy and Material Technology', 'Robotics and Artificial Intelligence',
        'Artificial Intelligence and Machine Learning', 'Computer Science (Data Science)', 'Bio Medical Engineering',
        'Civil and Environmental Engineering', 'Electronics and Telecommunication Engineering',
        'Electronics and Telecommunication', 'Plastic Engineering', 'Mechanical and Automation',
        'Artificial Intelligence and Robotics'
    ]
    
    # Add "ALL" option and sort alphabetically
    branches.append("ALL")
    branches = sorted(branches)
    
    # Multiselect for branches
    branch = st.multiselect('Select Branch', branches)

    # Text input for percentile
    percentile = st.text_input('Enter Percentile')

    # Filter data based on user input
    filtered_data = df[
        (df['SEAT TYPE'].isin(seat_types)) &
        (df['INSTITUTE DISTRICT'].isin(regions if "ALL" not in regions else df['INSTITUTE DISTRICT'])) &
        (df['BRANCH NAME'].isin(branch if "ALL" not in branch else df['BRANCH NAME']))
    ]

    if percentile:
        try:
            percentile = float(percentile)
            filtered_data = filtered_data[filtered_data['CUTOFF (PERCENTILE)'] <= percentile]
        except ValueError:
            st.error("Please enter a valid percentile")

    st.header('Filtered Colleges')
    st.write(filtered_data)

if __name__ == '__main__':
    main()
