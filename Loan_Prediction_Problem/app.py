import streamlit as st
import pandas as pd
import pickle as pk

model = pk.load(open('model.pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))

st.header('Loan Prediction Problem')

no_of_dep = st.slider('choose no of depenedents ',0,5)
grad = st.selectbox('choose graduation',['Graduated', ' Not Graduated'])
self_emp = st.selectbox('self employed',['Yes','No'])
annual_income = st.slider('Choose annual income ',0,10000000)
loan_amount = st.slider('Choose Loan Amount ',0,10000000)
loan_dur = st.slider('Choose Loan Duration ',0,20)
cibil = st.slider('Choose Cibil Score ',0,1000)
luxury_assets_value = st.slider('Choose ammount luxury_assets_value',0,10000000)
bank_asset_value = st.slider('Choose ammount bank_asset_value',0,10000000)
assets = st.slider('Choose the assets ',0,10000000)


if grad =='graduate':
    grad_s = 1
else:
    grad_s = 0

if self_emp=='No':
    emp_s = 0
else:
    emp_s = 1

if st.button("Predict"):
    pred_data = pd.DataFrame([[no_of_dep,grad_s,emp_s,annual_income,loan_amount,loan_dur,cibil,luxury_assets_value,bank_asset_value,assets]],
                             columns=['no_of_dependents',	'education',	'self_employed',	'income_annum',	'loan_amount',	'loan_term',	'cibil_score','luxury_assets_value','bank_asset_value',	'assets' ])
    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)
    if predict[0] == 1:
        st.markdown('Loan Is Approved')
    else:
        st.markdown('Loan Is Not Approved')


