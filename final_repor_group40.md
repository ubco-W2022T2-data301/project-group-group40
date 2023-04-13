## Introduction
Our group decided to investigate the factors contributing to high medical costs in the United States. We were particularly interested in understanding how medical expenditures were distributed across different regions and genders, whether having children was a factor, and how body mass index (BMI) and smoking status were related to medical expenses.

## Exploratory Data Analysis
During our exploratory data analysis, we examined the distribution of medical expenses, age, gender, region, and BMI. We also looked for any potential outliers or missing values in our dataset.

One of the key findings from our EDA was that medical expenses were heavily skewed to the right, indicating that a small percentage of individuals had much higher medical costs than the rest of the population. We also observed that BMI was positively correlated with medical expenses, which was not surprising given that individuals with higher BMI tend to have more health issues.

### Question 1: How are medical expenditures distributed across various regions and genders?
To answer this question, we created a series of scatterplots to examine the relationship between medical expenses, region, and gender. We found that medical expenses were generally higher for males than females, and that the Southeast region had the highest medical expenses overall.

### Question 2: Are children one of the underlying factors contributing to the high costs of healthcare in the United States?
To explore this question, we grouped individuals by the number of children they had and examined the distribution of medical expenses within each group. We found that individuals with more children tended to have slightly higher medical expenses than those with fewer children. However, this difference was relatively small and likely not a significant factor in the overall high costs of healthcare in the United States.

### Question 3: What is the relationship between body mass index (BMI) and smoking status and their impact on an individual's medical expenses in the United States?
To answer this question, we created a series of scatterplots and histograms to examine the relationship between BMI, smoking status, and medical expenses. We found that smokers tended to have much higher medical expenses than non-smokers, and that this effect was even more pronounced for individuals with higher BMI.

## Summary/Conclusion
Overall, our analysis suggests that factors such as gender, region, smoking status, and BMI are all important contributors to the high costs of healthcare in the United States. While having more children may be a factor, it is likely not a major contributor. Our findings underscore the importance of promoting healthy behaviors such as not smoking and maintaining a healthy BMI in order to reduce healthcare costs and improve overall health outcomes.


### Question 1: How are medical expenditures distributed across various regions and genders?
I produced two visualisations to investigate how medical costs differ by area and gender.

The first visualisation is a box plot that illustrates the distribution of medical expenses by gender for each location. Males are represented by the colour green, while females are represented by the colour red. The four zones are represented by the x-axis, while the charges are represented by the y-axis. The plot's title is "Medical spending costs by region divided by sex." According to the results of this visualization, there are considerable disparities in medical expenditures between regions and genders, with the southeast area having the greatest medical expenditures for both males and girls.
The second visualisation is a heatmap of average medical costs by area and gender. The colour intensity indicates the average charge, with deeper colours representing larger charges. Gender is shown on the x-axis, while the four areas are represented on the y-axis. "Average Medical Charges by Region and Gender" is the plot's title. According to the statistics, males have greater medical costs than females in general, and the southeast area has the highest medical expenses for both genders.



### Question 2: Is there a link between smoking behaviours and medical costs, and does it differ by area and gender in the United States?
I used Python to generate data visualisations to investigate this link.

I used a pivot table in the first code to determine total medical expenses by gender and smoking status. Then I made a stacked bar chart to compare the total costs of male and female smokers and non-smokers. The purple bars reflect non-smokers' charges, whereas the orange bars represent smokers' charges. According to the graph, smokers have greater medical expenditures than nonsmokers. Furthermore, male smokers have higher medical expenditures than female smokers.

I used seaborn to construct a bar chart that shows the number of smokers by location and gender in the second code. The pink bars indicate the number of female smokers, whereas the blue bars indicate the number of male smokers. The graphic reveals that the southeast area has the most smokers, while male smokers outnumber female smokers in all regions.

Overall, this data show that smoking habits are due to greater medical expenses, and that this association varies by gender and region in the United States. When we study and predict medical expenditures, these aspects must be taken into account.



### Question 3: Is there a relationship between BMI (Body Mass Index) and medical costs, and how does it vary across different regions and genders?
After analysing the data with Python and the seaborn library, I discovered a link between BMI and medical expenses that varied by gender and area. I was able to visualise this link and acquire some insights by using violin plots and linear regression graphs.

Individuals with a BMI greater than 30 had higher medical costs than those with a BMI between 18.5 and 25 based on the violin plots. Surprisingly, the distribution of medical expenses for people with BMIs between 25 and 30 was rather comparable.

I was able to better appreciate the nature of the association between BMI and medical expenditures thanks to the linear regression charts. There was a definite positive link between these two parameters, implying that as BMI climbed, so did medical expenses. This was true for all areas and genders.

When I examined the slope of the linear regression line for each location and gender, I discovered that males in the southwest region had a higher slope than other regions and genders. This meant that the link between BMI and medical expenditures was higher for men in the southwest.

Overall, our findings emphasise the necessity of taking gender and location into account when analysing and forecasting medical expenses. It is critical to recognise that the association between BMI and medical expenditures might vary based on these factors, and that any study must account for them.

## Summary/Conclusion
I was able to establish a link between smoking habits and BMI with medical expenses in the United States by using Python and data visualisation techniques such as box plots, heatmaps, stacked bar charts, violin plots, and linear regression graphs. I discovered that smoking and having a high BMI were connected to increased medical costs, and that this connection varied by gender and area. My findings emphasise the need of taking these factors into account when researching and estimating medical expenditures.
