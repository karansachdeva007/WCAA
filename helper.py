from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
import emoji
from collections import Counter
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()


extract = URLExtract()

def fetch_stats(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

        # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # # fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # # fetch number of links shared
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages,len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts().head() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'user': 'name', 'count': 'percent'})
    return x, df

def create_wordcloud(selected_user,df):


    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=800, height=600, background_color='white', min_font_size=10)

    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc


def most_common_words(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    emojis = []

    for message in df['message'].dropna():
        for char in message:
            if emoji.is_emoji(char):
                emojis.append(char)
    emoji_df = pd.DataFrame(Counter(emojis).most_common(), columns=['emoji', 'count'])
    return emoji_df

def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap

def sentiment_analysis(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['message'] != '<Media omitted>\n']
    temp = temp[temp['user'] != 'group_notification']

    def get_sentiment(message):
        score = sia.polarity_scores(message)['compound']
        if score > 0.05:
            return 'Positive'
        elif score < -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    temp['sentiment'] = temp['message'].apply(get_sentiment)
    sentiment_counts = temp['sentiment'].value_counts()

    return sentiment_counts, temp


def monthly_sentiment_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['message'] != '<Media omitted>\n']
    temp = temp[temp['user'] != 'group_notification']

    def get_sentiment(message):
        score = sia.polarity_scores(message)['compound']
        if score > 0.05:
            return 'Positive'
        elif score < -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    temp['sentiment'] = temp['message'].apply(get_sentiment)

    sentiment_timeline = (
        temp
        .groupby(['year', 'month', 'sentiment'])
        .count()['message']
        .reset_index()
    )

    sentiment_timeline['time'] = sentiment_timeline['month'] + "-" + sentiment_timeline['year'].astype(str)

    return sentiment_timeline


def user_wise_sentiment(df):
    temp = df[df['message'] != '<Media omitted>\n']
    temp = temp[temp['user'] != 'group_notification']

    def get_sentiment(message):
        score = sia.polarity_scores(message)['compound']
        if score > 0.05:
            return 'Positive'
        elif score < -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    temp['sentiment'] = temp['message'].apply(get_sentiment)

    user_sentiment = (
        temp
        .groupby(['user', 'sentiment'])
        .count()['message']
        .unstack()
        .fillna(0)
    )

    return user_sentiment

def sentiment_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['message'] != '<Media omitted>\n']
    temp = temp[temp['user'] != 'group_notification']

    def get_sentiment_score(message):
        return sia.polarity_scores(message)['compound']

    temp['sentiment_score'] = temp['message'].apply(get_sentiment_score)

    # Create pivot table: Day vs Time period
    heatmap_data = temp.pivot_table(
        index='day_name',
        columns='period',
        values='sentiment_score',
        aggfunc='mean'
    ).fillna(0)

    return heatmap_data
