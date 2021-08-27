## Introduction

This sample pipeline uses some advanced ensemble techniques to stack a wide variety of models. If you are not curious about the ensemble techniques, please go straight to the next section. Otherwise, read on!

The features engineering is rather parsimonious (at least compared to some others great scripts). It is pretty much:
- Imputing missing values by proceeding sequentially through the data
- Transforming some numerical variables that seem really categorical
- Label Encoding some categorical variables that may contain information in their ordering set
- Box Cox Transformation of skewed features (instead of log-transformation) : This gave a slightly better result both on leaderboard and cross-validation.
- Getting dummy variables for categorical features.

Then we choose many base models (mostly sklearn based models + sklearn API of DMLC's XGBoost and LightGBM), cross-validate them on the data before stacking/ensembling them. The key here is to make the (linear) models robust to outliers. This improved the result both on LB and cross-validation.


## Quickstart instruction

### Prerequisites:
Three things are needed in this sample:
- An installation of the `same` command - [a CLI to work with SAME programs](https://github.com/azure-octo/same-cli),
- A working [Kubeflow](https://kubeflow.org) installation in a [Kubernetes](https://k8s.io) cluster, and
- A SAME program definition file `same.yaml` together with all the files it refers.


#### Install `same`
To download and install the `same` command,
```bash
curl -L0 https://get.sameproject.org/ | bash -
```
For more information, check out the [repo](https://github.com/azure-octo/same-cli).

#### Install [Kubeflow](https://kubeflow.org)
Installing Kubeflow on Kubernetes in a generic manner is difficult. However, if your local platform is AMD64 on Mac/Linux the `same` command provides a simple helper to install Kubeflow on K3s for you:

```bash
same installK3s
```

If that doesn't work for you, try following the instruction [here](https://www.kubeflow.org/docs/components/pipelines/installation/localcluster-deployment/) to install Kubeflow on your a local Kubernetes cluster of your choice (KinD, k3s, k3d, minikube, etc...).

#### Get a SAME program definition file
Clone this repository and go to the `houseprice` directory.
```bash
cd houseprice

# Inspect the SAME program definition with your favorite editor
emacs same.yaml
```

For the rest of the instructions, please stay in the `houseprice` directory. If you choose not to, you will need to supply a `--config` option the commands to point to the correct location of the `same.yaml` file.

Now, all the prerequisites are checked. Let's start using SAME.

> **PRO TIP**: You can run `same program run --help`, `same run list --help`, or `same run describe --help` to explore a full list of options for each of those commands.

### Step 1: Run your SAME program

Go to the `houseprice` directory and run the following command:
```bash
same program run --run-name demo --experiment-name demo 
```
That will trigger a SAME program run on your local Kubeflow cluster. Congratulations!

### Step 2: View the result of your SAME program using Kubeflow UI
To view the result, first open a tunnel to the Kubeflow UI
```bash
kubectl port-forward svc/ml-pipeline-ui 8080:80
```
Following that, open a browser and go to http://localhost:8080 to see the Kubeflow UI. Go tho the Experiment `demo` and find your SAME run named `demo`.

### Step 3: Inspect your SAME program using the CLI

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
The code in here was adapted from https://www.kaggle.com/serigne/stacked-regressions-top-4-on-leaderboard. If you like it, please show support to the original Notebook's author by following that link to upvote.

### Dataset
The Ames Housing dataset was compiled by Dean De Cock for use in data science education. It's an incredible alternative for data scientists looking for a modernized and expanded version of the often cited Boston Housing dataset. 
