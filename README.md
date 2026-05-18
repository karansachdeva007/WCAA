# WhatsApp Chat Analyzer with NLP Sentiment Analysis 📊💬

🔗 **Live Demo:** (https://wca007.streamlit.app/)

An interactive **WhatsApp Chat Analyzer** built using **Python** and **Streamlit** that transforms exported WhatsApp chats into meaningful insights using **Data Analysis**, **Visualization**, and **Natural Language Processing (NLP)** techniques.

The application supports both **individual** and **group chats**, providing detailed analytics such as message statistics, timelines, activity heatmaps, word clouds, emoji analysis, and NLP-based sentiment analysis.

---

# 🚀 Features

## 📈 Chat Statistics
- Total Messages
- Total Words
- Media Shared
- Links Shared

## 📅 Timeline Analysis
- Monthly Timeline
- Daily Timeline
- Most Active Days & Months

## 🔥 Activity Analysis
- Weekly Activity Map
- Monthly Activity Map
- Day vs Time Heatmap

## ☁️ Text Analysis
- Word Cloud Generation
- Most Common Words
- Emoji Analysis

## 😊 NLP-Based Sentiment Analysis
- Positive / Negative / Neutral Classification
- Sentiment Distribution Charts
- Monthly Sentiment Timeline
- User-wise Sentiment Analysis
- Sentiment Heatmap (Day vs Time)

## 👥 Group Chat Insights
- Most Active Users
- Top-N User Filtering
- User-wise Sentiment Comparison

---

# 🛠️ Tech Stack

## Backend & Data Processing
- Python 3.x
- Pandas
- NumPy
- Regular Expressions (Regex)

## NLP & Text Analysis
- NLTK (VADER Sentiment Analyzer)
- WordCloud
- Emoji
- URLExtract

## Data Visualization
- Matplotlib
- Seaborn

## Frontend
- Streamlit

## Development Tools
- PyCharm
- Git & GitHub

---

# 📂 Project Structure

```bash
WhatsApp-Chat-Analyzer/
│
├── app.py                 # Main Streamlit application
├── helper.py              # Analysis & visualization functions
├── preprocessor.py        # Chat preprocessing & parsing
├── stop_hinglish.txt      # Stopwords file
├── requirements.txt       # Required dependencies
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
```

---

## 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

### Activate Environment

#### Windows
```bash
venv\Scripts\activate
```

#### Mac/Linux
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

# 📥 How to Export WhatsApp Chat

1. Open WhatsApp Chat  
2. Click **More Options → Export Chat**  
3. Select **Without Media**  
4. Upload the `.txt` file into the application  

---

# 📊 Sample Analysis & Visualizations

The application provides multiple insights and visual analytics including:

- Monthly Chat Timeline
- Daily Activity Graph
- Activity Heatmap
- Word Cloud
- Emoji Analysis
- Most Active Users
- Sentiment Distribution
- User-wise Sentiment Comparison
- Sentiment Heatmap

---

# 🧠 NLP & Sentiment Analysis

The project uses **VADER Sentiment Analysis (NLTK)** to classify messages into:

- 😊 Positive
- 😐 Neutral
- 😞 Negative

Sentiment trends are visualized using:
- Pie Charts
- Monthly Sentiment Timeline
- Stacked Bar Charts
- Sentiment Heatmaps

---

# 🔍 Methodology

1. Export WhatsApp chat data  
2. Preprocess raw text using Regex  
3. Extract structured information (date, user, message)  
4. Perform statistical and NLP analysis  
5. Generate visual insights and dashboards using Streamlit  

---

# 📌 Applications

- Personal Chat Analysis
- Group Activity Monitoring
- Communication Pattern Analysis
- NLP & Data Science Learning
- Social Media Analytics

---

# 🔮 Future Enhancements

- Real-time chat analysis
- Multi-language support
- Advanced Deep Learning–based sentiment analysis
- AI-powered chat summarization
- Cloud deployment and mobile integration


---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

### Steps to Contribute:
1. Fork the repository  
2. Create a new branch  
3. Commit your changes  
4. Push the branch  
5. Open a Pull Request  

---

# 📜 License

This project is developed for educational and learning purposes.

---

# 👨‍💻 Author

## Karan Sachdeva

- LinkedIn: (https://www.linkedin.com/in/karan-sachdeva-kss007/)

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub and share your feedback!
