# Covid Public Concern

## Overview  
Using numerical statistics (Term Frequency – Inverse Document Frequency), we aim to discover the current trending topics on Canadian social media regarding the COVID-19 pandemic by collecting and analyzing 1000 Tweets from the popular social media platform Twitter.  

### Dataset Collection 
To gather the dataset required for this investigation, we utilize Twitter’s API, which is readily available for public use. Using the API, we are able to create a dataset of English Tweets from Canada which mention COVID, the various vaccines as well as the overall responses to the vaccination mandate across the country.  
Then we manually annotate the one thousand Tweets based on their topics and sentiment into seven topics and three sentiment categories.  

### Analysis  
To analyze our data we go through some minor preprocessing then compute the Term Frequency - Inverse Document Frequency (TF-IDF) scores for each word in each category and order them in decreasing order to generate a list of the top 10 keywords per category based on their TF-IDFscores.  

### Purpose 
By figuring out the keywords per category, we aim to draw some big-data conclusions on the general public’s sentiment on the pandemic as well as the government’s policies.  
Our end-goal is to investigate further on the salient topics discussed around the Coronavirus pandemic and what each topic primarily concerns, the relative engagement around these topics as well as how positive, neutral or negative the responses to the pandemic/vaccination has been.  

### Scope 
We believe that the results from our analysis can provide broader and deeper insight around this topic and also potentially aid in any future investigations surrounding this topic. 

## Dataset 

We used Tweepy, a Python library for accessing the Twitter API to collect our dataset.  

In order to collect 1000 tweets, we first created a Twitter developer account to generate consumer_key, consumer_secret, access_token, token_secret and bearer_token for authentication.  

We generated 26 requests to Twitter’s API (each for 100 Tweets) to collect 2600 Tweets in total. We collected 900 Tweets on 30th November 2021, 900 Tweets on 1st December 2021, and 800 Tweets on 2nd December 2021 . 

We set the language parameter to “English” and used the following keywords (hashtags and words) to filter in COVID related Tweets - #covid (for 260 Tweets), #coronavirus (for 260 Tweets), #pfizer (for 260 Tweets), #astrazeneca (for 260 Tweets), #moderna (for 260 Tweets), #COVID (for 260 Tweets), #vaccination (for 260 Tweets), Covid-19 (for 260 Tweets), COVID (for 260 tweets), and Coronavirus (for 260 tweets). We then filter-out 1200 unique COVID related English Tweets. 

Out of this we then randomly selected 1000 Tweets for our analysis. We created a dictionary to save our data in a .json file where each record has a Tweet id and text. We, then, manually read all 1000 Tweets for correctness. 

## Annotation 
Using the JSON data received from Twitter’s API, a short Python script was created to convert the JSON data into a CSV file with the Tweet text, category, and sentiment columns. Then to generate annotations, an open coding was conducted on the first 200 Tweets in the dataset to determine dominant and relevant topics. Upon thorough investigation, it was determined that most of the Tweets fell into one of seven different categories (Table 1): Variant/Mutation (V), Illness (I), Travel Restrictions (T), Covid Measurements (M),Vaccination (N), Covid Cases (C), and Others (O). 

Furthermore, each Tweet was categorized into three additional groups based on their sentiments: Positive (POS), Neutral (NEU) and Negative (NEG). We believed that seven topics and three sentiments best represented the data and that the most informative conclusions could be drawn. 

## Pre-processing 
After annotation, we dedicated our efforts to preprocessing each Tweet’s text to make them best suitable for analysis using Python. The following preprocessing decisions were applied: 
1. Lowercasing 
2. Newline Character Removal 
3. Non-alphanumeric Character Removal 
4. Stopword Removal (from A8) 

Lowercasing was done to remove double counting of the same word with different casing. Newline character removal was necessary to prevent them from altering the TF-IDF calculations. Non-alphanumeric characters were removed using Regex to make it easier to isolate words, and to prevent double counting between a word and the same word with a hashtag in front. Lastly, stopwords were removed to eliminate “meaningless” but frequent words from the TF-IDF counts. 

## TF-IDF 
Following the light preprocessing procedure, within the same Python script, a procedure was written to compute the TF-IDF scores for each word per category. The specific formula for computing the TF-IDF scores per category. 

The impact of our preprocessing decisions were noticeable. Compared with blindly running the TF-IDF script on the original unprocessed Tweets, the generated top 10 words for every category were much more relevant, rid of meaningless words, and contained no duplicate words. 
