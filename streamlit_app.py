import pickle
import streamlit as st
from streamlit_option_menu import option_menu
# Set page configuration
st.set_page_config(page_title="Diseases predictor",
                   layout="wide",
                   page_icon="🧑‍⚕️")


st.markdown(
    """
    <style>
    body {
        background-color: navy;
        color: white;
    }
    .stButton>button {
        background-color: limegreen;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: white;
        color: navy;
    }
    .stExpanderHeader {
        color: limegreen;
    }
    .stMarkdown h3 {
        color: white;
    }
    .st-expander-content {
        background-color: #1E1E1E;
    }
    .css-1q8dd3e {
        background-color: navy;
    }
    .css-17eq0hr {
        color: limegreen;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)




# Load the saved models
try:
    diabetes_model = pickle.load(open("saved models/diabetes_model.sav", 'rb'))
    heart_disease_model = pickle.load(open("saved models/heart_disease_model.sav", 'rb'))
    parkinsons_model = pickle.load(open("saved models/parkinsons_model.sav", 'rb'))
    breast_cancer_model = pickle.load(open("saved models/breast_cancer_model.sav", 'rb'))
    
except Exception as e:
    st.error(f"Error loading models: {e}")

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Predictor',
                           ['Diabetes Prediction',
                            'Heart Diseases Prediction',
                            'Parkinson Prediction',
                           'Breast Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Helper function to display the result
def display_result(message, is_positive):
    if is_positive:
        st.markdown(f"""
            <div style="background-color:#FF4C4C;padding:10px;border-radius:5px;">
                <h3 style="color:white;text-align:center;">{message}</h3>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="background-color:#4CAF50;padding:10px;border-radius:5px;">
                <h3 style="color:white;text-align:center;">{message}</h3>
            </div>
        """, unsafe_allow_html=True)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    
    st.title('Diabetes Prediction')
    
    
    with st.expander("Click for Input Information"):
        st.write("""
        **Input Information:**
        - **Pregnancies**: Number of times pregnant.
        - **Glucose**: Plasma glucose concentration after 2 hours in an oral glucose tolerance test.
        - **Blood Pressure**: Diastolic blood pressure (mm Hg).
        - **Skin Thickness**: Triceps skin fold thickness (mm).
        - **Insulin**: 2-Hour serum insulin (mu U/ml).
        - **BMI**: Body mass index (weight in kg/(height in m)^2).
        - **Diabetes Pedigree Function**: A function that scores the likelihood of diabetes based on family history.
        - **Age**: Age of the person in years.
        """)

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # Code for Prediction
    if st.button('Diabetes Test Result'):
        try:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                          BMI, DiabetesPedigreeFunction, Age]
            user_input = [float(x) for x in user_input]

            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                display_result('The person is diabetic', True)
            else:
                display_result('The person is not diabetic', False)
        except Exception as e:
            st.error(f"Error in Diabetes Prediction: {e}")

# Heart Disease Prediction Page
if selected == 'Heart Diseases Prediction':
    st.title('Heart Disease Prediction')
    
    with st.expander("Click for Input Information"):
       st.write("""
       **Input Information:**
       - **Age**: Age of the patient in years.
       - **Sex**: Sex of the patient (1 = male, 0 = female).
       - **Chest Pain Type (cp)**: 
         - 0 = typical angina 
         - 1 = atypical angina 
         - 2 = non-anginal pain 
         - 3 = asymptomatic
       - **Resting Blood Pressure (trestbps)**: In mm Hg on admission to the hospital.
       - **Serum Cholesterol (chol)**: In mg/dL.
       - **Fasting Blood Sugar (fbs)**: > 120 mg/dL (1 = true, 0 = false).
       - **Resting Electrocardiographic Results (restecg)**: 
         - 0 = normal 
         - 1 = ST-T wave abnormality 
         - 2 = probable or definite left ventricular hypertrophy.
       - **Maximum Heart Rate Achieved (thalach)**.
       - **Exercise-Induced Angina (exang)**: (1 = yes, 0 = no).
       - **ST Depression (oldpeak)**: Induced by exercise relative to rest.
       - **Slope of Peak Exercise ST Segment (slope)**: 
         - 0 = upsloping 
         - 1 = flat 
         - 2 = downsloping.
       - **Number of Major Vessels Colored by Fluoroscopy (ca)**: (0-3).
       - **Thalassemia (thal)**: 
         - 1 = normal 
         - 2 = fixed defect 
         - 3 = reversible defect.
       """)
       
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal')

    # Code for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]

            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                display_result('The person is having heart disease', True)
            else:
                display_result('The person does not have any heart disease', False)
        except Exception as e:
            st.error(f"Error in Heart Disease Prediction: {e}")
    
# Parkinson's Prediction Page
if selected == "Parkinson Prediction":
    st.title("Parkinson's Disease Prediction")
    
    with st.expander("Click for Input Information"):
        st.write("""
        **Input Information:**
        - **MDVP:Fo(Hz)**: Average vocal fundamental frequency.
        - **MDVP:Fhi(Hz)**: Maximum vocal fundamental frequency.
        - **MDVP:Flo(Hz)**: Minimum vocal fundamental frequency.
        - **MDVP:Jitter(%)**, **MDVP:Jitter(Abs)**, **MDVP:RAP**, **MDVP:PPQ**, **Jitter:DDP**: Measures of variation in fundamental frequency.
        - **MDVP:Shimmer**, **MDVP:Shimmer(dB)**, **Shimmer:APQ3**, **Shimmer:APQ5**, **MDVP:APQ**, **Shimmer:DDA**: Measures of variation in amplitude.
        - **NHR**, **HNR**: Measures of ratio of noise to tonal components in the voice.
        - **RPDE**, **D2**: Nonlinear dynamical complexity measures.
        - **DFA**: Signal fractal scaling exponent.
        - **spread1**, **spread2**, **PPE**: Nonlinear measures of fundamental frequency variation.
        """)

    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")

    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")

    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")

    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")

    with col5:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")

    with col1:
        RAP = st.text_input("MDVP:RAP")

    with col2:
        PPQ = st.text_input("MDVP:PPQ")

    with col3:
        DDP = st.text_input("Jitter:DDP")

    with col4:
        Shimmer = st.text_input("MDVP:Shimmer")

    with col5:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")

    with col1:
        APQ3 = st.text_input("Shimmer:APQ3")

    with col2:
        APQ5 = st.text_input("Shimmer:APQ5")

    with col3:
        APQ = st.text_input("MDVP:APQ")

    with col4:
        DDA = st.text_input("Shimmer:DDA")

    with col5:
        NHR = st.text_input("NHR")

    with col1:
        HNR = st.text_input("HNR")

    with col2:
        RPDE = st.text_input("RPDE")

    with col3:
        DFA = st.text_input("DFA")

    with col4:
        spread1 = st.text_input("spread1")

    with col5:
        spread2 = st.text_input("spread2")

    with col1:
        D2 = st.text_input("D2")

    with col2:
        PPE = st.text_input("PPE")

    # Code for Prediction
    if st.button("Parkinson's Test Result"):
        try:
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer,
                          Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            user_input = [float(x) for x in user_input]

            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                display_result("The person has Parkinson's disease", True)
            else:
                display_result("The person does not have Parkinson's disease", False)
        except Exception as e:
            st.error(f"Error in Parkinson's Prediction: {e}")

# Sidebar option for Breast Cancer Classification
if selected == 'Breast Cancer Prediction':
    st.title("Breast Cancer Prediction")

    with st.expander("Click for Input Information"):
        st.write("""
        **Input Information:**
        - **mean radius**
        - **mean texture**
        - **mean perimeter**
        - **mean area**
        - **mean smoothness**
        - **mean compactness**
        - **mean concavity**
        - **mean concave points**
        - **mean symmetry**
        - **mean fractal dimension**
        - **radius error**
        - **texture error**
        - **perimeter error**
        - **area error**
        - **smoothness error**
        - **compactness error**
        - **concavity error**
        - **concave points error**
        - **symmetry error**
        - **fractal dimension error**
        - **worst radius**
        - **worst texture**
        - **worst perimeter**
        - **worst area**
        - **worst smoothness**
        - **worst compactness**
        - **worst concavity**
        - **worst concave points**
        - **worst symmetry**
        - **worst fractal dimension**
        """)

    # Create columns
    col1, col2, col3, col4, col5 = st.columns(5)

    # Input fields in columns
    with col1:
        mean_radius = st.text_input("Mean Radius")
        mean_texture = st.text_input("Mean Texture")
        mean_compactness = st.text_input("Mean Compactness")
        radius_error = st.text_input("Radius Error")
        worst_radius = st.text_input("Worst Radius")

    with col2:
        mean_perimeter = st.text_input("Mean Perimeter")
        mean_area = st.text_input("Mean Area")
        mean_concavity = st.text_input("Mean Concavity")
        texture_error = st.text_input("Texture Error")
        worst_texture = st.text_input("Worst Texture")

    with col3:
        mean_smoothness = st.text_input("Mean Smoothness")
        mean_concave_points = st.text_input("Mean Concave Points")
        mean_symmetry = st.text_input("Mean Symmetry")
        perimeter_error = st.text_input("Perimeter Error")
        worst_perimeter = st.text_input("Worst Perimeter")

    with col4:
        mean_fractal_dimension = st.text_input("Mean Fractal Dimension")
        radius_error = st.text_input("Radius Error")
        area_error = st.text_input("Area Error")
        smoothness_error = st.text_input("Smoothness Error")
        worst_area = st.text_input("Worst Area")

    with col5:
        compactness_error = st.text_input("Compactness Error")
        concavity_error = st.text_input("Concavity Error")
        concave_points_error = st.text_input("Concave Points Error")
        symmetry_error = st.text_input("Symmetry Error")
        worst_smoothness = st.text_input("Worst Smoothness")

    # Prediction
    if st.button("Breast Cancer Test Result"):
        try:
            # Collecting all user inputs into a list
            user_input = [
                float(mean_radius), float(mean_texture), float(mean_perimeter),
                float(mean_area), float(mean_smoothness), float(mean_compactness),
                float(mean_concavity), float(mean_concave_points), float(mean_symmetry),
                float(mean_fractal_dimension), float(radius_error), float(texture_error),
                float(perimeter_error), float(area_error), float(smoothness_error),
                float(compactness_error), float(concavity_error), float(concave_points_error),
                float(symmetry_error), float(worst_radius), float(worst_texture),
                float(worst_perimeter), float(worst_area), float(worst_smoothness),
                float(worst_compactness), float(worst_concavity), float(worst_concave_points),
                float(worst_symmetry), float(worst_fractal_dimension)
            ]
            
            breast_cancer_prediction = breast_cancer_model.predict([user_input])

            if breast_cancer_prediction[0] == 1:
                display_result('The tumor is Malignant (Cancerous)', True)
            else:
                display_result('The tumor is Benign (Non-Cancerous)', False)
        except Exception as e:
            st.error(f"Error in Breast Cancer Prediction: {e}")
