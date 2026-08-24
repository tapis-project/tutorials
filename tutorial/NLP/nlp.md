## Natural Language Processing (NLP)

### Text classification
Text classification is an important task in NLP. Common applications of text classification include:
- Sentiment analysis
- Spam detection 
- Topic labelling, etc.

There are two main approaches for text classification
* Rules based 
    - Handcrafted lingustic rules
    - Disadvantage: needs a lot of domain expertise and difficult to scale
* Machine learning based
    - Several machine learning approaches can be used for Text Classification. 
    - In order to train models on large text datasets, the text data is first converted to numerical data, also known as **feature extraction**. 
    - Bag of words and n-grams are one of the important feature extraction techniques.
    - Popular machine learning algorithms are:
        - Naive Bayes Classifier
        - Support vector machines
        - Deep learning 

### Sentiment Analysis
It is the process of classifying the text as positive, negative or neutral based on the emotions that are expressed in the text. 

It is commonly used to make business decisions or improve processes based on the reviews received by the customers/users. Manually analyzing all the reviews and feedback is time consuming and not scalable. Companies make use of modern NLP techniques and Machine learning algorithms to analyze the data. Some of the common applications of sentiment analysis are:
    - Customer Product Reviews
    - Market Research Analysis
    - Social Media Monitoring


### Tools for Sentiment Analysis

In this tutorial we will use tools provided by [Hugging Face](https://huggingface.co) to perform sentiment analysis. 

Hugging face platform provides tools that enables users to build, train and deploy their ML models and share their models and dataset with researchers, data scientists, developers,etc.

It is most notable for its [Transformers](https://huggingface.co/docs/transformers/index) library which is built for natural language processing applications.

### Transformers 
Transformer models are used to solve all kinds of NLP tasks. Transformer library helps to create and use shared models. Model Hub contains numermous models which be easily downloaded and used.

Most basic object in Transformers library is the pipeline(). It connects a model with all its required pre and post processing steps, allowing us to enter any input and getting the required answer.

In this tutorial we will explain how to use the pipeline function for performing sentiment analysis just with three to four lines of code and also how to build a Tapis Sentiment Analysis App.




