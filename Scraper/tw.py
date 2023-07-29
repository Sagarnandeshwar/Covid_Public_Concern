import json

def main():
    # Tweets from tweet1 
    file_input = open("tweet1.json", 'r')
    dataframe = json.load(file_input)

    tweet_text_list = []
    main_tweet_list = []
    
    total_tweets = 0
    duplicate_tweets = 0
    
    for tweets in dataframe["data"]:
        if tweets["text"] not in tweet_text_list:
            tweet_text_list.append(tweets["text"])
            main_tweet_list.append(tweets)
            total_tweets = total_tweets + 1
        else:
            duplicate_tweets = duplicate_tweets + 1

    file_input.close()

    # Tweets from tweet2

    file_input = open("tweet2.json", 'r')
    dataframe = json.load(file_input)
    
    for tweets in dataframe["data"]:
        if tweets["text"] not in tweet_text_list:
            tweet_text_list.append(tweets["text"])
            main_tweet_list.append(tweets)
            total_tweets = total_tweets + 1
        else:
            duplicate_tweets = duplicate_tweets + 1
    
    file_input.close()

    # Tweets from tweet3

    file_input = open("tweet3.json", 'r')
    dataframe = json.load(file_input)
    
    for tweets in dataframe["data"]:
        if tweets["text"] not in tweet_text_list:
            tweet_text_list.append(tweets["text"])
            main_tweet_list.append(tweets)
            total_tweets = total_tweets + 1
        else:
            duplicate_tweets = duplicate_tweets + 1
    
    file_input.close()

    # Tweets from tweet4

    file_input = open("tweet4.json", 'r')
    dataframe = json.load(file_input)
    
    for tweets in dataframe["data"]:
        if tweets["text"] not in tweet_text_list:
            tweet_text_list.append(tweets["text"])
            main_tweet_list.append(tweets)
            total_tweets = total_tweets + 1
            if total_tweets == 1000:
                break
        else:
            duplicate_tweets = duplicate_tweets + 1
    
    file_input.close()

    #writting 1000 tweets in 

    final_data = {"data":main_tweet_list}
    file_output = open("ALLTweets.json", 'w')
    json.dump(final_data,file_output)
    file_output.close
            
            
    

    
if __name__ == "__main__":
    main()
