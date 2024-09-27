import streamlit as st
import pandas as pd
import numpy as np


# Title
st.title("Diljit Dosanjh Concert Tickets")


# Description
st.write("Book your tickets for Diljit Dosanjh's DIL-LUMINATI TOUR! Choose your preferred event and fill out the form below:")


concerts = [
    ("Sep 28, 6:30 PM - Manchester, GB - Co-op Live", "Manchester"),
    ("Oct 2, 6:30 PM - Dublin, IE - 3Arena", "Dublin"),
    ("Oct 4, 6:30 PM - London, GB - The O2", "London"),
    ("Oct 5, 6:30 PM - London, GB - The O2", "London"),
    ("Oct 9, 8:00 PM - Düsseldorf, DE - PSD Bank Dome", "Düsseldorf"),
    ("Oct 11, 8:00 PM - Amsterdam, NL - Ziggo Dome", "Amsterdam"),
    ("Oct 26, 7:00 PM - New Delhi, India - Jawaharlal Nehru Stadium", "New Delhi"),
    ("Nov 9, 6:30 PM - Abu Dhabi, UAE - Etihad Park", "Abu Dhabi"),
    ("Nov 15, 7:00 PM - Hyderabad, India - Hyderabad Home", "Hyderabad"),
    ("Nov 17, 7:00 PM - Ahmedabad, India - Ahmedabad Gujarat", "Ahmedabad"),
    ("Nov 22, 7:00 PM - Lucknow, India", "Lucknow"),
    ("Nov 24, 7:00 PM - Pune, India", "Pune"),
    ("Nov 30, 7:00 PM - Kolkata, India", "Kolkata"),
    ("Dec 6, 7:00 PM - Bengaluru, India", "Bengaluru"),
    ("Dec 8, 7:00 PM - Indore, India", "Indore"),
    ("Dec 14, 7:00 PM - Chandigarh, India", "Chandigarh"),
    ("Dec 29, 7:00 PM - Guwahati, India", "Guwahati")
]

# User Form for Booking
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")

# Event Selection using Slider
event_index = st.slider("Choose your event", 0, len(concerts) - 1)
selected_event = concerts[event_index]

# Show Selected Event
st.write(f"**You selected:** {selected_event[0]}")

st.header("ID PROOF UPLOAD (Aadhar Card, Passport, Driving License , Voter ID)")
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg", "csv"])

# Display uploaded file details or preview
if uploaded_file is not None:
    file_details = {
        "filename": uploaded_file.name,
        "filetype": uploaded_file.type,
        "filesize": uploaded_file.size
    }
    
    st.write("Uploaded file details:")
    st.write(file_details)
    
    # Handling different file types
    if uploaded_file.type == "application/pdf":
        st.write("PDF file uploaded!")
        st.download_button("Download the uploaded PDF", data=uploaded_file, file_name=uploaded_file.name)
    
    elif uploaded_file.type == "text/csv":
        st.write("CSV file uploaded!")
        csv_data = pd.read_csv(uploaded_file)
        st.write(csv_data)
    
    elif uploaded_file.type in ["image/png", "image/jpeg", "image/jpg"]:
        st.write("Image uploaded!")
        st.image(uploaded_file)

# Confirm Registration
if st.button("Confirm Booking"):
    if name and email and phone:
        st.success(f"Thank you {name}, your booking for {selected_event[0]} is confirmed!")
        st.info(f"We will contact you at {email} or {phone} for more details.")
    else:
        st.error("Please fill in all the required details.")
