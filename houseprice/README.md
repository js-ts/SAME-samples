## Introduction

This sample pipeline uses some advanced essemble techniques to stack a wide variety of models. 

The features engeneering is rather parsimonious (at least compared to some others great scripts) . It is pretty much:
- Imputing missing values by proceeding sequentially through the data
- Transforming some numerical variables that seem really categorical
- Label Encoding some categorical variables that may contain information in their ordering set
- Box Cox Transformation of skewed features (instead of log-transformation) : This gave a slightly better result both on leaderboard and cross-validation.
- Getting dummy variables for categorical features.

Then we choose many base models (mostly sklearn based models + sklearn API of DMLC's XGBoost and LightGBM), cross-validate them on the data before stacking/ensembling them. The key here is to make the (linear) models robust to outliers. This improved the result both on LB and cross-validation.


## Quickstart instruction

### Step 1: Download SAME

```bash
curl -L0 https://get.sameproject.org/ | bash -
```

### Step 2: Install Kubeflow locally
```bash
same installK3s
```

### Step 3: Run your first SAME program

Go to the `houseprice` directory and run the following command:
```bash
same program run --run-name demo --experiment-name demo 
```
That will trigger a SAME program run on your local Kubeflow cluster.

To view the result, first open a tunnel to the Kubeflow UI
```bash
kubectl port-forward svc/ml-pipeline-ui 8080:80
```
Following that, open a browser and go to http://localhost:8080 to see the Kubeflow UI. Go tho the Experiment `demo` and find your SAME run named `demo`.

### Step 4: Inspect your SAME program

#### Using `same run list` 
The command `same run list` can be used to inspect the executions of your SAME program, like this
```bash
same run list
```

You should see something like this
```
INFO[0000] No scheme specified in the URL, so assuming local - 'same.yaml' 
ID                                     NAME          PIPELINEVERSION                                 CREATED                    STATUS      rmsle
489a193e-62ac-42c8-b532-df5a0781cace   demo          House Prices - Advanced Regression Techniques   2021-03-29T19:07:44.000Z   Succeeded   0.0755
```

Beside identifying information in `ID`, `NAME`, `PIPELINEVERSION` columns, take a look at the `STATUS` and the columns to its right. The `STATUS` column shows the status of the execution: `Succeeded`, `Failed`, or `Running`. Columns after the `STATUS` column contains pipeline metrics like RMS, precisions, recalls, etc... and will vary between pipelines.

#### Using `same run describe`
While `same run list` show information of all the executions of a given SAME program, the command `same run describe` will present information from a particular run. You will need a `<run-id>` obtained from the `ID` column in the outpt of `same run list`. For example,

```bash
same run describe --run-id 489a193e-62ac-42c8-b532-df5a0781cace
```

You should see something like this
```

You sent Today at 5:10 PM
Name:           awesome-run
ID:             489a193e-62ac-42c8-b532-df5a0781cace
Pipeline:
    Name:       House Prices - Advanced Regression Techniques
    Version:    House Prices - Advanced Regression Techniques
    VersionID:  a7793507-a30d-41d2-a5bc-670372398674
Parameters:
    batch_size:	200
    epochs:	350
Created:        Mon, 29 Mar 2021 19:07:44 UTC
Finished:       Mon, 29 Mar 2021 19:21:54 UTC
Status:         Succeeded
Error:          
Metrics:
    rmsle:	0.07545640264909739
```


## Acknowledgments

### Code
The code in here was adapted from https://www.kaggle.com/serigne/stacked-regressions-top-4-on-leaderboard. If you like it, please show support to the original Notebook's author by upvoting.

### Dataset
The Ames Housing dataset was compiled by Dean De Cock for use in data science education. It's an incredible alternative for data scientists looking for a modernized and expanded version of the often cited Boston Housing dataset. 
