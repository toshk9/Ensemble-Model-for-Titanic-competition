# Titanic Survival Prediction using Ensemble Model

This repository contains the code for the Titanic survival prediction competition on Kaggle. The goal of the competition is to develop a model that can accurately predict the survival of passengers aboard the Titanic based on various features. The main file containing the data preparation code, model creation and so on is called **ensemble_titanic_competition.ipynb**

## Installing
Run the file called **requirements_installing.py** to install all the required modules

## Dataset
The dataset folder **titanic** contains the training and testing datasets in CSV format. These datasets are used for model training and evaluation.

## Preprocessing and Data Visualization
The notebook file includes the code for data preprocessing, where missing values are handled and features are transformed. It also includes data visualization techniques to gain insights into the data and understand the correlations between different variables.

## Ensemble Model
The ensemble model is constructed using a stacking technique, combining the predictions of multiple base models. The following base models are used: RandomForestClassifier, SVC, GradientBoostingClassifier, and LogisticRegression. The predictions of these models are then used as input to a meta-algorithm, XGBoost, which generates the final predictions.

## Stacking
Stacking is a method of combining multiple models by training a meta-model on their predictions. In this case, the predictions of the base models are stacked together and used as input features for the meta-model. This allows the ensemble model to leverage the strengths of each base model and improve overall prediction accuracy.

## Result
At the end of the notebook, the model's performance on the competition's test dataset is provided. The score represents the accuracy of the model's predictions in the competition.

Feel free to explore the notebook to understand the implementation details and experiment with different models and techniques for improving the predictions.

Good luck with your own experiments and participation in the Titanic competition on Kaggle!
