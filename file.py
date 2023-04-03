import streamlit as st
import pickle
import pandas as pd
from PIL import Image
image = Image.open('L&T.png')
st.set_page_config(page_title="LLD",layout="wide", page_icon=image)
hide_menu_style="""
    <style>
    #MainMenu {visibility: hidden;}
    footer { visibility : hidden;}
    </style>
    """
st.markdown(hide_menu_style,unsafe_allow_html=True)



def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
def user_input_features():

    mat = st.selectbox('Material of Construction of Lug?',  ("SA 516 GR. 70",))
    Ys= st.number_input('Yield Strength at Room Temperature( kg/mm² )')
    N = st.number_input('Number Of Lugs',value=1,step=1)
    Lb =st.number_input('Length Of Bottom Of Lug ( mm )')
    Lc= st.number_input('Length Of Lug at Centerline of Hole ( mm )')
    t = st.number_input('Thickness of Lug( mm )')
    L= st.number_input('Distance of centerline of Hole from bottom of Lug( mm )')
    dh =st.number_input('Diameter of Hole of Lug( mm )')
    lf =st.number_input('Length of Weld Leg( mm )')
    E= st.number_input('Weld Efficiency')
    W =st.number_input('Weight on a Dishend ( Kg )')
    IP =st.number_input('Impact factor')
output = user_input_features()
