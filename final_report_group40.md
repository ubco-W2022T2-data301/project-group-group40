## Introduction
Our group decided to investigate the factors contributing to high medical costs in the United States. We were particularly interested in understanding how medical expenditures were distributed across different regions and genders, whether having children was a factor, and how body mass index (BMI) and smoking status were related to medical expenses.

## Exploratory Data Analysis
During our exploratory data analysis, we examined the distribution of medical expenses, age, gender, region, and BMI. We also looked for any potential outliers or missing values in our dataset.

One of the key findings from our EDA was that medical expenses were heavily skewed to the right, indicating that a small percentage of individuals had much higher medical costs than the rest of the population. We also observed that BMI was positively correlated with medical expenses, which was not surprising given that individuals with higher BMI tend to have more health issues.

### Question 1: Is there a link between smoking behaviours and medical costs, and does it differ by area and gender in the United States?

To answer this question, we created a series of scatterplots to examine the relationship between medical expenses, region,gender and smoking. We found that smoking is more widespread among men and those living in the Southeast.Morover,the overall charges for nonsmokers are significantly cheaper than for smokers, regardless of gender. This emphasises the importance of smoking cessation and preventive initiatives in reducing the burden of medical expenditures, particularly for smokers.You can check out the in depht analysis of this question in the [jupyter file](/analysis/analysis%202.ipynb).

![Number of Smokers by Region and Gender](/images/project%201.png)

I used a pivot table in the first code to determine total medical expenses by gender and smoking status. Then I made a stacked bar chart to compare the total costs of male and female smokers and non-smokers. The purple bars reflect non-smokers' charges, whereas the orange bars represent smokers' charges. According to the graph, smokers have greater medical expenditures than nonsmokers. Furthermore, male smokers have higher medical expenditures than female smokers.

![Total Medical Charges by Sex and Smoker Status](/images/project%202.png)

I used seaborn to construct a bar chart that shows the number of smokers by location and gender in the second code. The pink bars indicate the number of female smokers, whereas the blue bars indicate the number of male smokers. The graphic reveals that the southeast area has the most smokers, while male smokers outnumber female smokers in all regions.



### Question 2: Are children one of the underlying factors contributing to the high costs of healthcare in the United States?
To answer this topic, I used a range of powerful tools, including joint plots, cluster maps, and pivot tables. My primary focus was on evaluating the relationships between key variables such as children, age, gender, region, and charges.

My findings demonstrated a striking link between the number of children in a household and medical expenses, with costs often rising as the family size expands. However, if a family has four or five children, this trend begins to level off, indicating a saturation threshold. Age and location were also identified as key factors influencing medical spending. Surprisingly, males with 3-4 children had higher medical costs than females, but families with more children had a higher median age. This question's in-depth examination may be found [notbook](/analysis/analysis1.ipynb). 


![jointplot](/images/jointplot.png)

According to the graph, the number of children has a positive relationship with healthcare costs, particularly for adults aged 20 to 40. The relationship between healthcare expenditures and the number of children may also decline as people age. Furthermore, we can see that healthcare costs climb as people age, especially for those with three or four children.

![pivottable](/images/pivottable.png)

The graph shows that the number of children has a positive relationship with the average cost of healthcare. Individuals with more children paid more for healthcare across all regions, albeit this decreases after 4-5 children. Similarly, the Southeast has the highest average charges, followed by the Northeast, Southwest, and Northwest.


### **Question 3: What is the relationship between body mass index (BMI) and smoking status and their impact on an individual's medical expenses in the United States?**
To answer this question, I created a series of scatterplots and histograms to examine the relationship between BMI, smoking status, and medical expenses. You can check out my in depth analysis of this question in this [jupyter file](/analysis/analysis3.ipynb). I found that smokers tended to have much higher medical expenses than non-smokers, and that this effect was even more pronounced for individuals with higher BMI. These are few of the visualization I created which will give you an idea of how BMI and smoking status impact an individual's medical expenses in United States



![Relationship between BMI and Charges by Sex, Smoker, and Region](/images/relationship_bw_bmi_charges.png)

The chart displays the relationship between BMI and medical charges, and it indicates that as BMI increases, medical charges also tend to increase. However, this relationship is not consistent across all subgroups. For non-smokers, the correlation between BMI and medical charges is weaker compared to smokers, which suggests that smoking status is an important factor to consider when examining this relationship. Moreover, the graph shows that regional differences may also play a role, as the association between BMI and medical charges appears to be stronger in the southeast region compared to the northeast region, particularly for female smokers.

![Distribution of BMI by smoking status](/images/distribution_of_bmi_by_smoking_status.png)

This graph is a stacked histogram that compares the distribution of BMI for smokers and non-smokers in the dataset. The x-axis displays the BMI values, while the y-axis shows the count of individuals falling in each BMI bin. The graph suggests that non-smokers have a relatively higher proportion of individuals within the healthy BMI range, whereas smokers have a larger proportion of individuals in the overweight and obese BMI range. This finding suggests that smoking status may have an impact on BMI and that smokers may be at higher risk for overweight or obesity.

![Trend of Charges over Age in the Medical Cost Dataset](/images/trend_of_charges_over_age.png)

The above line graph displays the trend of average medical charges with respect to age. The x-axis represents age, while the y-axis shows the average medical charges. The graph indicates that medical charges increase with age, with a gradual incline until around age 60, after which the increase becomes steeper. This observation suggests that older individuals may have higher medical costs, possibly due to age-related health conditions.


## **Summary/Conclusion**
Overall, our analysis suggests that factors such as gender, region, smoking status, and BMI are all important contributors to the high costs of healthcare in the United States. While having more children may be a factor, It does vary depending on the number of children you have. Our findings underscore the importance of promoting healthy behaviors such as not smoking and maintaining a healthy BMI in order to reduce healthcare costs and improve overall health outcomes.Overall, our analysis show that smoking habits lead to greater medical expenses, and that this association varies by gender and region in the United States. When we study and predict medical expenditures, these aspects must be taken into account.

