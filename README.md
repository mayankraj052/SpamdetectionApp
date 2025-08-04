# 📬 Spam Detection App

A machine learning-powered application that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP). This project includes:

- ✅ Command-line interface (CLI)
- ✅ Interactive Streamlit web app
- ✅ Trained model using `Multinomial Naive Bayes`
- ✅ TF-IDF-based text preprocessing
- ✅ K-Fold evaluation metrics

# 🖼️ Preview
![App Screenshot](Screenshot%202025-08-05%20000957.png)


## 🤖 Model Overview

- **Vectorizer**: `TfidfVectorizer(stop_words='english')`
- **Classifier**: `MultinomialNB()`
- **Training Strategy**: `10-Fold Cross Validation`
- **Evaluation Metrics**:
  - Accuracy: ~97.15%
  - Precision: ~99.66%
  - Recall: ~78.98%
  - F1 Score: ~88.10%
  - Geometric Mean: ~88.84%

### 🧠 Why Naive Bayes?
Multinomial Naive Bayes is efficient and performs well for **text classification tasks** like spam detection, where input features are word frequencies or TF-IDF scores.

---

## 🚀 How to Run Locally

### 1. Clone the Repository
<pre lang="bash"><code>git clone https://github.com/mayankraj052/SpamdetectionApp.git cd SpamdetectionApp </code></pre>

## 2.  Create a Virtual Environment
**for window**
<pre lang="bash"><code>
python -m venv venv
venv\Scripts\activate </code></pre>    
**macOS/Linux**
<pre lang="bash"><code>
source venv/bin/activate  </code></pre>

## 3. Install Requirements

<pre lang="bash"><code>pip install -r requirements.txt</code></pre>

## 4. Run Streamlit App

<pre lang="bash"><code>streamlit run app.py</code></pre>

## 5. Run Command-Line Tool

<pre lang="bash"><code>python spam_check_cli.py</code></pre>

# 🧪 Example Predictions

    "Hey John, I thought you might like this opportunity — earn $500/day working from home!" → Spam

    "Are we still meeting at 6 PM today?" → Ham

# 🗂 Dataset Used
*  SMS Spam Collection Dataset (UCI ML Repository)
* [Data Set Link]( https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)
*  Format: Label (spam or ham) + Message content

# 📦 Model Pipeline
#### The model pipeline is saved in spam_pipeline.pkl contains:
 * TF-IDF Vectorizer (preprocessing)
*  Multinomial Naive Bayes Classifier

<pre lang="python"><code>from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

spam_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('model', MultinomialNB())
])</code></pre>

# 📈 Evaluation via K-Fold Cross-Validation

<pre lang="python"><code>from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix</code></pre>
* Used to validate model performance across 10 different splits. Metrics like accuracy, precision, recall, F1, specificity, and geometric mean were averaged.
## 🛠 Tools & Libraries
* Python 3.11+
* Scikit-learn
* Pandas & NumPy
* Streamlit
* Joblib
* Git for version control

# 📜 License

This project is open-source and available under the MIT License.
🙋‍♂️ Author

Made with ❤️ by Mayank Raj


