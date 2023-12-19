import streamlit as st
from PIL import Image
import pickle


model = pickle.load(open('C:/Users/S3EED/Downloads/Pro/ML_Model1.pkl', 'rb'))

def run():
    img1 = Image.open('C:/Users/S3EED/Downloads/Pro/extras/utas.png')
    st.title("Bank Loan Eligibility using Machine Learning")

    ## Account No
    account_no = st.text_input('Account number')

    ## Full Name
    fn = st.text_input('Full Name')

    ## For gender
    gen_display = ('Female','Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    DAYS_BIRTH = st.number_input("Days of birth",value=0)

    DAYS_ID_PUBLISH = st.number_input("Days of publish",value=0)

    DAYS_REGISTRATION = st.number_input("How many dayes you have been with us?",value=0)
    
    CNT_CHILDREN = st.number_input("Num of Children",value=0)
    
    CNT_FAM_MEMBERS = st.number_input("Num of Family members",value=0)
    
    DAYS_LAST_PHONE_CHANGE = st.number_input("last time you changed the phone number",value=0)
    
    AMT_CREDIT = st.number_input("Credit",value=0)
    
    DAYS_EMPLOYED = st.number_input("how many days you have been emploied",value=0)

    AMT_INCOME_TOTAL = st.number_input("yearly income",value=0)

    dur_display = ['2 Month','6 Month','8 Month','1 Year','16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])
     
   
    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[DAYS_BIRTH, DAYS_ID_PUBLISH, DAYS_REGISTRATION, CNT_CHILDREN, CNT_FAM_MEMBERS, DAYS_LAST_PHONE_CHANGE, AMT_CREDIT, DAYS_EMPLOYED, AMT_INCOME_TOTAL]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'According to our Calculations, you will not get the loan from Bank'
            )
        else:
            st.success(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'Congratulations!! you will get the loan from Bank'
            )

run()
