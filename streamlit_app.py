import streamlit as st
import os 
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyA7_v1IJm4-MXBBj3CVSSl548xX-Znx264")

mode1 = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text, image_data, prompt):
    response = mode1.generate_content([input_text, image_data[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts =[ 
            {
                "mime_type" : uploaded_file.type,
                "data" : bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File was Uploaded")

st.set_page_config(page_title="Shaunak's Invoice Gen")
st.sidebar.header("Robobill")
st.sidebar.write("Made by Shaunak")
st.sidebar.write("Powered by Google Gemini AI")
st.header("RoboBILL")
st.subheader("Manage Your Expenses")
input = st.text_input("What do you want me to do?",key="input")
uploaded_file = st.file_uploader("Choose an image", type = ["jpg","jpeg","png"])
image =""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)
ssubmit = st.button("Lets Go")

input_prompt = """
You are an expert in reading invoices.We are going to upload an image of an invoice and you will make a proper tabular "list" and emojis for each item for the same list out the item 
names and display its prices in the same font in a proper list and print the time and add the total amount and display
the total amount and add a tag "RoboBill" in the end. and ask the user to use it again and if it was helpful?
make it a proper list in different lines and add emojis 

"""
if ssubmit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's what u need to know")
    st.write(response)
    
