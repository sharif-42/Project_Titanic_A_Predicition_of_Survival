# Project Titanic A Prediction of Survival

## Overview
The sinking of the Titanic is one of the most infamous shipwrecks in history.On April 15, 1912, during her maiden 
voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. 
Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 
passengers and crew.While there was some element of luck involved in surviving, it seems some groups of people were 
more likely to survive than others.

This project predict predict if a passenger survived the sinking of the Titanic or not. For each in the test set, 
we predict a 0 or 1 value for the variable. Here 1 means the passenger survived otherwise Failed to Survived.

## Data Set
Data sets were collected from [**Kaggle**](https://www.kaggle.com/c/titanic/data). 

Data sets contain two types of  similar data-sets that include passenger information like name, age, gender, 
socio-economic class, etc. One data-set is titled  ***train.csv*** and the other is titled ***test.csv***.

The ***train.csv*** will contain the details of a subset of the passengers on board (891 to be exact) and importantly, 
will reveal whether they survived or not, also known as the “ground truth”.

The ***test.csv*** data-set contains similar information of 418 passengers but does not disclose the “ground truth” 
for each passenger. We have to predict whether the other 418 passengers on board (found in test.csv) survived.

### Data Dictionary
| Variable | Definition | Key |
| :---         |     :---:      |          ---: |
| survived   | Survived     | 0=No, 1 = Yes    |
| pclass     | Ticket Class       | 1 = 1st, 2 = 2nd, 3 = 3rd  |
| sex     | Sex       | Male, Female      |
| Age     | Age In year       |       |
| sibsp     | # of siblings / spouses aboard the Titanic       |     |
| parch    | # of parents / children aboard the Titanic    |      |
| ticket     | Ticket number       |       |
| fare     | Passenger fare       |       |
| cabin     | Cabin number       |       |
| embarked     | Port of Embarkation       |   C = Cherbourg, Q = Queenstown, S = Southampton    |

### Variable Notes
pclass: A proxy for socio-economic status (SES)
1st = Upper
2nd = Middle
3rd = Lower

age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

sibsp: The dataset defines family relations in this way...
Sibling = brother, sister, stepbrother, stepsister
Spouse = husband, wife (mistresses and fiancés were ignored)

parch: The dataset defines family relations in this way...
Parent = mother, father
Child = daughter, son, stepdaughter, stepson
Some children travelled only with a nanny, therefore parch=0 for them.

### Used Tools:
* Python 
* Numpy
* Pandas for data manipulation
* Matplotlib and Seaborn for data visualization
* Jupyter Notebook
* Scikit Learn to build models

### Installing Jupyter Notebook Using PIP
~~~~
python3 -m pip install --upgrade pip
python3 -m pip install jupyter
~~~~
### Inatall Scikit Learn Using PIP
~~~~
pip install scikit-learn
~~~~
### Install Numpy Using PIP
~~~~
pip install numpy
~~~~
### Install Pandas Using PIP
~~~~
pip install pandas
~~~~
### Install Matplotlib Using PIP
~~~~
pip install matplotlib
~~~~