# Reconstruction-Based Deep Learning Models for Randomly Generated Time Series Anomaly Detection 

## Abstract:

Time series anomalies can offer critical information relevant to various fields, including and not limited to seismology (earthquakes), medicine (abnormal respiratory sounds), finance (stock price fluctuations), physics (gravitaional waves), and industrial prognostics (machine health monitoring). However, detecting anomalies in time series data is particularly challenging due to the vague definition of anomalies and data’s frequent lack of labels and highly complex temporal correlations. Current state-of-the-art unsupervised deep learning methods for anomaly detection suffer from scalability and portability issues, and may have high false positive rates. 

This work is an attempt to utilize and test the effectiveness of several deep learning models in detecting collective anomalies within randomly generated data. The data is initially labeled for the purpose of assessing the models' performance, but the models are blind to these labels, so the problem in hand is an unsupervised one. The data is preprocessed, and the models are trained on it in such a way to allow for effective time-series data reconstruction. After reconstruction errors are computed using MSE loss, a threshold is defined, over which data points are considered anomalous. Anomalous regions are detected, and evaluation metrics are computed for each model. A brief comparison between the models utilized and a few closing comments are made in regards to the results obtained.


## Methodology:
2023 Data 


## Data and Data Preprocessing:
<p align="center">
<img align="center" width="1000" src="https://github.com/BadeaTayea/Mini-Projects/blob/main/Anomaly%20Detection/Images/Train%20Dataset.png">
</p>

<p align="center">
<img align="center" width="1000" src="https://github.com/BadeaTayea/Mini-Projects/blob/main/Anomaly%20Detection/Images/Test%20Dataset.png">
</p>



<p align="center">
<img align="center" width="300" src="https://github.com/BadeaTayea/Mini-Projects/blob/main/Anomaly%20Detection/Images/Data/Training%20Dataset%20-%20Non-anomalous%20Region.png">
</p>

<p align="center">
<img align="center" width="300" src="https://github.com/BadeaTayea/Mini-Projects/blob/main/Anomaly%20Detection/Images/Data/Testing%20Dataset%20-%20First%20Anomalous%20Region.png">
<img align="center" width="300" src="https://github.com/BadeaTayea/Mini-Projects/blob/main/Anomaly%20Detection/Images/Data/Testing%20Dataset%20-%20Second%20Anomalous%20Region.png">
<img align="center" width="300" src="https://github.com/BadeaTayea/Mini-Projects/blob/main/Anomaly%20Detection/Images/Data/Testing%20Dataset%20-%20Third%20Anomalous%20Region.png">
</p>


<p align="center">

<img align="center" width="300" src="https://github.com/BadeaTayea/Mini-Projects/blob/main/Anomaly%20Detection/Images/Data/Training%20and%20Testing%20Data%20of%20Day%203.png">
<img align="center" width="300" src="https://github.com/BadeaTayea/Mini-Projects/blob/main/Anomaly%20Detection/Images/Data/Sequences%20(Preprocessed).png">
</p>

## Deep Learning Models:

### 1. CNN-Based Autoencoder
### 2. LSTM-Based Autoencoder 
### 3. Convolutional Neural Network
### 4. Recurrent Neural Network (LSTM)
### 5. Transformer

## Comparison:
<p align="center">
<img align="center" width="750" src="https://github.com/BadeaTayea/Mini-Projects/blob/main/Anomaly%20Detection/Images/Comparison%20of%20Model%20Performance.png">
</p>

## Summary and Comments:




## Backlog
| <img align="center" width="300" src="https://github.com/BadeaTayea/Mini-Projects/blob/main/Anomaly%20Detection/Images/Data/Training%20Dataset%20-%20Non-anomalous%20Region.png">  | <img align="center" width="300" src="https://github.com/BadeaTayea/Mini-Projects/blob/main/Anomaly%20Detection/Images/Data/Testing%20Dataset%20-%20First%20Anomalous%20Region.png"> |
| :---: | :---: |
| <img align="center" width="300" src="https://github.com/BadeaTayea/Mini-Projects/blob/main/Anomaly%20Detection/Images/Data/Testing%20Dataset%20-%20Second%20Anomalous%20Region.png">  | <img align="center" width="300" src="https://github.com/BadeaTayea/Mini-Projects/blob/main/Anomaly%20Detection/Images/Data/Testing%20Dataset%20-%20Third%20Anomalous%20Region.png">  |


