# IrisDetection

This code is to train and compare quickly different algorithms, for now pretty much for scikit learn.
You can easily compare algorithm and parameters using the configuration
file.
The comparison will be performed on an average score on a cross validation
where train/test proportion and number of sample are user defined
(by default : 90%/10% for train/test proportion and 10 for the number of sample)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
```
Python 3.6.1
numpy
scipy
sklearn
```
You can install them through the requirements.txt file with:
```
pip install -r requirements.txt
```

Use "virtualenv" if you want to keep another version of python on your computer.

### Running and using

Configuration folder (inputs) are in the folder "data" as
"algorithmComparison" or "SVMcomparisonInputParameters".
Please check if changing any path is needed in these files.
In this folder, you can specify which algorithms you want to compare,
with which parameters of algorithms and the sample_number or test_proportion you want use for the cross validation.

Here are the available algorithms (from scikit-learn):
   - svm
   - LogisticRegression
   - NaiveBayes

Feel free to add your own personal algorithms


##### Use cases
command line to use the code:
```
python detection.py conf=data/SVMcomparaisonInputParameters.json
```
or
```
python detection.py conf=data/algorithmComparaison.json
```

## Authors

* **Christophe Silhouette** - *Initial work* - [PhoenixRebirth](https://github.com/phoenixRebirth)
