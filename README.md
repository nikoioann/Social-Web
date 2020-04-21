# Social-Web
A twitter analysis report

Nikolas Ioannou 
Paris Sfikouris
Arsh Sadana
Omer
Osman

Extracted from project Report
"""
...
Explanation of the code
Our code for the project is Python object-oriented. We have
two classes each of them responsible for distinct uses. In
the first class, TwitterClient is responsible for the
authentication of the user and for retrieving the client API.
This helped with granting access to Twitter data. The
second class, TweetAnalyzer, as it is stated by the name, is
used for analyzing our tweets. It contains four(4) definitions.
1. Contain_hashtags - determine if a certain hashtag
is present in the tweet
2. Filter_tweets - responsible for removing a tweet
from data frame if a hashtag is not included
3. Clean_tweet - remove all non-essential characters
4. Tweets_to_dataframes - create a data frame and
store information we chose from each tweet.
The control flow of the script starts with creating two
objects, one of each class mentioned before, triggering
constructors that initialized the authentication process using
our credentials stored in a different script. We created two
arrays, accounts and hashtags which are the accounts that
we would mine their tweets and the hashtags we would use
to filter the tweets we needed.
For each account, we acquired their tweets through the
method user_timeline and we performed data cleaning and
hashtag filtering before creating a data frame to store it. We
then proceeded with concatenating all the data frames and
exporting it to a CSV file.
...
"""
