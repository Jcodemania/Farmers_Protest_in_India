import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import re
import streamlit as st
from PIL import Image

#Twitter API Credentials
consumer_key="D8fYcWlanXo3Bymvzz3eozqSt"
consumer_secret="JAQAMThv6kUguYCXpOZyKqmMSduBtEuCfR0rTcPSzakcQDAjXW"
access_token="1205110377513545728-ZMu0EpeB34ZJvTrfAKjp2DrRQBBq7O"
access_token_secret="BIz4g4yVy10lhySPAzFHIWiqR4dAXrcH5Ex1xDlCCSzmQ"
#API Credentials are subject to security issues and cannot be shown

#Create the Authentication Object
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)

#Set the access token and access token secret
auth.set_access_token(access_token,access_token_secret)

#Create the API Object while passing the Auth information
api=tweepy.API(auth)

#Using Streamlit for Visualization
page=st.sidebar.selectbox("Choose a page", ["Bar Graph","Line Graph","WordCloud"])
st.write("""
  # Sentiment Analysis on Tweets of the People of India on Farmers Protest...
  Analyse the sentiments of the people of India!
  """)
image=Image.open('fb.jpg')
image_style = {'width': '50px', 'height':'30px'}
st.image(image)

#Extract the tweets from the twitter user
results=api.search(q="#FarmersProtest", lang="en", result_type="recent",  count=1000)

#Create dataframe with column named Tweets
df=pd.DataFrame([tweet.text for tweet in results], columns=['Tweets'])
#Creating function to clean tweets
def cleanTxt(text):
    text=re.sub(r'@[A-Za-z0-9]+','',text)
    text=re.sub(r'#','',text)
    text=re.sub(r'RT[\s]+','',text)
    text=re.sub(r'https?:\/\/\S+','',text)
    text=re.sub(r':','',text)
    return text
df['Tweets']=df['Tweets'].apply(cleanTxt)

st.subheader('Some of the extracted Tweets')
st.write(df)

def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

#Adding two new columns in Dataframe named Subjectivity and Polarity
df['Subjectivity']=df['Tweets'].apply(getSubjectivity)
df['Polarity']=df['Tweets'].apply(getPolarity)
st.subheader('DataFrame with new columns as Subjectivity and Polarity')
st.write(df)

#Creating function to get positive, negative or neutral values
def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score==0:
        return 'Neutral'
    else:
        return 'Positive'

#Adding analysis column into dataframe
df['Analysis']=df['Polarity'].apply(getAnalysis)
st.subheader('DataFrame after calculating Sentiments on tweets')
st.write(df)

#Sorting dataframe by polarity to see most Negative tweet
sortedDF=df.sort_values(by=['Polarity'])
st.subheader('Most Negative Tweets')
st.write(sortedDF.head())

#Getting percentage of negative tweets
ntweets=df[df.Analysis=='Negative']
ntweets=ntweets['Tweets']
neg=round((ntweets.shape[0]/df.shape[0]*100),1)
st.subheader('Getting Percentage of calculated sentiments of tweets')
st.write('Negative Tweets(%): ')
st.write(neg)

#Getting percentage of positive tweets
ptweets=df[df.Analysis=='Positive']
ptweets=ptweets['Tweets']
pos=round((ptweets.shape[0]/df.shape[0]*100),1)
st.write('Positive Tweets(%): ')
st.write(pos)

#Getting percentage of neutral tweets
netweets=df[df.Analysis=='Neutral']
netweets=netweets['Tweets']
neu=round((netweets.shape[0]/df.shape[0]*100),1)
st.write('Neutral Tweets(%): ')
st.write(neu)

#Sidebar
if page=="Bar Graph":
    st.subheader('Bar Graph')
    st.bar_chart(df['Analysis'].value_counts())
elif page=="Line Graph":
    st.subheader('Line Graph')
    st.line_chart(df['Analysis'].value_counts())
elif page=="WordCloud":
    st.subheader('Word Cloud for Mostly used hashtags in Tweets')
    allWords=''.join([twts for twts in df['Tweets']])
    wordCloud=WordCloud(width=750,height=510,random_state=20,max_font_size=119).generate(allWords)
    st.image(wordCloud.to_array())
