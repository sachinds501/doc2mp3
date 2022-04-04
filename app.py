import streamlit as st
import pandas as pd

st.header("PDF to Audio")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    # data = bytes_data.decode("utf-8")

    if st.button('Listen to your Pdf'):
        import pyttsx3
        import PyPDF2

        # Read the PDF file binary mode
        pdf_file = open('C:/Users/SACHIN/Downloads/13.pdf', 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
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
            newrate = 200
            engine.setProperty('rate', newrate)
            newvolume = 200
            engine.setProperty('volume', newvolume)

            # say method on the engine that passing input text to be spoken
            engine.say(page_content)

            # run and wait method to processes the voice commands.
            engine.runAndWait()
