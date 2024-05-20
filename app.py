import streamlit as st
import pickle
import pandas as pd
import requests

@st.cache
def load_pickle_file(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we got a successful response
    return pickle.loads(response.content)

# Replace these URLs with the actual URLs of your files in the cloud storage
cos_sim_url = "https://ml-model-cos-sim.s3.ap-southeast-2.amazonaws.com/cos_sim.pkl"
songs_dic_url = "https://ml-model-cos-sim.s3.ap-southeast-2.amazonaws.com/songs_dic.pkl"

cos_sim = load_pickle_file(cos_sim_url)
songs_dic = load_pickle_file(songs_dic_url)
song_df = pd.DataFrame(songs_dic)

def recommended(song_name):
    song_index = song_df[song_df['song_name'] == song_name].index[0]
    distances = cos_sim[song_index]
    song_top_20_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:21]

    recommended_songs = []
    for i in song_top_20_list:
        recommended_songs.append(song_df.iloc[i[0]].song_name)
    return recommended_songs

st.title('Spotify Song Recommender')

select_song_name = st.selectbox(
    "What would you like to hear?",
    song_df['song_name'].values)

if st.button('Recommend'):
    recommendations = recommended(select_song_name)
    for i in recommendations:
        st.write(i)