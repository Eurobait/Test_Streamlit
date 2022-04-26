import streamlit as st
import pandas as pd


mold = st.number_input("Chance of mold", 0.01)
st.write("Chance of no mold", 1-mold)


high_sugar = st.number_input("Chance of High Sugar Level", 0.01)
common_sugar = st.number_input("Chance of Typical Sugar Level", 0.01)
st.write("Chance of No Sugar", 1-high_sugar - common_sugar)

harvest = 960000
storm_noharvest = 3300000*mold + 420000*(1-mold)
nostorm_noharvest = 1500000*high_sugar + 1410000*common_sugar + 960000*(1-high_sugar - common_sugar)


p_ns_dns = 0.02
p_s_ds = 0.99

p_ds = 0.984
p_dns = 0.016

e_dns_upper = harvest
e_dns_lower = p_ns_dns * nostorm_noharvest + (1-p_ns_dns)*storm_noharvest
e_dns = max(e_dns_lower, e_dns_upper)

e_ds_upper = harvest
e_ds_lower = p_s_ds*storm_noharvest + (1-p_s_ds)*nostorm_noharvest
e_ds = max(e_ds_lower, e_ds_upper)
result = p_dns*e_dns + p_ds*e_ds



st.write("Expected value of harvest $", harvest)
st.write("Expected value of using ML system $", result)


st.write("The final decision:")
if result > harvest:
    st.write("Proceed with ML system")
    st.write("Maximum of deployment: $", result - harvest)
else:
    st.write("Just Harvest")

st.write("Please note the model isn't perfect right now with sensitivity of 0.99 and specificity of 0.02")
st.write("Decision may not change will changing chance parameters")