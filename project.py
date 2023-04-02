
import streamlit as st
import pandas as pd 
import analysis as analysis

import datetime
# Define the pages of your app
page_names = ["Home", "About", "Test"]
submissions = []


# Add a dropdown menu to the sidebar for page navigation
st.sidebar.image('hacklogo.png')
page = st.sidebar.selectbox("Select a page", page_names)
with st.sidebar.expander("What is Force Flicker?", expanded = False):
    st.write("*Force Flicker* is a web app that helps users Physical therapy data and advanced data analysis to provide the treatment plan to use personalized to the patients improvement patterns.")
    
with st.sidebar.expander("How do I use this program?", expanded = False):
    st.write("1. use the hardware and enter patient data into the system")
    st.write("2. search the patients record to see their performance")
    st.write("3. Get your results!")
    st.write("")


with st.sidebar.expander("What are the meanings of the inputs?", expanded = False):
    st.write("`name`: patients first and last name")
    st.write("`Date of birth`: patient's DOB")
    st.write("`Date`: Date of test ")
    st.write("`Exercise type`: exercise patient perfomance prior to test")



# Show the appropriate page based on the user's menu choice
#home page 
if page == "Home":
    st.title("Welcome to the Home Page!")
    # Set a default date for the date selector
    default_date = datetime.date(2023, 4, 1)
    st.title(" what to you want to do today?")

    analyze = st.selectbox("task",['Pull patient data', ' exercise statistics'])
    if analyze == 'Pull patient data':
        st.write("Enter patients name")
        butt = st.button(label="search")
        name_sel = st.text_input("Name")
        if(butt):
            analysis.pull_patient_data(name_sel)  
        
# Pages 
elif page == "About":
    st.title("About Our tests and tools")
    st.write("What is out Project")
    st.write(" Force flick is a webapplication, and a hardware testing device built for testing finger mobility in physical therapy environments.\n In our website you can record patient data, and view various analysis on thero test performance.\n Some of the analytical points include: \n Performance improvement over time \n Effeciency score for exercises, \n a dynamic personalized exercise plan ")
# test page code  
else:
    df = pd.DataFrame(columns=['Name', 'DOB', 'TODAY','exercise type','test_number','test type','time_taken'])
    def add_to_df(name, dob_str, date_str, excersize, i, test_type,Time_taken):
        global df
        df= pd.read_csv("input.csv")
        df = df.append({'Name': name, 'DOB': dob_str, 'TODAY': date_str,'exercise type': excersize,'test_number':i,'test type': test_type, 'time_taken': Time_taken}, ignore_index=True)
    st.title("Set up your test")
    st.write("Enter name of the patient")
    name = st.text_input("Enter your name")
    st.write("Enter DOB of the patient")
    dob = st.date_input("Enter your date of birth")
    dob_str = dob.strftime('%m/%d/%Y')
    st.write("select todays date")
    date = st.date_input('date')
    date_str=date.strftime('%m/%d/%Y')
    num_test = st.select_slider('Pick number of tests today', [0, 1, 2,3,4,5,6,7,8,9,10])
    
    st.write("Today's exercise")
    excersize = st.selectbox('Exercise performed today',('no exercise', 'stress-ball squeez', 'joystick','pinching','scrolling'))

    st.write('You selected:', excersize)
    
    for i in range(num_test):
    # Add a dropdown box with the selected number as the label
        
        test_type = st.selectbox(f"test type for test {i+1}", [1,2,3,4,5])
        Time_taken = st.number_input(f"Enter an integer{i+1}")
        submit_button = st.button(label=f"submit test {i+1}")
        if(submit_button):
            add_to_df(name,dob_str,date_str,excersize,i,test_type,Time_taken)
            df.to_csv("input.csv",index=False)
            
    st.dataframe(df)