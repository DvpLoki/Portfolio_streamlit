import streamlit as st
from PIL import Image

st.set_page_config(page_title='loki-About',page_icon="🇱")

@st.cache_data
def getdata():
    pic=Image.open('profile-pic.png')
    data=open('Lokiresume.pdf','rb')
    res=data.read()

    return pic,res

pf,res=getdata()

l,r=st.columns(2)
l.image(pf,width=320)

r.title("I am ,")
r.title('Devarapu Lokesh')
r.subheader('Indian')
r.markdown("Email: dvploki@gmail.com")
r.markdown("[LinkedIn](https://www.linkedin.com/in/devarapu-lokesh-99057225a) |  [GitHub](https://github.com/DvpLoki)")
r.markdown("<style> a{text-decoration:none;}</style>",unsafe_allow_html=True)
r.download_button(data=res,file_name="loki_Resume.pdf",label="Download Resume")

st.markdown("#")
st.markdown("---")
st.subheader("About Me")
st.write("I am a  Btech CSE graduate with a passion in datascience. open to internships , entry level positions and projects that allow me to learn and grow.")
st.write("If you are looking for a motivated and dedicated team member , lets connect through Linkedin or mail , i am exicted to explore opportunities and contribute to the success of your organization. ")
with st.container():
    st.markdown("---")
    st.header("Education")
    st.subheader("BTech CSE")
    st.write("YSR Engineering college of yogi vemana university, kadapa ,AP")
    st.write("2019 - 2023 |   CGPA: 8.3/10.0")
    st.subheader("Intermediate MPC")
    st.write("Scholars college , Guntur , AP")
    st.write("2017 - 2019  |  CGPA: 9.8/10.0")


    





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

