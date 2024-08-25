import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Diseases Predictor",
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
  
    st.write("😎Developed by Aritra Sarkar")

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

# Function to automatically fill inputs from bulk text
def auto_fill_inputs(input_data, num_inputs):
    input_data = input_data.strip().split()
    if len(input_data) == num_inputs:
        return input_data
    else:
        st.error(f"Expected {num_inputs} inputs, but got {len(input_data)}. Please ensure you provide exactly {num_inputs} space-separated values.")
        return [""] * num_inputs

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    
    st.title('💉Diabetes Prediction')
    
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

    bulk_input = st.text_area("Paste all inputs here (space-separated values):", "")
    if bulk_input:
        inputs = auto_fill_inputs(bulk_input, 8)
    else:
        inputs = [""] * 8

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', inputs[0])

    with col2:
        Glucose = st.text_input('Glucose Level', inputs[1])

    with col3:
        BloodPressure = st.text_input('Blood Pressure value', inputs[2])

    with col1:
        SkinThickness = st.text_input('Skin Thickness value', inputs[3])

    with col2:
        Insulin = st.text_input('Insulin Level', inputs[4])

    with col3:
        BMI = st.text_input('BMI value', inputs[5])

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', inputs[6])

    with col2:
        Age = st.text_input('Age of the Person', inputs[7])

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
    st.title('🫀Heart Disease Prediction')
    
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

    bulk_input = st.text_area("Paste all inputs here (space-separated values):", "")
    if bulk_input:
        inputs = auto_fill_inputs(bulk_input, 13)
    else:
        inputs = [""] * 13

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age', inputs[0])

    with col2:
        sex = st.text_input('Sex', inputs[1])

    with col3:
        cp = st.text_input('Chest Pain types', inputs[2])

    with col1:
        trestbps = st.text_input('Resting Blood Pressure', inputs[3])

    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl', inputs[4])

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', inputs[5])

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', inputs[6])

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', inputs[7])

    with col3:
        exang = st.text_input('Exercise Induced Angina', inputs[8])

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', inputs[9])

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', inputs[10])

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy', inputs[11])

    with col1:
        thal = st.text_input('thal', inputs[12])

    # Code for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]

            heart_diagnosis = heart_disease_model.predict([user_input])

            if heart_diagnosis[0] == 1:
                display_result('The person is having heart disease', True)
            else:
                display_result('The person does not have any heart disease', False)
        except Exception as e:
            st.error(f"Error in Heart Disease Prediction: {e}")

