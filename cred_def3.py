#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pickle

st.header("Credit Card Default checker")
st.subheader("Credit Limit:")
cre_lim=st.number_input("Credit Limit set by the bank")

st.subheader("Gender :")
gender=st.selectbox("Select the gender",["Male","Female"])
if gender is not None:
  if gender=="Male":
    gender_int=1
  
  elif gender=="Female":
    gender_int=2
    
st.subheader("Education :")
edu=st.selectbox("Educational Qualification",["Graduate School","University","High School","Others"])
if edu is not None:
    if edu=="Graduate School":
        edu_int=1
    elif edu=="University":
        edu_int=2
    elif edu=="High School":
        edu_int=3
    elif edu=="Others":
        edu_int=4
        
st.subheader("Married :")
Married=st.selectbox("Married or not",["Yes","No","Others"])
if Married is not None:
  if Married=="Yes":
    marr_int=1
  
  elif Married=="No":
    marr_int=2
  else:
    marr_int=3

st.subheader("Age:")
aged=st.number_input("Age of the person")

st.subheader("Pay status 1-3:")
pay_st1=st.number_input("Pay status for first 3 bills")

st.subheader("Pay status 3-6:")
pay_st2=st.number_input("Pay status for last 3 bills")

st.subheader("Bill Amount 1-3:")
bill_st1=st.number_input("Bill Amount for first 3 bills")

st.subheader("Bill Amount 3-6:")
bill_st2=st.number_input("Bill Amount for last 3 bills")

st.subheader("Paid Amount 1-3:")
paid_st1=st.number_input("Paid Amount for first 3 bills")

st.subheader("Paid Amount 3-6:")
paid_st2=st.number_input("Paid Amount for last 3 bills")


arr_avg=[167484.32266666667, 1.6037333333333332, 1.8422666666666667, 1.5554666666666668, 35.4855, 1.8947503333332274, 1.74085933333326, 49138.52029266713, 40815.37013233324, 5603.475154666639, 4946.9890503333245]
arr_std=[129747.66156719506, 0.4891291960904071, 0.7444944624525737, 0.5181367880008597, 9.217904068090183, 1.037238799157465, 1.0647640453617335, 69560.37980673157, 60084.4453398624, 13658.079160307629, 10747.778000305894]
liss=[cre_lim,gender_int,edu_int,marr_int,aged,pay_st1,pay_st2,bill_st1,bill_st2,paid_st1,paid_st2]

for i in range(len(liss)):
    if i not in [1,2,3]:
        liss[i]=(liss[i]-arr_avg[i])/arr_std[i]
    
    
    
grb=pickle.load(open("ada_cd.pkl","rb"))
result=["This person may pay the due on time","This person may not pay the due on time"]


if st.checkbox("Predict"):
   pred=grb.predict([liss])
   if pred==0:
     st.write(result[0])
     
   elif pred==1:
     st.write(result[1])
    
   
   

