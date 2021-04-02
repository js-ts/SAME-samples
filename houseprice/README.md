## Introduction

This sample pipeline uses some advanced essemble techniques to stack a wide variety of models. 

The features engeneering is rather parsimonious (at least compared to some others great scripts) . It is pretty much:
- Imputing missing values by proceeding sequentially through the data
- Transforming some numerical variables that seem really categorical
- Label Encoding some categorical variables that may contain information in their ordering set
- Box Cox Transformation of skewed features (instead of log-transformation) : This gave a slightly better result both on leaderboard and cross-validation.
- Getting dummy variables for categorical features.

Then we choose many base models (mostly sklearn based models + sklearn API of DMLC's XGBoost and LightGBM), cross-validate them on the data before stacking/ensembling them. The key here is to make the (linear) models robust to outliers. This improved the result both on LB and cross-validation.


## Acknowledgments

### Code
The code in here was adapted from https://www.kaggle.com/serigne/stacked-regressions-top-4-on-leaderboard. If you like it, please show support to the original Notebook's author by upvoting.

### Dataset
The Ames Housing dataset was compiled by Dean De Cock for use in data science education. It's an incredible alternative for data scientists looking for a modernized and expanded version of the often cited Boston Housing dataset. 
