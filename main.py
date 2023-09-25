"""
    Streamlit Financial Calculator.
    Description: This file is used to launch a minimal streamlit web 
	application. A financial calculator that estimates the monthly installment that will be paid 
    for covering a personal loan.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/
 
 Author: Sudhanshu Kumar

"""

#Streamlit depends 
import streamlit as st #  pip install streamlit
from calculator import monthly_installment
import base64 #pip install base64

#SEO configuration
st.set_page_config (page_title = 'Fincial Calculator:  Monthly Installment Estimation ',
                    page_icon ='', 
                    layout ='centered'
)

# modify app display
hide_menu = """
<style>
#MainMenu {
    visibility: hidden;
    }

footer {
    visibility: visible;
}
footer:before{
    content:'© All rights reserved 2023-24 Developed with ❤ by Sudhanshu Kumar';
    display:block;
    position:relative;
    color:#D33639;
}
<style>
"""

def main ():
    st.markdown(hide_menu,unsafe_allow_html=True)
    st.title("Financial Calculator")
    
    #using strimlit form to collect data from user
    with st.form('data_form', clear_on_submit=False):
        principal = st.number_input('ENTER LOAN AMOUNT R')
        period = st.slider('LOAN TERM IN YEARS',1,20)
        interest_rate = st.slider('VARIABLE INTEREST RATE %', 7.75, 0.25, 25.75)

        if st.form_submit_button('Calculate Monthly Installment'):
            st.write('Your Monthly Installment for the loan of ₹ '+str(principal)+ 'is ₹ ' +str(monthly_installment(principal,period,interest_rate)))
    

if __name__ =='__main__':
    main()
