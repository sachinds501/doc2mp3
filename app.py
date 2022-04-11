from io import StringIO

import streamlit as st
import pyttsx3
import PyPDF2

st.header("PDF to Audio")

uploaded_file = st.file_uploader("Choose a file", type=['pdf'])
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    if st.button('Listen and Download'):

        # Read the PDF file binary mode
        # pdf_file = open("C:/Users/SACHIN/Downloads/Yolo.pdf", 'rb')
        read_pdf = PyPDF2.PdfFileReader(uploaded_file, strict=False)
        # Find the number of pages in the PDF document
        number_of_pages = read_pdf.getNumPages()
        # init function to get an engine instance for the speech synthesis
        engine = pyttsx3.init()

        for i in range(0, number_of_pages):
            # Read the PDF page
            page = read_pdf.getPage(i)

            # Extract the text of the PDF page
            page_content = page.extractText()
            # set the audio speed and volume
            cleaned_text = page_content.strip().replace('\n', ' ')
            print(cleaned_text)

            # say method on the engine that passing input text to be spoken
            engine.say(cleaned_text)
            st.write(cleaned_text)
            engine.save_to_file(cleaned_text, 'download.mp3')
            # run and wait method to processes the voice commands.
            engine.runAndWait()
