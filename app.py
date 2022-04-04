from io import StringIO

import streamlit as st
import pyttsx3
import PyPDF2

st.header("PDF to Audio")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    if st.button('Listen to your Pdf'):
        pdfreader = PyPDF2.PdfFileReader(uploaded_file)
        speaker = pyttsx3.init()

        for page_num in range(pdfreader.numPages):
            text = pdfreader.getPage(page_num).extractText()  ## extracting text from the PDF
            cleaned_text = text.strip().replace('\n', ' ')  ## Removes unnecessary spaces and break lines
            print(cleaned_text)  ## Print the text from PDF
            speaker.say(cleaned_text)        ## Let The Speaker Speak The Text
            speaker.save_to_file(cleaned_text, 'story.mp3')  ## Saving Text In a audio file 'story.mp3'
            speaker.runAndWait()
        speaker.stop()
