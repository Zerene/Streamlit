import streamlit as st
import numpy as np

st.image("https://wallpaperaccess.com/full/1704555.jpg", caption="", use_column_width=True)
st.title('Hypothesis Tester')

control_visitors = st.number_input("Enter the number of visitors in the control group: ",step=1,value=1)
control_conversions = st.number_input("Enter the number of conversions in the control group: ",step=1)
treatment_visitors = st.number_input("Enter the number of visitors in the treatment group: ",step=1,value=1)
treatment_conversions = st.number_input("Enter the number of conversions in the treatment group: ",step=1)

control_rate = control_conversions / control_visitors
treatment_rate = treatment_conversions / treatment_visitors

pooled_se = np.sqrt((control_rate * (1 - control_rate) / control_visitors) + (treatment_rate * (1 - treatment_rate) / treatment_visitors))


z_score = (treatment_rate - control_rate) / pooled_se

confidence_level = st.radio('Choose the confidence level: ',
				('90', '95', '99'))


if( confidence_level == '90'):
    z_critical = 1.645
 
elif(confidence_level == '95'):
    z_critical = 1.96

else:
    z_critical = 2.576

    

if(st.button('Start Test')):
    if z_score > z_critical:
        st.success( "Experiment Group is Better")
    elif z_score < -z_critical:
        st.warning( "Control Group is Better")
    else:
        st.error("Indeterminate")

