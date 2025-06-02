# 📧 Spam Detector

A simple spam message classifier built with Python and Streamlit. It uses natural language processing and machine learning to predict whether a message is spam or not.

## 🚀 Features


- Classifies messages as **Spam** or **Ham**
- Clean, interactive web UI with **Streamlit**
- Trained using **scikit-learn** models
- Can be deployed easily to **Streamlit Community Cloud**

## 🖼️ Screenshot

![App Screenshot](screenshot.png) <!-- Optional: Add if you have a screenshot -->



---

## 🚀 Features

- Data cleaning and preprocessing
- Text preprocessing (stopword removal, lowercasing, etc.)
- TF-IDF vectorization
- Model training using:
  - Naive Bayes
  - Logistic Regression
  - Random Forest
  - SVM
- Evaluation (Accuracy, Precision, Recall, F1 Score)
- Streamlit web app for real-time predictions

---

## 🔧 Tech Stack

- **Language**: Python 3
- **Libraries**: `pandas`, `scikit-learn`, `nltk`, `streamlit`, `joblib`
- **IDE**: Jupyter Notebook, VSCode
- **Deployment**: Streamlit

---

## 📊 Model Performance

| Model               | Accuracy | Precision | Recall | F1-Score |
|--------------------|----------|-----------|--------|----------|
| Naive Bayes        | ~98%     | High      | High   | High     |
| Logistic Regression| ~97%     | High      | High   | High     |
| SVM                | ~96%     | High      | High   | High     |
| Random Forest      | ~96%     | High      | High   | High     |

> *Naive Bayes performed the best overall on this dataset.*

---

## 🧪 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/spam-detection.git
   cd spam-detection


   ---

   
## 📝 Dataset

Name: SMS Spam Collection

Source: Kaggle Dataset

Contains 5,574 SMS messages classified as ham (legit) or spam.

---

## 📌 To Do / Future Work

Integrate deep learning models (LSTM, BERT)

Use word embeddings (GloVe, Word2Vec)

Deploy on the web using Heroku/Render

Improve preprocessing with lemmatization

---

## 🤝 Contributing

Feel free to fork the project and submit pull requests. Contributions are welcome!

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙌 Acknowledgements

Kaggle Dataset

NLTK and Scikit-learn teams

Streamlit community

---

## 📫 Contact

GitHub: LegendaryLapulgaa

Email: emmanuelnzekwue@icloud.com

---

## 🔧 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
