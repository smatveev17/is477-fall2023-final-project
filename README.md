# Analysis of UCI Wine Data (IS477)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10268872.svg)](https://doi.org/10.5281/zenodo.10268872)

## Overview
In this project, we perform an analysis on the Wine data set from th UCI Machine Learning archive. This dataset uses chemical analysis to differentiate between wines that were made in the same region within Italy. This dataset looks at 13 different features that make up each wine, and the quantity of each feature present in them. Each wine is sorted into one of 3 classes. The classes do not have a name provided in the original dataset so they are referenced as class 1,2,3 in this study.

In this repository, there are descriptive statistics (standard deviation, mean, count, etc.) of the data in UCI Wine Data. Additionally, the dataset is used to perform a logistic regression on the relationship between a wine's class and the quantity of each of the 13 features in that wine. The regression model was performed on training data split from the original dataset, and accuracy of its predictions were found using testing data from that split. There is also a scatterplot displaying the relationship of the classification of a wine based on the amount of alcohol and color intensity in them. We were able to achieve a high accuracy of .97 and a weighted precision of .97 for the three classes. 
![Screensot of workflow generated by snakefile](results/wine_classification_plot.pdf)

## Contributions
Nora Duffy completed the README, snakefile, workflow visualization, profile.py and requirements.txt.

Sasha Matveev implemented the licenses for this repository, the snakefile, zenodo.json, analysis.py and the prepare_data.py.

## Analysis
In the analysis described above, the test/train split on the logistic regression displayed 97% overall accuracy, meaning that 97% of wines were classified correctly based on their makeup. The F-1 scores, which describes the average of precision (an instance predicted to be a certain class is actually that class) and recall ( or true positive rate, meaning the ratio of correctly predicted positive observations to all observations in the class) were .96, .97 and 1.00 for class 1, 2 and 3 respectively.  


## Workflow
![Screensot of workflow generated by snakefile](workflow_1.PNG)

## Reproducing 
To reproduce the workflow, use the run_all step in the snakefile through the docker image provided 

```bash
docker run --rm -v %cd%:/is477 matveev2/is477-fall2023-final-project:v1 snakemake --cores 1 run_all
```

Running this with the is477-fall2023-final-project:v1 image from dockerhub will read in the dataset from the UCI website and unzip into the data folder if it is not there already, produce a profiling.html file that gives and overview of the data using the ydata package, as well as a graph of logistic regression results, a csv with summary statistics, and a classification report that contains metrics like precision, f-1, recall, and support. You can also run each step individualy:

```bash
docker run --rm -v %cd%:/is477 matveev2/is477-fall2023-final-project:v1 snakemake --cores 1 prepare
```
```bash
docker run --rm -v %cd%:/is477 matveev2/is477-fall2023-final-project:v1 snakemake --cores 1 profile
```
```bash
docker run --rm -v %cd%:/is477 matveev2/is477-fall2023-final-project:v1 snakemake --cores 1 analyze
```

## License
### Software
The software provided in this repository is open source (permissive MIT) license. Since the purpose of this repository is scientific and academic in nature, having a proprietary or hybrid software license would be counterproductive. Any restrictions on copying, redistributing or modifying the license would not only go against the principles of a reproducibility study, it would also needlessly complicate further studies as it would be tough to verify the results of our study which uses open-source data and proprietary software. 
### Data
The data license for this repository is Creative Commons Attribution 4.0. This means that the data license is compatible with our open source license for software and can be used freely for content and data with attribution and no share-alike license strings. Although we are using the UCI Wine dataset which is distributed under the same license and does not require us to use the same license in our redistribution, we believe it is appropriate to reuse the original license as we do not own the data and cannot dedicate it to the public domain with something like a Creative Commons CCZero or Open Data Commons Public domain license. The data will be attributed to the original creators of the UCI Wine dataset, Aeberhard,Stefan and Forina,M.. (1991). Wine. UCI Machine Learning Repository. https://doi.org/10.24432/C5PC7J.

## References
Aeberhard,Stefan and Forina,M.. (1991). Wine. UCI Machine Learning Repository. https://doi.org/10.24432/C5PC7J.