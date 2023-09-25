import csv as cs
temp = []
sentiment = []

with open('FinalDataSet.csv', 'r') as mf:
    fileReader=cs.reader(mf)
    for row in fileReader:
        temp.append(row)

for row in temp:
    if(row!=[]):
        sentiment.append(row) 

#print(sentiment)
sentimentAnalysis = []
for item in sentiment:
    sentimentAnalysis.append(item[-1])

#print(sentimentAnalysis)

import matplotlib.pyplot as plt

# Your list of labels
labels = ['Positive', 'Negative', 'Neutral']

# Count the occurrences of each label in the list
positive_count = sentimentAnalysis.count('Positive')
negative_count = sentimentAnalysis.count('Negative')
neutral_count = sentimentAnalysis.count('Neutral')

# Create a list of counts
counts = [positive_count, negative_count, neutral_count]
print(counts)
# Define colors for the pie chart
colors = ['green', 'red', 'gray']

# Create a pie chart
plt.pie(counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Add a title
plt.title('Sentiment Analysis of TV Show')

# Display the pie chart
plt.show()