# 🍇 Unveiling the Secrets of Wine Quality 🍷

> Bypassing traditional tasting methods, this project employs data analysis to predict the quality of wine based on its chemical features.

In our project, our primary objective is to conduct a comprehensive analysis of wine quality, focusing on its psychochemical properties. Since the taste and overall quality of wine are influenced by a complex interplay of various characteristics, we aim to delve into the intricate relationships among these chemical properties. By doing so, we aspire to enhance the production of high-quality wine and offer valuable insights to winemakers. Using data-driven methods, our goal is to design a predictive model for wine quality and uncovering the most important factor influencing the quality. Additionally, we seek to discern the distinctions between white and red wine, unraveling unique psychochemical profiles for each type.

Project done as part of a LPI Data Science Course.


## 🍷 1. Introduction

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
- **Limitation**:
  - Lack of Temporal Information:
    - We are unable to analyze variations in wine quality across different years, also making it impossible for us to identify the relationship between weather conditions and wine quality.
  - Lack of Brand and Public Preference Data: 
    - We are unable to establish a direct link between wine quality attributes and consumer preferences or sales performance. 

#### 1.3.1 Chemical Features:
🧪 Data recorded by iLab, a computerized system managing wine sample testing.

1. **Fixed Acidity (g/dm³)**: 
   - *Role in Production*: Represents the total concentration of acids.
   - *Impact on Taste and Quality*: Influences freshness, crispness, and aging potential.
2. **Volatile Acidity (g/dm³)**: 
   - *Role in Production*: Includes vaporizing acids; can contribute to complexity in moderation.
   - *Impact on Taste and Quality*: High levels can result in a vinegar-like taste.
3. **Citric Acid (g/dm³)**: 
   - *Role in Production*: Enhances freshness and fruitiness.
   - *Impact on Taste and Quality*: Adds a citrusy character and contributes to acidity.
4. **Residual Sugar (g/dm³)**: 
   - *Role in Production*: Determines sweetness level after fermentation.
   - *Impact on Taste and Quality*: Influences perceived sweetness; higher levels result in a sweeter wine.
5. **Chlorides (g/dm³)**: 
   - *Role in Production*: Salts influencing flavor and microbial stability.
   - *Impact on Taste and Quality*: Moderate levels contribute to structure; high levels may lead to a salty taste.
6. **Free Sulfur Dioxide (mg/dm³)**: 
   - *Role in Production*: Exists in equilibrium between molecular SO2 and bisulfite ion; prevents microbial growth and wine oxidation.
   - *Impact on Taste and Quality*: Maintains freshness, but excessive levels can result in a sulfurous aroma.
7. **Total Sulfur Dioxide (mg/dm³)**: 
   - *Role in Production*: Includes both free and bound forms; measures overall sulfite content.
   - *Impact on Taste and Quality*: Crucial for preservation; excessive levels can affect the wine's quality.
8. **Density (g/cm³)**: 
   - *Role in Production*: Indicates mass per unit volume; related to sugar and alcohol concentration.
   - *Impact on Taste and Quality*: Influences body and mouthfeel; higher density contributes to a fuller-bodied wine.
9. **pH**: 
   - *Role in Production*: Measures acidity or alkalinity; influences stability and chemical reactions.
   - *Impact on Taste and Quality*: Affects color, flavor, and microbial stability; balanced pH is essential.
10. **Sulphates (g/dm³)**: 
    - *Role in Production*: Added as sulfur dioxide; acts as an antioxidant and antimicrobial agent.
    - *Impact on Taste and Quality*: Proper use preserves freshness; too high level can lead to undesirable flavors.
11. **Alcohol (% by Volume)**: 
    - *Role in Production*: Byproduct of fermentation; contributes to body, mouthfeel, and structure.
    - *Impact on Taste and Quality*: Influences warmth, body, and balance; well-integrated alcohol is crucial for a harmonious taste.

#### 1.3.2 Potential Connections and Relationships:

- **Acidity and pH:**
  - *Connection:* The relationship between fixed acidity and pH is critical. Higher fixed acidity tends to lower the pH, influencing the wine's color, stability, and microbial environment.

- **Sugar and Alcohol:**
  - *Connection:* The level of residual sugar at the end of fermentation affects the final alcohol content. Balancing these elements is crucial for achieving the desired sweetness and alcohol levels.

- **Sulfur Dioxide and Volatile Acidity:**
  - *Connection:* Proper use of sulfur dioxide can help control volatile acidity, preventing the development of unwanted vinegar-like flavors.

- **Chlorides and Total Sulfur Dioxide:**
  - *Connection:* The balance between chlorides and total sulfur dioxide contributes to the wine's structure and preservation. Monitoring both helps avoid undesirable tastes.


## 2. Research Questions and Motivations

### 2.1 Research Questions
Our reserach questions enhances and expands upon prior studies by:

- 🍇 Which features contribute the most to predict good and poor quality of wine?
- 🍇 What is the recipe for a good and poor wine? 

### 2.2 Motivations:

- 🇫🇷 **Cultural Significance**: Studying in France, a nation celebrated for its wine tradition, we seek to deepen our understanding of wine. This analysisfosters a greater appreciation of this heritage.
- 🍾 **Enhancing Wine Production:** Providing actionable insights for quality improvement through advanced statistical and machine learning techniques.
- 📊 **Analytical Depth:** Leveraging data-driven methods to explore wine quality nuances. This exploration will enhance our analytical skills while shedding light on hidden characteristics within wines.

## 3. Data Analysis

### 3.1 📊 Statistical Analysis

- **Skewness Detection**: Utilizing Quantile-Quantile (QQ) plots, we analyze the distribution of wine qualities. Where skewness is evident, we apply logarithmic transformations to normalize the data.
- **Outliers Detection**: We employ boxplots and Z-score calculations (with a threshold of 6) to pinpoint outliers. This helps in understanding and addressing anomalies in the dataset.

### 3.2 🛠️ Model Building
- **Feature Selection**: Through cluster maps and correlation matrices, we explore the relationships between various features and wine quality. To avoid multicollinearity, we carefully select only one feature from groups of highly correlated attributes.
- **Predictive Modeling**: Noticing a distinct trend in wine alcohol level (quality 3-5 and 6-9), we employ piecewise linear regression. This method categorizes wines into quality tiers while assessing the impact of different factors on wine quality.
 
![Box Plots for White Wine Without Outliers](figures/2_Boxplots_without_outliers/Box%20Plots%20for%20White%20Wine%20(Without%20Outliers).png)
*Wine alcohol level differs in the group of quality 3-5 and 6-9.*

### 3.3 🥂 Project Outcomes
- **Quality Prediction**: Our models are designed to accurately forecast wine quality, highlighting the key factors that contribute to producing high-quality wines.
- **Recipe Derivation**: By analyzing the coefficients of significant features in our model, we derive ranges for these key attributes, effectively creating 'recipes' for high-quality wines.

## 4. 🚀 Future Directions and Limitations

- **Subgroup Analysis via K-Means**: The QQ plot revealed a significant subgroup in chlorides. Implementing K-means clustering could further refine our understanding of such subgroups.
![ ](figures/3_QQ_plots_log_corrected/QQ%20Plots%20for%20White%20Wine(Second%20Log).png)
- **Enhanced Feature Selection**: Future work could explore alternative methods like Principal Component Analysis (PCA) for more robust feature selection.
- **Model Diversification**: Comparing multiple models could provide a more comprehensive understanding of the factors influencing wine quality.
- **Dataset Expansion**: To improve generalizability, incorporating additional data like weather conditions, vintage year, and regional specifics could offer a more holistic analysis of wine quality.
