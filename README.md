# 🍇 Unveiling the Secrets of Wine Quality 🍷
Bypassing traditional tasting methods, this project employs data analysis to predict the quality of wine based on its chemical features.

## Intro: 

## 🍷 1. Introduction about the Data Set

### 📖 1.1 General Information:
- **Provided by**: [The UCI Machine Learning Repository](http://archive.ics.uci.edu/dataset/109/wine).
- **Donated by**: Paulo Cortez, Antonio Cerdeira, Fernando Almeida, Telmo Matos, and Jose Reis.
   - 📜 **Their paper**: [Modeling wine preferences by data mining from physicochemical properties](https://repositorium.sdum.uminho.pt/bitstream/1822/10029/1/wine5.pdf).
   - 🧐 **Main idea**: Using data mining to understand how various factors influence wine quality, offering insights into wine production and certification. 
   - ⚒️ **Approach**: Support Vector Machines (SVM), Neural Networks (NN), and Multiple Regression (MR) techniques.
   - 🧰 **Conclusion**: 
     - For assessing wine quality, the Support Vector Machine (SVM) method outperforms other techniques in accuracy, especially for white wines.
     - Alcohol level is a key factor in determining wine quality. Citric acid and residual sugar are more significant in white wines, whereas sulphates are highly important in both types.

### 🍇 1.2 Info about the Wine:
- **Types**: Both white and red wines from the Vinho Verde region in northwestern Portugal 🇵🇹.
- **Production**: Represents 15% of Portuguese production.

### 📊 1.3 Info about the Datasets:
- **Wines**: 1599 red and 4898 white samples.
- **Collection**:
   - ⏳ Timeframe: May 2004 to February 2007.
   - 🏷️ Type: Only protected designation of origin samples by CVRVV (Comissão de Viticultura da Região dos Vinhos Verdes), focused on enhancing the quality and marketing of vinho verde.
- **Quality Assessment**:
   - Rated by at least three sensory assessors (blind tastes), on a 0 (very bad) to 10 (excellent) scale. The final score is the median of these ratings.
- **Chemical Features Tested**:
   - 🧪 Data recorded by iLab, a computerized system managing wine sample testing.
   - Tests include density, alcohol, pH values, etc.
- **Limitation**:
  - Lack of Temporal Information:
    - We are unable to analyze variations in wine quality across different years, also making it impossible for us to identify the relationship between weather conditions and wine quality.
  - Lack of Brand and Public Preference Data: 
    - We are unable to establish a direct link between wine quality attributes and consumer preferences or sales performance. 

In our project, our primary objective is to conduct a comprehensive analysis of wine quality, focusing on its psychochemical properties. Since the taste and overall quality of wine are influenced by a complex interplay of various characteristics, we aim to delve into the intricate relationships among these chemical properties. By doing so, we aspire to enhance the production of high-quality wine and offer valuable insights to winemakers. Using data-driven methods, our goal is to design a predictive model for wine quality and uncovering the most important factor influencing the quality. Additionally, we seek to discern the distinctions between white and red wine, unraveling unique psychochemical profiles for each type.

The dataset was firstly introduced in the *Modeling wine preferences by data mining from physicochemical properties* by P. Cortez, A. Cerdeira, Fernando Almeida, Telmo Matos, J. Reis. 2009.* The authors used novel method *the sensitivity analysis* NN and SVM metchods to analyze wine quaity.

Project done as part of a LPI Data Science Course.

**Source of the datasets:** https://www.semanticscholar.org/paper/Modeling-wine-preferences-by-data-mining-from-Cortez-Cerdeira/bf15a0ccc14ac1deb5cea570c870389c16be019c 

## 2. Research Questions and Motivations

### 2.1 Research Questions
Our reserach questions enhances and expands upon prior studies by:

- 🍇Which features contribute the most to predict good and poor quality of wine?
- 🍇What is the recipe for a good and poor wine? 


### 2.2 Motivations:
- 🍇 **Cultural Significance**: Residing in France, a nation celebrated for its wine tradition, we seek to deepen our understanding of wine. This analysisfosters a greater appreciation of this heritage.
- 🍾 **Enhancing Wine Production:** Providing actionable insights for quality improvement through advanced statistical and machine learning techniques.
- 📊 **Analytical Depth:** Leveraging data-driven methods to explore wine quality nuances. This exploration will enhance our analytical skills while shedding light on hidden characteristics within wines.

## Examples to look at:
- [Neural Network](https://www.kaggle.com/code/andrecarneiroamaral/wine-quality-classification-neural-networks)
- [Cool Visualization](https://www.kaggle.com/code/qusaybtoush1990/wine-quality)
- [Outlier](https://www.kaggle.com/code/mohitgoyal522/wine-quality-data-analysis-and-prediction)

**Datasets** The dataset describes Red Wine (1599 data points) and White Wine (4898 data points) of *vinho verde*, product from the Minho (northwest) region of Portugal. The data were collected from May 2004 to February 2007 *(Cortez et al.,2020)*.

**Dataset Features:**
1. **Fixed Acidity (g/dm³):**
   - *Role in Production:* Represents the total concentration of acids.
   - *Impact on Taste and Quality:* Influences freshness, crispness, and aging potential.

2. **Volatile Acidity (g/dm³):**
   - *Role in Production:* Includes vaporizing acids; can contribute to complexity in moderation.
   - *Impact on Taste and Quality:* High levels can result in a vinegar-like taste.

3. **Citric Acid (g/dm³):**
   - *Role in Production:* Enhances freshness and fruitiness.
   - *Impact on Taste and Quality:* Adds a citrusy character and contributes to acidity.

4. **Residual Sugar (g/dm³):**
   - *Role in Production:* Determines sweetness level after fermentation.
   - *Impact on Taste and Quality:* Influences perceived sweetness; higher levels result in a sweeter wine.

5. **Chlorides (g/dm³):**
   - *Role in Production:* Salts influencing flavor and microbial stability.
   - *Impact on Taste and Quality:* Moderate levels contribute to structure; high levels may lead to a salty taste.

6. **Free Sulfur Dioxide (mg/dm³):**
   - *Role in Production:* Exists in equilibrium between molecular SO2 and bisulfite ion; prevents microbial growth and wine oxidation.
   - *Impact on Taste and Quality:* Maintains freshness, but excessive levels can result in a sulfurous aroma.

7. **Total Sulfur Dioxide (mg/dm³):**
   - *Role in Production:* Includes both free and bound forms; measures overall sulfite content.
   - *Impact on Taste and Quality:* Crucial for preservation; excessive levels can affect the wine's quality. Concentrations over 50 ppm may become evident in the nose and taste of wine.

8. **Density (g/cm³):**
   - *Role in Production:* Indicates mass per unit volume; related to sugar and alcohol concentration.
   - *Impact on Taste and Quality:* Influences body and mouthfeel; higher density contributes to a fuller-bodied wine.

9. **pH:**
   - *Role in Production:* Measures acidity or alkalinity; influences stability and chemical reactions.
   - *Impact on Taste and Quality:* Affects color, flavor, and microbial stability; balanced pH is essential.

10. **Sulphates (g/dm³):**
    - *Role in Production:* Added as sulfur dioxide; acts as an antioxidant and antimicrobial agent.
    - *Impact on Taste and Quality:* Proper use preserves freshness; too high level can lead to undesirable flavors.

11. **Alcohol (% by Volume):**
    - *Role in Production:* Byproduct of fermentation; contributes to body, mouthfeel, and structure.
    - *Impact on Taste and Quality:* Influences warmth, body, and balance; well-integrated alcohol is crucial for a harmonious taste.

## Potential Connections and Relationships:

- **Acidity and pH:**
  - *Connection:* The relationship between fixed acidity and pH is critical. Higher fixed acidity tends to lower the pH, influencing the wine's color, stability, and microbial environment.

- **Sugar and Alcohol:**
  - *Connection:* The level of residual sugar at the end of fermentation affects the final alcohol content. Balancing these elements is crucial for achieving the desired sweetness and alcohol levels.

- **Sulfur Dioxide and Volatile Acidity:**
  - *Connection:* Proper use of sulfur dioxide can help control volatile acidity, preventing the development of unwanted vinegar-like flavors.

- **Chlorides and Total Sulfur Dioxide:**
  - *Connection:* The balance between chlorides and total sulfur dioxide contributes to the wine's structure and preservation. Monitoring both helps avoid undesirable tastes.

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


### Resources: 
- Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Modeling wine preferences by data mining from physicochemical properties. Decision support systems, 47(4), 547-553.
- https://rpubs.com/Hernando23/330833