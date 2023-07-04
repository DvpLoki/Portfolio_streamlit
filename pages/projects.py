import streamlit as st
from PIL import Image

st.set_page_config(page_title='loki-projects',page_icon="🇱")

st.title('Projects')
with st.container():
     st.markdown("---")
     st.subheader("Data Analysis")
     st.markdown('#')
     st.subheader("❖HR Analytics Dashboard (Power BI)")
     st.write(" Designed and developed an interactive dashboard to visualize HR analytics data using Power BI. Provided key insights to enhance employee satisfaction and retention.")
     st.markdown("[Github](https://github.com/DvpLoki/HR-Analytics-Dashboard-using-power-BI)")
     st.subheader("❖Interactive Sales and Inventory Dashboard for Vrinda Store (Excel)")
     st.write(" Designed and developed an interactive dashboard report using Excel.Provided data-driven insights for sales analysis and inventory management.")
     st.markdown("[Github](https://github.com/DvpLoki/Vrinda_store_analysis_using_Excel)")

with st.container():
     st.markdown("---")
     st.subheader("Machine Learning ")
     st.markdown("#")
     st.subheader("❖Car Price Prediction")
     st.write(" Developed a machine learning model to predict car prices based on various features. Achieved 96% accuracy using RandomForest Regressor. Deployed the project using Streamlit for an interactive user interface.")
     st.markdown("[Github](https://github.com/DvpLoki/OIBSIP/tree/main/Car%20Price%20Prediction)  |  [Demo](https://loki-car-price-prediction.streamlit.app/)")
    
with st.container():
     st.markdown("---")
     st.subheader("Cryptography")
     st.markdown("#")
     st.subheader("❖Modified AES by adding Addroundkey")
     st.write(" Developed a new implementation of the AES encryption algorithm in Python.  Improved the avalanche effect of the algorithm by adding addroundkey function between shiftrows and mixed columns operations.Achieved better results compared to the standard AES encryption algorithm. For better access it is deployed using streamit and PBKDF2 for key derivation to ensure maximum security.")
     st.markdown("[Github](https://github.com/DvpLoki/AES-File-Encryption-Decryption-App)  |  [Demo](https://aes-file-encrypt-decrypt.streamlit.app/)")
     st.subheader("❖Implemented DES algorithm in Python")
     st.write("A pure python implementation of Data Encryption standard (DES) , a widely used encryption algorithm")
     st.markdown("[Github](https://github.com/DvpLoki/DES-in-python)")

with st.container():
     st.markdown("---")
     st.subheader("Natural language processing (NLP)")
     st.markdown("#")
     st.subheader("❖Email Spam Detection")
     st.write("Built a spam detection system using machine learning algorithms. Preprocessed email data, extracted relevant features, and trained a classifier. Achieved high accuracy 97.8 % and precision of 0.99 using Linear SVM in classifying spam and non-spam emails. Deployed the project using Streamlit for easy access and usage.")
     st.markdown("[Github](https://github.com/DvpLoki/OIBSIP/tree/main/Email%20Spam%20detection%20with%20machine%20learning) | [Demo](https://loki-email-spam-classifier.streamlit.app/)")
     
with st.container():
     st.markdown("---")
     st.subheader("Deep Learning")
     st.markdown("#")
     st.subheader("❖Traffic sign classification using CNN and German traffic sign dataset")
     st.write("Developed a convolutional neural network (CNN) model to classify traffic signs using the German traffic sign dataset Achieved an accuracy of 95% on the test dataset")
     st.markdown("[Github](https://github.com/DvpLoki/Traffic-sign-classification-using-CNN)")


st.markdown("<style> a{text-decoration:none;}</style>",unsafe_allow_html=True)
footer = """
    <style>
        .footer {
                position: fixed;
                
                left: 0;
                bottom: 0;
                width: 100%;
                background-color:black;
                padding: 10px;
                text-align: center;
                font-size: 14px;
                color:white;
            }
    </style>

    <div class="footer">
        <h4>Made with &#10084; by Devarapu Lokesh</h4>
    </div>
    """

st.write(footer, unsafe_allow_html=True)

hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            header {visibility:hidden;}
            </style>
            """
st.markdown(hide_st_style,unsafe_allow_html=True)

