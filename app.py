# 'age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol',
#            'gluc', 'smoke', 'alco', 'active'

import streamlit as st
def Home():
    st.Page('app.py',title = "Home")
    st.header('Home')
    

pages = {
    "Home":[
        st.Page(Home)
    ],
    'Models':[
        st.Page('logistic.py', title = 'Logistic'),
        st.Page('svm.py', title = 'SVM')
    ]
}
pg = st.navigation(pages)
pg.run()