# Parkinson's Prediction Page
if selected == "Parkinson Prediction":
    st.title("🩺Parkinson's Disease Prediction")

    with st.expander("Learn more about the input features"):
       st.write("""
       **Input Information:**
       - **MDVP:Fo(Hz)**: Average vocal fundamental frequency.
       - **MDVP:Fhi(Hz)**: Maximum vocal fundamental frequency.
       - **MDVP:Flo(Hz)**: Minimum vocal fundamental frequency.
       - **MDVP:Jitter(%)**: Variation in fundamental frequency.
       - **MDVP:Jitter(Abs)**: Variation in fundamental frequency (in absolute value).
       - **MDVP:RAP**: Variation in fundamental frequency.
       - **MDVP:PPQ**: Variation in fundamental frequency.
       - **Jitter:DDP**: Variation in fundamental frequency.
       - **MDVP:Shimmer**: Variation in amplitude.
       - **MDVP:Shimmer(dB)**: Variation in amplitude.
       - **Shimmer:APQ3**: Variation in amplitude.
       - **Shimmer:APQ5**: Variation in amplitude.
       - **MDVP:APQ**: Variation in amplitude.
       - **Shimmer:DDA**: Variation in amplitude.
       - **NHR**: Ratio of noise to tonal components in the voice.
       - **HNR**: Ratio of noise to tonal components in the voice.
       - **RPDE**: Nonlinear dynamical complexity measure.
       - **DFA**: Signal fractal scaling exponent.
       - **spread1**: Nonlinear measure of fundamental frequency variation.
       - **spread2**: Nonlinear measure of fundamental frequency variation.
       - **D2**: Nonlinear measure of fundamental frequency variation.
       - **PPE**: Nonlinear measure of fundamental frequency variation.
       """)

    bulk_input = st.text_area("Paste all inputs here (space-separated values):", "")
    if bulk_input:
        inputs = auto_fill_inputs(bulk_input, 22)
    else:
        inputs = [""] * 22

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', inputs[0])

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', inputs[1])

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', inputs[2])

    with col1:
        jitter_percent = st.text_input('MDVP:Jitter(%)', inputs[3])

    with col2:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)', inputs[4])

    with col3:
        rap = st.text_input('MDVP:RAP', inputs[5])

    with col1:
        ppq = st.text_input('MDVP:PPQ', inputs[6])

    with col2:
        ddp = st.text_input('Jitter:DDP', inputs[7])

    with col3:
        shimmer = st.text_input('MDVP:Shimmer', inputs[8])

    with col1:
        shimmer_db = st.text_input('MDVP:Shimmer(dB)', inputs[9])

    with col2:
        apq3 = st.text_input('Shimmer:APQ3', inputs[10])

    with col3:
        apq5 = st.text_input('Shimmer:APQ5', inputs[11])

    with col1:
        apq = st.text_input('MDVP:APQ', inputs[12])

    with col2:
        dda = st.text_input('Shimmer:DDA', inputs[13])

    with col3:
        nhr = st.text_input('NHR', inputs[14])

    with col1:
        hnr = st.text_input('HNR', inputs[15])

    with col2:
        rpde = st.text_input('RPDE', inputs[16])

    with col3:
        dfa = st.text_input('DFA', inputs[17])

    with col1:
        spread1 = st.text_input('spread1', inputs[18])

    with col2:
        spread2 = st.text_input('spread2', inputs[19])

    with col3:
        d2 = st.text_input('D2', inputs[20])

    with col1:
        ppe = st.text_input('PPE', inputs[21])

    # Code for Prediction
    if st.button("Parkinson's Test Result"):
        try:
            user_input = [fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]
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
    
    st.title('🧬Breast Cancer Prediction')
    
    with st.expander("Learn more about the input features"):
        st.write("""
        **Input Information:**
        - **Radius Mean**: Mean of distances from center to points on the perimeter.
        - **Texture Mean**: Standard deviation of gray-scale values.
        - **Perimeter Mean**: Mean size of the core tumor.
        - **Area Mean**: Mean area of the tumor.
        - **Smoothness Mean**: Mean of local variation in radius lengths.
        - **Compactness Mean**: Mean of perimeter^2 / area - 1.0.
        - **Concavity Mean**: Mean of severity of concave portions of the contour.
        - **Concave Points Mean**: Mean of number of concave portions of the contour.
        - **Symmetry Mean**: Mean symmetry.
        - **Fractal Dimension Mean**: Mean for "coastline approximation" - 1.
        - **Radius SE**: Standard error of distances from center to points on the perimeter.
        - **Texture SE**: Standard error of gray-scale values.
        - **Perimeter SE**: Standard error of the core tumor perimeter.
        - **Area SE**: Standard error of the tumor area.
        - **Smoothness SE**: Standard error of local variation in radius lengths.
        - **Compactness SE**: Standard error of perimeter^2 / area - 1.0.
        - **Concavity SE**: Standard error of severity of concave portions of the contour.
        - **Concave Points SE**: Standard error of number of concave portions of the contour.
        - **Symmetry SE**: Standard error of symmetry.
        - **Fractal Dimension SE**: Standard error for "coastline approximation" - 1.
        - **Radius Worst**: "Worst" or largest mean value for radius.
        - **Texture Worst**: "Worst" or largest mean value for texture.
        - **Perimeter Worst**: "Worst" or largest mean value for perimeter.
        - **Area Worst**: "Worst" or largest mean value for area.
        - **Smoothness Worst**: "Worst" or largest mean value for smoothness.
        - **Compactness Worst**: "Worst" or largest mean value for compactness.
        - **Concavity Worst**: "Worst" or largest mean value for concavity.
        - **Concave Points Worst**: "Worst" or largest mean value for concave points.
        - **Symmetry Worst**: "Worst" or largest mean value for symmetry.
        - **Fractal Dimension Worst**: "Worst" or largest mean value for fractal dimension.
        """)

    bulk_input = st.text_area("Paste all inputs here (space-separated values):", "")
    if bulk_input:
        inputs = auto_fill_inputs(bulk_input, 30)
    else:
        inputs = [""] * 30

    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean = st.text_input('Radius Mean', inputs[0])
        texture_mean = st.text_input('Texture Mean', inputs[1])
        perimeter_mean = st.text_input('Perimeter Mean', inputs[2])
        area_mean = st.text_input('Area Mean', inputs[3])
        smoothness_mean = st.text_input('Smoothness Mean', inputs[4])
        compactness_mean = st.text_input('Compactness Mean', inputs[5])
        concavity_mean = st.text_input('Concavity Mean', inputs[6])
        concave_points_mean = st.text_input('Concave Points Mean', inputs[7])
        symmetry_mean = st.text_input('Symmetry Mean', inputs[8])
        fractal_dimension_mean = st.text_input('Fractal Dimension Mean', inputs[9])

    with col2:
        radius_se = st.text_input('Radius SE', inputs[10])
        texture_se = st.text_input('Texture SE', inputs[11])
        perimeter_se = st.text_input('Perimeter SE', inputs[12])
        area_se = st.text_input('Area SE', inputs[13])
        smoothness_se = st.text_input('Smoothness SE', inputs[14])
        compactness_se = st.text_input('Compactness SE', inputs[15])
        concavity_se = st.text_input('Concavity SE', inputs[16])
        concave_points_se = st.text_input('Concave Points SE', inputs[17])
        symmetry_se = st.text_input('Symmetry SE', inputs[18])
        fractal_dimension_se = st.text_input('Fractal Dimension SE', inputs[19])

    with col3:
        radius_worst = st.text_input('Radius Worst', inputs[20])
        texture_worst = st.text_input('Texture Worst', inputs[21])
        perimeter_worst = st.text_input('Perimeter Worst', inputs[22])
        area_worst = st.text_input('Area Worst', inputs[23])
        smoothness_worst = st.text_input('Smoothness Worst', inputs[24])
        compactness_worst = st.text_input('Compactness Worst', inputs[25])
        concavity_worst = st.text_input('Concavity Worst', inputs[26])
        concave_points_worst = st.text_input('Concave Points Worst', inputs[27])
        symmetry_worst = st.text_input('Symmetry Worst', inputs[28])
        fractal_dimension_worst = st.text_input('Fractal Dimension Worst', inputs[29])

    # Code for Prediction
    if st.button('Breast Cancer Test Result'):
        try:
            user_input = [
                radius_mean, texture_mean, perimeter_mean, area_mean,
                smoothness_mean, compactness_mean, concavity_mean,
                concave_points_mean, symmetry_mean, fractal_dimension_mean,
                radius_se, texture_se, perimeter_se, area_se,
                smoothness_se, compactness_se, concavity_se,
                concave_points_se, symmetry_se, fractal_dimension_se,
                radius_worst, texture_worst, perimeter_worst, area_worst,
                smoothness_worst, compactness_worst, concavity_worst,
                concave_points_worst, symmetry_worst, fractal_dimension_worst
            ]
            user_input = [float(x) for x in user_input]

            cancer_prediction = breast_cancer_model.predict([user_input])

            if cancer_prediction[0] == 1:
                display_result('The tumor is malignant', True)
            else:
                display_result('The tumor is benign', False)
        except Exception as e:
            st.error(f"Error in Breast Cancer Prediction: {e}")


          

