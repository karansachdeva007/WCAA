import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)



    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    if st.sidebar.button("Show Analysis"):
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user,df)
        st.title("Top Statistics")
        col1,col2,col3,col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        # monthly timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user,df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'],color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)


        # activity map
        st.title('Activity Map')
        col1,col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

        # Sentiment Heatmap
        st.title("Sentiment Heatmap (Day vs Time)")

        sentiment_heatmap_df = helper.sentiment_heatmap(selected_user, df)

        fig, ax = plt.subplots(figsize=(12, 6))
        sns.heatmap(
            sentiment_heatmap_df,
            cmap='coolwarm',
            ax=ax
        )

        ax.set_xlabel("Time Period")
        ax.set_ylabel("Day of Week")
        st.pyplot(fig)

        # finding the busiest users in the group(group level)

        if selected_user == "Overall":
            st.title("Most Busy Users")
            x , new_df= helper.most_busy_users(df)
            fig,ax = plt.subplots()

            col1,col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color='blue')
                plt.xticks(rotation=90)
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        # User-wise Sentiment Analysis (Group Chats)
        if selected_user == "Overall":
            st.title("User-wise Sentiment Analysis")

            # 🔽 Slider FIRST (important)
            top_n = st.slider(
                "Select number of top users to display",
                min_value=5,
                max_value=20,
                value=10,
                key="top_n_users"
            )

            # Compute sentiment
            user_sentiment_df = helper.user_wise_sentiment(df)

            # Select top N users
            user_sentiment_df['Total'] = user_sentiment_df.sum(axis=1)
            top_users_df = (
                user_sentiment_df
                .sort_values(by='Total', ascending=False)
                .head(top_n)
                .drop(columns='Total')
            )

            st.subheader(f"Top {top_n} Users – Sentiment Distribution")


            plt.clf()

            fig, ax = plt.subplots(figsize=(12, 6))
            top_users_df.plot(
                kind='bar',
                stacked=True,
                ax=ax
            )

            ax.set_xlabel("User")
            ax.set_ylabel("Number of Messages")
            ax.legend(title="Sentiment", loc='upper right')
            plt.xticks(rotation=45, ha='right')

            st.pyplot(fig, clear_figure=True)

        # wordcloud
        st.title("Word Cloud")
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words
        most_common_df = helper.most_common_words(selected_user,df)
        fig,ax = plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')
        st.title("Most Common Words")
        st.pyplot(fig)

        # Emoji Analysis - Top Emojis Bar Chart
        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Top Emojis")

        # Take top 10 emojis
        top_emoji_df = emoji_df.head(10)

        fig, ax = plt.subplots()
        ax.barh(top_emoji_df['emoji'], top_emoji_df['count'], color='skyblue')

        ax.set_xlabel("Count")
        ax.set_ylabel("Emoji")
        ax.invert_yaxis()  # highest count on top
        st.pyplot(fig)

        # Sentiment Analysis
        st.title("Sentiment Analysis")

        sentiment_counts, sentiment_df = helper.sentiment_analysis(selected_user, df)

        fig, ax = plt.subplots()
        ax.pie(
            sentiment_counts.values,
            labels=sentiment_counts.index,
            autopct='%1.1f%%',
            startangle=90
        )
        ax.axis('equal')
        st.pyplot(fig)

        # Monthly Sentiment Timeline
        st.title("Monthly Sentiment Timeline")

        sentiment_timeline = helper.monthly_sentiment_timeline(selected_user, df)

        fig, ax = plt.subplots()

        for sentiment in sentiment_timeline['sentiment'].unique():
            data = sentiment_timeline[sentiment_timeline['sentiment'] == sentiment]
            ax.plot(data['time'], data['message'], label=sentiment)

        plt.xticks(rotation='vertical')
        ax.legend()
        st.pyplot(fig)


