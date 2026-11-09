# SMS Spam Detection Using Machine Learning

## 1. Project Overview

This project uses machine learning and Natural Language Processing (NLP) to classify SMS messages as either **Spam** or **Ham (Legitimate Message)**.

The objective is to build a model that can identify unwanted messages by learning patterns from previously labelled SMS messages.

The project uses TF-IDF for text representation and Multinomial Naive Bayes for classification.

## 2. Problem Statement

SMS spam messages are a common problem. They can contain misleading offers, unwanted advertisements, and fraudulent claims.

Manually identifying these messages can be inconvenient.

This project explores how machine learning can automate SMS classification and distinguish legitimate messages from spam.

## 3. Dataset

The project uses the SMS Spam Collection dataset.

Dataset information:

- Total messages: 5,572
- Ham messages: 4,825
- Spam messages: 747
- Features: Label and message

Class distribution:

| Label | Number of messages |
|---|---:|
| Ham | 4,825 |
| Spam | 747 |
| Total | 5,572 |

The dataset is imbalanced because legitimate messages make up approximately 86.59% of the data, while spam messages account for approximately 13.41%.

This makes accuracy alone insufficient for evaluating the model.

## 4. Data Exploration

During exploratory data analysis, I investigated:

- Distribution of spam and ham messages.
- Average message length.
- Most frequently occurring words.
- Differences in word frequencies between spam and legitimate messages.

One observation was that spam messages were longer on average than legitimate messages in this dataset.

- Average ham message length: approximately 71.48 characters.
- Average spam message length: approximately 138.67 characters.

## 5. Text Preprocessing

Before training the model, I prepared the messages using the following steps:

1. Converted text to lowercase.
2. Removed punctuation.
3. Tokenized messages into individual words using NLTK.
4. Removed English stopwords.
5. Preserved the words "not" and "no" because they can affect meaning.

The processed words were joined back into text strings for vectorization.

## 6. Text Vectorization

Machine learning models cannot directly understand raw text. Therefore, I converted the messages into numerical representations.

I explored two approaches:

**Bag of Words (BoW)**

CountVectorizer was used to represent messages based on word frequencies.

**TF-IDF (Term Frequency-Inverse Document Frequency)**

TfidfVectorizer was used to assign numerical weights to words based on their importance within individual messages and across the dataset.

TF-IDF was selected for the final model.

The vectorizer was fitted on the training data only to prevent data leakage.

## 7. Model Training

The dataset was divided into:

- Training data: 80% (4,457 messages).
- Testing data: 20% (1,115 messages).

Stratified splitting was used to maintain approximately the same class proportions in both datasets.

**Algorithm:** Multinomial Naive Bayes

Multinomial Naive Bayes was selected because it is a suitable classification algorithm for many text-classification tasks.

The model was trained using the TF-IDF representations of the training messages.

## 8. Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

### Threshold comparison

I experimented with different classification thresholds to investigate the trade-off between precision and recall.

The results were:

| Threshold | Precision | Recall | F1-score |
|---|---:|---:|---:|
| 0.1 | 0.746 | 0.926 | 0.826 |
| 0.2 | 0.977 | 0.839 | 0.903 |
| 0.3 | 0.984 | 0.805 | 0.886 |
| 0.4 | 1.000 | 0.758 | 0.863 |
| 0.5 | 1.000 | 0.698 | 0.822 |

A threshold of 0.2 produced the highest F1-score among the tested thresholds.

### Selected threshold: 0.2

At this threshold, the confusion matrix was:

| Actual / Predicted | Ham | Spam |
|---|---:|---:|
| Ham | 963 | 3 |
| Spam | 24 | 125 |

Key results:

- Accuracy: approximately 97.58%.
- Spam precision: approximately 97.66%.
- Spam recall: approximately 83.89%.
- Spam F1-score: approximately 90.25%.

The model correctly identified 125 out of 149 actual spam messages.

It missed 24 spam messages and incorrectly classified 3 legitimate messages as spam.

## 9. Testing on New Messages

After training and evaluation, I tested the model using two previously unseen SMS messages.

Example 1:

"Hey, are you coming to class tomorrow?"

Prediction: Ham

Spam probability: approximately 0.21%.

Example 2:

"Congratulations! You have won a free gift voucher. Claim now!"

Prediction: Spam

Spam probability: approximately 88.17%.

The predictions were consistent with the expected classifications of these example messages.

## 10. Model Persistence

To reuse the trained model without retraining it, I used Joblib to save:

- `spam_classifier.pkl` — the trained Multinomial Naive Bayes model.
- `tfidf_vectorizer.pkl` — the fitted TF-IDF vectorizer.

I also loaded both saved objects and verified that they produced the same probabilities as the original objects.

## 11. Limitations

Although the model achieved promising results, it has some limitations:

1. The dataset is relatively small and may not represent all modern SMS spam patterns.
2. The dataset contains more legitimate messages than spam messages.
3. Removing punctuation may remove useful information from some messages.
4. The model may struggle with new spam patterns that were not represented in its training data.
5. The selected threshold still allows some spam messages to go undetected.

**Evaluation note:** The threshold comparison was performed using the test set. Therefore, the reported results at 0.2 are exploratory rather than a fully independent final evaluation. A stronger evaluation would select the threshold using a separate validation set and evaluate the chosen threshold once on an untouched test set.

## 12. Future Improvements

Possible improvements include:

- Evaluating additional classification algorithms.
- Experimenting with alternative text preprocessing techniques.
- Testing on a larger and more recent dataset.
- Using a separate validation set for threshold selection.
- Building a simple web application for SMS classification.
- Monitoring model performance as new message patterns emerge.

## Project Structure

```text
SMS Spam Detection/
├── data/
│   ├── SMSSpamCollection
│   └── cleaned_sms.csv
├── models/
│   ├── spam_classifier.pkl
│   └── tfidf_vectorizer.pkl
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_text_preprocessing.ipynb
│   └── 03_text_vectorization.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Follow these steps to set up the project locally.

**1. Clone the repository**

```bash
git clone https://github.com/Sammy5code/AI-Learning.git
```

**2. Navigate to the project directory**

```bash
cd "Traditional ML project/SMS Spam Detection"
```

**3. Create a virtual environment**

```bash
python -m venv ai-env
```

**4. Activate the virtual environment**

On Linux and macOS:

```bash
source ai-env/bin/activate
```

**5. Install the required dependencies**

```bash
pip install -r requirements.txt
```

## Running the Project

1. Make sure your virtual environment is activated.
2. Start Jupyter Notebook:

```bash
jupyter notebook
```

3. Navigate to the `notebooks` directory.
4. Run the notebooks in the following order:

   - `01_data_exploration.ipynb`
   - `02_text_preprocessing.ipynb`
   - `03_text_vectorization.ipynb`

Run each notebook from beginning to end to reproduce the project workflow.

## 13. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- Scikit-learn
- Joblib
- Jupyter Notebook

## 14. Conclusion

This project provided practical experience in developing a traditional machine learning classification system.

It covered the complete workflow, from data exploration and text preprocessing to vectorization, model training, evaluation, error analysis, threshold selection, inference, and model persistence.

The project also demonstrated that evaluating a machine learning model requires more than looking at accuracy. Precision, recall, F1-score, and the consequences of classification errors must also be considered.