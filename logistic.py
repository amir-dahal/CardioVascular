import streamlit as st
import requests


feature, target, scaler, model, Y_pred, cr, cm = cardioPredict()
API_URL = 'http://127.0.0.1:8000/predict-cardio'


st.header('Logistic')

st.header('Catdiovascular Disease Prediction')
st.subheader('Using Logistic Regression')

st.sidebar.title(
    'Cardio Features'
)
age = st.sidebar.slider(
    'Age',
    max_value = 70,
    min_value = 26,
    value = 35,
    step=1
)

gender_dict = {1: 'Female', 2: 'Male'}
gender = st.sidebar.radio(
    'Gender',
    options = list(gender_dict.keys()),
    format_func = lambda x : gender_dict.get(x)
)

# height -> 150 - 200
# weight -> 45 - 120
# ap_hi -> 100 - 200
# ap_lo -> 50 - 90

height = st.sidebar.slider(
    'Height',
    max_value = 200.0,
    min_value = 150.0,
    value = 160.0,
    step=0.011
)

weight = st.sidebar.slider(
    'Weight',
    max_value = 120,
    min_value = 45,
    value = 50,
    step=1
)

ap_hi = st.sidebar.slider(
    'Systolic Pressure',
    max_value = 200,
    min_value = 100,
    value = 120,
    step=1
)

ap_lo  = st.sidebar.slider(
    'Disystolic Pressure',
    max_value = 90,
    min_value = 50,
    value = 80,
    step=1
)

cholestrol_dict = {1: 'Low Cholestrol', 2: 'Mild Cholestrol', 3: 'High Cholestrol'}
cholesterol = st.sidebar.radio(
    'Cholesterol',
    options = list(cholestrol_dict.keys()),
    format_func = lambda x : cholestrol_dict.get(x)
)

glucose_dict = {1: 'Low Glucose', 2: 'Mild Glucose', 3: 'High Glucose'}
gluc = st.sidebar.radio(
    'Glucose',
    options = list(glucose_dict.keys()),
    format_func = lambda x : glucose_dict.get(x)
)

smoke_dict = {0: 'Doesnot Smoke', 1: 'Does Smoke'}
smoke = st.sidebar.radio(
    'Smoke',
    options = list(smoke_dict.keys()),
    format_func = lambda x : smoke_dict.get(x)
)

alcohol_dict = {0: 'Doesnot drink', 1: 'Does drink'}
alco = st.sidebar.radio(
    'Alcohol',
    options = list(alcohol_dict.keys()),
    format_func = lambda x : alcohol_dict.get(x)
)

active_dict = {0: 'Doesnot do PA', 1: 'Does do PA'}
active = st.sidebar.radio(
    'Physical Activities',
    options = list(active_dict.keys()),
    format_func = lambda x : active_dict.get(x)
)
if st.button('Predict'):
    payload = {
        'age': age,
        'gender': gender,
        'height': height,
        'weight': weight,
        'ap_hi': ap_hi,
        'ap_lo': ap_lo,
        'cholesterol': cholesterol,
        'gluc': gluc,
        'smoke': smoke,
        'alco': alco,
        'active': active
    }
 
    try:
        response = requests.post(API_URL, json=payload)
       
        if response.status_code == 200:
            result = response.json()
           
            if result['Prediction_Status'] == 0:
                st.write('No disease found.')
                st.success('No Cardiovascular Disease🫡.')
            else:
                st.write('Disease Found.')
                st.warning('Cardiovascular Disease😭.')
        else:
            st.error(f'API Status Error: {response.status_code}')
    except requests.exceptions.RequestException:
        st.error(f'API Server Error: {response.status_code}')

# if st.button('Predict'):
#     data = pd.DataFrame([[
#        ' age' :, gender, height, weight, ap_hi, ap_lo, cholesterol,
#         gluc, smoke, alco, active
#     ]], columns=feature)
    
#     data_scale = scaler.transform(data)
#     prediction = model.predict(data_scale)
    
#     if prediction[0] == 0:
#         st.write('No disease found.')
#         st.success('No Cardiovascular Disease🫡.')
#     else:
#         if prediction[0] == 0:
#         st.write('No disease found.')
#         st.success('No Cardiovascular Disease🫡.')
        
#     # Visualization
# st.subheader('Visualization')
    
# fig, ax = plt.subplots(figsize = (6,4))
# sns.heatmap(cm, annot= True, fmt = '.0f', xticklabels = ['Predicted Healthy [0]', 'Predicted Unhealthy[1]'],
#            yticklabels = ['Actual Healthy [0]','Actual Unhealthy [1]'])
# plt.title('Actual Cardio vs. Predicted Cardio')
# st.pyplot(fig)
    
# report = pd.DataFrame(cr).transpose()
# st.dataframe(data.style.format(precision = 2))