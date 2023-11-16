# 🍇 Wine_quality 🍷

## Intro: 

In our project, our primary objective is to conduct a comprehensive analysis of wine quality, focusing on its psychochemical properties. Since the taste and overall quality of wine are influenced by a complex interplay of various characteristics, we aim to delve into the intricate relationships among these chemical properties. By doing so, we aspire to enhance the production of high-quality wine and offer valuable insights to winemakers. Using data-driven methods, our goal is to design a predictive model for wine quality and uncovering the most important factor influencing the quality. Additionally, we seek to discern the distinctions between white and red wine, unraveling unique psychochemical profiles for each type.

The dataset was firstly introduced in the *Modeling wine preferences by data mining from physicochemical properties* by P. Cortez, A. Cerdeira, Fernando Almeida, Telmo Matos, J. Reis. 2009.* The authors used novel method *the sensitivity analysis* NN and SVM metchods to analyze wine quaity.

Project done as part of a LPI Data Science Course.

**Datasets** The dataset describes Red Wine (1599 data points) and White Wine (4898 data points) of *vinho verde*, product from the Minho (northwest) region of Portugal. The data were collected from May 2004 to February 2007 *(Cortez et al.,2020)*.

**Source of the datasets:** https://www.semanticscholar.org/paper/Modeling-wine-preferences-by-data-mining-from-Cortez-Cerdeira/bf15a0ccc14ac1deb5cea570c870389c16be019c 

## Examples to look at:
- [Neural Network](https://www.kaggle.com/code/andrecarneiroamaral/wine-quality-classification-neural-networks)
- [Cool Visualization](https://www.kaggle.com/code/qusaybtoush1990/wine-quality)
- [Outlier](https://www.kaggle.com/code/mohitgoyal522/wine-quality-data-analysis-and-prediction)


## Research Questions
### Statistics Outliers Detection:
1. Assess the homogeneity of wine qualities from different vineyards to determine if they follow a Gaussian distribution. Utilize QQ plots alongside other statistical tests forillustration.
2. Explore potential causes of outliers or variations, such as temperature and precipitation variations during the growing season.

### Predicting Performance:
1. Categorize wines into different quality tiers (e.g., low, medium, high) based on scores from wine experts. Utilize logistic regression and grid search, while also considering other machine learning algorithms such as Random Forest or Support Vector Machines for this analysis. 
2. Evaluate the model's ability to predict the quality of the wine accurately. Identify the main contributing factors to wine quality, and assess the significance and interaction of these factors. 
3. Offer insights on measures to avoid the production of poor-quality wine based on the identified factors from the predictive analysis. 
4. Determine the factors that most significantly distinguish the best wines from others. Discuss the application of the t-test in examining the statistical significance of these distinguishing factors.


### Clustering:
1. Explore different compositions and characteristics of high-rated white/red wines to determine if variations such as sweet and dry wines exist, and whether their composition differs significantly.
2. Apply K-means clustering and consider comparing with other clustering algorithms. Utilize heat maps alongside other visualization techniques like dendrograms for a comprehensive visual representation.


### Comments 13.11
- Add information when did they collect the date?
- outiers - normalization,  
- top quality modeling -  see if our features make sense - more like associations, not predictors
- the graphs should have a big font (with the name according to what we can see)

- while presentiong the plot - comment the plot (what is important, what is not so important - precise description)