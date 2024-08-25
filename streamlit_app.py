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
    breast_cancer_model = pickle.load(open("saved models/breast_cancer_model.sav",'rb'))
    
    
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
                           icons=['activity', 'heart', 'person','virus'],
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
    
    
    with st.expander("Learn more about the input features"):
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
    
    with st.expander("Learn more about the input features"):
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
    
    with st.expander("Learn more about the input features"):
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
# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':
    st.title("Breast Cancer Prediction")
    with st.expander("Learn more about the input features"):
         st.write("""
    ### Mean Features:
    - **Mean Radius**: The average distance from the center to points on the perimeter of the cell nuclei.
    - **Mean Texture**: The standard deviation of gray-scale values, representing the variation in texture within the nuclei.
    - **Mean Perimeter**: The average perimeter of the nuclei.
    - **Mean Area**: The average area of the nuclei.
    - **Mean Smoothness**: The mean of local variation in radius lengths, indicating how smooth the nuclear boundary is.
    - **Mean Compactness**: Calculated as the perimeter squared divided by the area minus 1, representing the compactness of the nuclei.
    - **Mean Concavity**: The average extent of concave portions of the nuclear contour.
    - **Mean Concave Points**: The number of concave portions in the nuclear contour.
    - **Mean Symmetry**: How symmetric the nuclei are in shape.
    - **Mean Fractal Dimension**: The “coastline approximation” or roughness of the nuclear boundary.

    ### Error Features (Measurement Error):
    - **Radius Error**: The standard deviation of the radius measurement.
    - **Texture Error**: The standard deviation of the texture measurement.
    - **Perimeter Error**: The standard deviation of the perimeter measurement.
    - **Area Error**: The standard deviation of the area measurement.
    - **Smoothness Error**: The standard deviation of the smoothness measurement.
    - **Compactness Error**: The standard deviation of the compactness measurement.
    - **Concavity Error**: The standard deviation of the concavity measurement.
    - **Concave Points Error**: The standard deviation of the concave points measurement.
    - **Symmetry Error**: The standard deviation of the symmetry measurement.
    - **Fractal Dimension Error**: The standard deviation of the fractal dimension measurement.

    ### Worst Features:
    - **Worst Radius**: The largest distance from the center to points on the perimeter.
    - **Worst Texture**: The largest standard deviation of gray-scale values.
    - **Worst Perimeter**: The largest perimeter observed.
    - **Worst Area**: The largest area observed.
    - **Worst Smoothness**: The largest deviation in smoothness.
    - **Worst Compactness**: The highest compactness observed.
    - **Worst Concavity**: The largest extent of concave portions of the nuclear contour.
    - **Worst Concave Points**: The maximum number of concave portions in the nuclear contour.
    - **Worst Symmetry**: The largest asymmetry observed.
    - **Worst Fractal Dimension**: The largest roughness of the nuclear boundary observed.
    """)

    # Input fields in 5 columns
    col1, col2, col3, col4, col5 = st.columns(5)

    input_labels = [
        'mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness',
        'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry',
        'mean fractal dimension', 'radius error', 'texture error', 'perimeter error',
        'area error', 'smoothness error', 'compactness error', 'concavity error',
        'concave points error', 'symmetry error', 'fractal dimension error',
        'worst radius', 'worst texture', 'worst perimeter', 'worst area',
        'worst smoothness', 'worst compactness', 'worst concavity',
        'worst concave points', 'worst symmetry', 'worst fractal dimension'
    ]

    user_input = []

    for i, label in enumerate(input_labels):
        if i % 5 == 0:
            col = col1
        elif i % 5 == 1:
            col = col2
        elif i % 5 == 2:
            col = col3
        elif i % 5 == 3:
            col = col4
        else:
            col = col5
        
        with col:
            user_input.append(col.text_input(label))

    # Prediction
    if st.button("Breast Cancer Test Result"):
        try:
            user_input = [float(x) for x in user_input]
            breast_cancer_prediction = breast_cancer_model.predict([user_input])

            if breast_cancer_prediction[0] == 0:
                display_result('The tumor is Malignant (Cancerous)', True)
            else:
                display_result('The tumor is Benign (Non-Cancerous)', False)
        except Exception as e:
            st.error(f"Error in Breast Cancer Prediction: {e}")

          

