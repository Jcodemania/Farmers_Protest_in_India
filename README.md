<h1>Sentiment Analysis on the Tweets of People of India about Farmers Protest Using Twitter API</h1>

<h4>Introduction</h4>
<p>Every day, we generate huge amounts of text online, creating vast quantities of data about what is happening in the world and what people think. All of this text data is an invaluable resource that can be mined in order to generate meaningful business insights for analysts and organizations. But analyzing all of this content isn’t easy, since converting text produced by people into structured information to analyze with a machine is a complex task. In recent years though, Natural Language Processing and Text Mining has become a lot more accessible for data scientists, analysts, and developers alike. In this project, I am going to analyse the sentiments on the Tweets of people of India who are giving feedback to Farmer Bill or Farmer’s Protest. </p>

<h4>Purpose</h4>
<p>Today, social media covers a huge part of everyone's life. They are increasingly becoming the platform of communication for every means. Businesses can effectively utilize this by carefully listening and monitoring consumers. To properly understand customer needs, it is imperative to leverage Sentiment Analysis. Also, it can be used proactively to solve many business problems. It can also benefit Health Professionals, Policymakers, State and Central governments, and societal representatives.</p>

<h4>Proposed Solution</h4>
<p>Using various Twitter and Python API's I fetched Tweets and performed Sentiment Analysis on the Tweets of the people of India to gain a wider public opinion on farmer’s bill which is officially known as Indian Agriculture Act 2020. </p>

<h4>This project will be completed into three phases:</h4>
<p>
  <b>Building a Corpus:</b> I have used Tweepy Library to gather text data from Twitter’s API with special keyword(#FarmerBill or #FarmerProtest).<br>
<b>Analyzing text:</b> Sentiment analysis to determine the attitude of the mass is positive, negative or neutral towards the subject of interest. For that I have used TextBlob python library to calculate sentiments.<br>
<b>Visualizing results:</b> Graphical representation of the sentiments is done using streamlit library and wordCloud. And this project is deployed using a platform named Streamlit.</p>
