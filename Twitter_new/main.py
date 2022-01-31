import twint
from pathlib import Path
from textblob import TextBlob


def my_tweets():
    c = twint.Config()
    c.Username = "elonmusk"
    c.Search = "the"
    c.Count = True
    # c.Limit = 1000
    c.Since = "2019-01-01"
    c.Until = "2022-01-01"
    c.Store_csv = True
    c.Custom["tweet"] = ["created_at", "tweet"]
    c.Output = "tweets.csv"
    twint.run.Search(c)

def analysis():
    data = open('tweets.csv', 'r', encoding='utf-8')
    data_with_analysis = open('tweets_with_analysis.csv', 'w')
    result = open('result.csv', 'w')
    neutral = 0
    positive = 0
    negative = 0
    for tweet in data:
        tweet = tweet.strip('\n')
        analysistweet = TextBlob(tweet).polarity
        data_with_analysis.write(f'{tweet}, {analysistweet}\n')
        if analysistweet == 0:
            neutral += 1
        elif analysistweet > 0:
            positive += 1
        else:
            negative += 1
    sum_tweets = neutral + negative + positive
    result.write(f'Всего было проанализировано {sum_tweets} твита(ов).\nИз них {round(neutral / sum_tweets * 100, 1)}% твитов нейтральной тональности, {round(positive / sum_tweets * 100, 1)}% твитов позитивной и {round(negative / sum_tweets * 100, 1)}% негативной тональности')
    data.close()
    data_with_analysis.close()
    result.close()

def main():
    tweets = Path('tweets.csv')
    if not tweets.is_file():
        my_tweets()
    analysis()




if __name__ == '__main__':
    main()

