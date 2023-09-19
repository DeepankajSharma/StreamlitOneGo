import streamlit as st
import pandas as pd
st.subheader("Loading the CSV file")
df=st.file_uploader("Upload the csv file:",type=["CSV","xlsx"])

#if df is not None:
#    st.dataframe(df)
df=pd.read_csv("Products.csv")
if df is not None:
    st.table(df.head())

st.subheader("Dealing with images")
st.image("/Users/HP/Atom IDE/Geeksforgeeks/img.png")

st.subheader("Dealing with images while uploading")
img1=st.file_uploader("Upload the image file: ", type=["png","jpeg"])
if img1 is not None:
    st.image(img1, caption="Uploaded Image")

st.subheader("Dealing with video uploading")
video_file=st.file_uploader("Upload the video file: ", type=["mkv","mp4"])

if video_file is not None:
    st.video(video_file,start_time=0)


st.subheader("Dealing with Audio uploading")
audio_file=st.file_uploader("Upload the audio file: ", type=["mp3","wav"])

if audio_file is not None:
    st.audio(audio_file.read())
