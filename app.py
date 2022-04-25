import datetime
from numpy import datetime_as_string
import streamlit as st
import pandas as pd

st.title("Attendance")
#save_data = st.button("Save File")
df = pd.read_csv("data/names.csv")
st.header("Existing File")
st.write(df)

st.sidebar.header("Options")
options_form = st.sidebar.form("options_form")
user_name = options_form.text_input("Name")
roll_no = options_form.slider("Roll_no", 0, 130, 25)
subject = options_form.radio("Subject", ('CCL', 'SPCC', 'AI'))
time = options_form.time_input('Time', datetime.time(8, 45))
add_data = options_form.form_submit_button()
if add_data:
#    st.write(user_name, roll_no, subject, time)
    new_data = {"Name": user_name, "Roll No.": int(roll_no), "Subject": subject, "Time": str(time)}
    df = df.append(new_data, ignore_index=True)
    df.to_csv("data/names.csv", index=False)

def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='attendance.csv',
     mime='text/csv',
 )