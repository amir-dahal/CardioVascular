# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# import joblib

# MODEL_PATH = 'models/cardio_logistic_model.pkl'
# SCALER_PATH = 'models/cardio_logistic_scaler.pkl'
# df= pd.read_csv('data/Cardiovascular_Disease.csv')
# data = df[df.duplicated()]
# df['age']= df['age']//365

# data = df[
#     (df['height'].between(150,200))&
#     (df['weight'].between(45,120))& 
#     (df['ap_hi'].between(100,200))&
#     (df['ap_lo'].between(50,90))]

# data= data.drop(columns= 'id')
# def cardioPredict():
#     feature = ['age','gender','height','weight','ap_hi', 'ap_lo','cholesterol','gluc','smoke','alco','active']
#     target = 'cardio'
    
#     X = data[feature]
#     Y = data[target]

#     X_train, X_test, Y_train,Y_test = train_test_split(
#         X ,Y,test_size = 0.2, random_state = 42, stratify = Y
#     )

#     scaler = StandardScaler()
#     X_train_scale = scaler.fit_transform(X_train)
#     X_test_scale = scaler.transform(X_test)

#     model = LogisticRegression(solver = 'liblinear', class_weight = 'balanced', random_state = 42)

#     model.fit(X_train_scale, Y_train)
    
    
#     joblib.dump(model, MODEL_PATH)
#     joblib.dump(scaler, SCALER_PATH)

#     return scaler, model

import joblib

MODEL_PATH = 'models/cardio_logistic_model.pkl'
SCALER_PATH = 'models/cardio_logistic_scaler.pkl'

def load_data():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    
    return model, scaler
