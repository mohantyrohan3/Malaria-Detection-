import streamlit as st
import numpy as np
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
import tensorflow as tf
from tensorflow import keras





#### Loading Model
model = keras.models.load_model('models/{1}')




#### Predicting 
def predict(img,model):
    image = tf.keras.preprocessing.image.load_img(img)
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    predictions = model.predict(input_arr)
    if predictions[0]>0.5:
        return 1
    else:
        return 0





### Loading Lottie Animation
def load_lottieurl(url):
     r = requests.get(url)
     if r.status_code != 200:
         return None
     return r.json()

lottie_coding=load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_lX3vm6.json")



#### Introdcution Section 

with st.container():
    components.html(""" 
    <div >
        <h1 style="text-align:center;color:white;font-family:monospace;font-size:50px;">
        Malaria Detection
        </h1>
    </div
    """)

    left_column,right_column=st.columns([3,2])
    with left_column:
        
        st.subheader("What is Malaria ?")
        st.write(""" 
            Malaria is a disease caused by a parasite. The parasite is spread to humans through the bites of infected mosquitoes. People who have malaria usually feel very sick with a high fever and shaking chills
        """)
        st.subheader("How is Prediction helps?")
        st.write(""" 
                User can save humans by detecting and deploying Image Cells that contain Malaria or not!
        """)

    with right_column:
        st_lottie(lottie_coding,height=300,key="air pollution")


st.write("---")


### Hiding Streamlit Watermarks
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)






### Middle Sub Section

st.subheader("Give a Image of Cell for Prediction")
file=st.file_uploader("Please Upload an Image ",type=['jpg','png'])
if file is None:
    st.text("Please upload an valid image file ")
else:
    ans=predict(file,model)
    image1 = tf.keras.preprocessing.image.load_img(file)
    st.image(image1,width=300)#use_column_width=True)
    if ans==0:
        st.success(" Oh ! This cell is Infected with Malaria ")
    else:
        st.success(" The cell is not Infected with Malaria ")









st.write("---")
# Showing Some Images of Parasitized and Uninfected 

with st.container():
    st.header("Difference between Infected and Uninfected")
    st.markdown("""   """)
    st.markdown("""   """)

    left_column,right_column=st.columns([1,1])
    with left_column:
        st.subheader("Uninfected")
        st.markdown("""   """)
        st.image("uninfected.png")
    
    with right_column:
        st.subheader("Parasitized")
        st.markdown("""   """)
        st.image("Parasitized.png")
        




st.write("---")


st.write("Credits")
st.markdown(""" Dataset taken from Kaggle : [Link Here](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria) """)
st.write("You can Download Here More Images for Checking")