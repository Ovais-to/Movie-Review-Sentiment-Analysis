# Movie Sentiment Analysis

## Project Overview
This project applies Natural Language Processing (NLP) techniques to analyze movie reviews from the IMDB dataset. It involves sentiment analysis to classify reviews as either positive or negative using a Naive Bayes classifier.

## Key Features
- Data cleaning and preprocessing including removing special characters and stemming.
- Transformation of text data into a suitable format for machine learning models using TfidfVectorizer.
- Sentiment analysis using Multinomial Naive Bayes.
- Evaluation of model accuracy through metrics like accuracy score, confusion matrix, and classification report.

## Dataset
The dataset consists of movie reviews from IMDB. Each review is labeled as either positive or negative.

## Installation
This project requires the following Python libraries: pandas, numpy, scikit-learn, nltk, seaborn, and pickle. You can install these packages using pip:

```bash
pip install pandas numpy scikit-learn nltk seaborn pickle
```

## Usage
The project includes code for preprocessing the data, training the Naive Bayes model, and making predictions on new data. Users can input their own movie review and receive a sentiment prediction.

## Visualization
A sample visualization of the sentiment distribution among movie reviews is included. Here's a snapshot of the code and its output:

![Code Snapshot](path-to-your-code-image)

## Results
The performance of the model is quantified using accuracy score, confusion matrix, and classification report, highlighting the effectiveness of the Naive Bayes classifier in sentiment analysis.

## Contributing
Suggestions and contributions are welcome! Feel free to fork this repository and submit pull requests, or open an issue for any bugs or improvements.

## License
This project is open-source and available under the [MIT License](LICENSE.md).
