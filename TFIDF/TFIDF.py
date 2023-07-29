import pandas as pd
import re
import math

df = pd.read_csv('tweets.csv')

df['text'] = df['text'].str.lower()
df['text'] = df['text'].str.replace("\n", " ")
df['text'] = df['text'].str.replace("rt", " ")
df['text'] = df['text'].map(lambda x: re.sub(r'[^a-z0-9 $]', "", x))

stopwords_file = open('stopwords.txt', 'r')
stopwords = []

for line in stopwords_file:
    if "#" not in line:
        stopwords.append(line.strip("\n"))

stopwords_file.close()

count_dict = {"V": {}, "I": {}, "T": {}, "M": {}, "N": {}, "C": {}, "O":{}, "NEG": {}, "NEU": {}, "POS": {}}
tfidf_dict = {"V": {}, "I": {}, "T": {}, "M": {}, "N": {}, "C": {}, "O":{}, "NEG": {}, "NEU": {}, "POS": {}}
output_dict = {"V": [], "I": [], "T": [], "M": [], "N": [], "C": [], "O":[], "NEG": [], "NEU": [], "POS": []}
num_types = 10

for type in count_dict.keys():
    tempDF = []
    if type == "NEG" or type == "NEU" or type == "POS":
        tempDF = df[df.sentiment == type]['text']
    else:
        tempDF = df[df.title == type]['text']
    
    for each_sentence in tempDF:
        sentence_split = each_sentence.split()
        for word in sentence_split:
            if word not in stopwords:
                if word in count_dict[type]:
                    count_dict[type][word] += 1
                else:
                    count_dict[type][word] = 1
    
for type in count_dict.keys():
    for word in count_dict[type]:
        number_of_types_that_use_the_word = 0
        for inner_type in count_dict.keys():
            if word in count_dict[inner_type]:
                number_of_types_that_use_the_word += 1
        tf = count_dict[type][word]
        idf = math.log(num_types/number_of_types_that_use_the_word,10)
        tfidf_dict[type][word] = tf * idf

for type in tfidf_dict:
    counter = 0
    tfidf_dict[type] = dict(sorted(tfidf_dict[type].items(), key=lambda item: item[1], reverse=True))
    pd.DataFrame.from_dict(data=tfidf_dict[type], orient='index', columns=['tfidf_score']).to_csv(type+".csv", header=True)


print(output_dict)

