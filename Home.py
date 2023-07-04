import streamlit as st
from PIL import Image

st.set_page_config(page_title='Portfolio Website',page_icon="🇱")

@st.cache_data
def getdata():
    pic=Image.open('profile-pic.png')
    data=open('Lokiresume.pdf','rb')
    res=data.read()

    return pic,res

pf,res=getdata()
l,r=st.columns(2)
l.image(pf,width=320)
r.title("Welcome to my Portfolio")
r.title('Devarapu Lokesh')
r.subheader('Fresher')
r.markdown("✉Email: dvploki@gmail.com")
r.markdown("[LinkedIn](https://www.linkedin.com/in/devarapu-lokesh-99057225a) |  [GitHub](https://github.com/DvpLoki)")
r.markdown("<style> a{text-decoration:none;}</style>",unsafe_allow_html=True)
r.download_button(data=res,file_name="loki_Resume.pdf",label="Download Resume")
with st.container():
     st.markdown('#')
     st.subheader('Looking for challenging opportunities !!')
     st.subheader(' As a fresher I am eager to learn and develope my skills to contribute to the sucess of the organization')

with st.container():
     st.markdown("---")
     st.subheader('Areas of Interests:')
     b1,b2,b3=st.columns(3)
     b1.header('Data Analysis')
     b2.header('Machine Learning')
     b3.header('python Developer')
    
    
with st.container():
     st.markdown("---")
     st.header("Skills")
     st.subheader("Programming Languages:")
     b1,b2,b3=st.columns(3)
     b1.write("Python")
     b2.write("C")
     b3.write("Java")
     st.subheader("Data Analysis & visulaization:")
     d1,d2,d3,d4=st.columns(4)
     d1.write("Pandas")
     d2.write("Numpy")
     d3.write("EDA")
     d4.write("statistics")
     d5,d6,d7,d8=st.columns(4)
     d5.write("Power BI")
     d6.write("matplotlib")
     d7.write("seaborn")
     d8.write("Plotly-Express")
     st.subheader('Machine Learning')
     m1,m2,m3=st.columns(3)
     m1.write("Scikit-Learn")
     m2.write("TensorFlow")
     m3.write("keras")
     st.subheader("Natural Language Processing (NLP)")
     n1,n2=st.columns(2)
     n1.write("NLTK")
     n2.write("WordCloud")
     st.subheader("Web Developement")
     w1,w2,w3=st.columns(3)
     w1.write("HTML")
     w2.write("CSS")
     w3.write("JavaScript")
     w4,w5,w6=st.columns(3)
     w4.write("Php")
     w5.write("Flask")
     w6.write("Streamlit")

     st.subheader("Databases")
     d1,d2=st.columns(2)
     d1.write("MySQL")
     d2.write("MongoDB")

     st.subheader("Tools")
     t1,t2,t3=st.columns(3)
     t1.write("Micorsoft - word, powerpoint, Excel")
     t2.write("Github")
     t3.write("VSCode")

     st.subheader("Operating System")
     o1,o2=st.columns(2)
     o1.write("Windows")
     o2.write("Linux/Unix")

     st.markdown("---")


keyskill={
     
     '✓ Data Analysis':' Proficient in utilizing Python libraries such as Pandas and NumPy for data manipulation, analysis, and cleaning.',
     '✓ Data Visualization':' Skilled in creating visualizations using tools like Matplotlib, Seaborn, and Plotly-Express, Power BI to communicate data-driven insights effectively.',
     '✓ Machine Learning':' Experience in developing machine learning models for classification and prediction tasks.',
     '✓ Web Development':' Proficient in web development technologies such as HTML, CSS, JavaScript, Python Flask and Streamlit for building interactive web applications.',
     '✓ Database Management':' Knowledge of databases like MySQL and MongoDB for storing, retrieving, and managing data efficiently.',
     '✓ Version Control': 'Familiar with Git for collaborative development and version control of projects.',
    '✓ Problem Solving':' Strong problem-solving abilities with a focus on finding innovative and efficient solutions' 
}

with st.container():
     st.header('What I can Do:')
     for key,item in keyskill.items():
          st.subheader(f"{key}")
          st.write(f"{item}")


    






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

