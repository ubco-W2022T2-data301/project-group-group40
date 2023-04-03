import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_process(url_or_path_to_csv_file):
    
    # Load data and drop unused columns
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(['region'], axis=1)
    )
    
    # Clean data
    df = (
        df
        .dropna()
        .reset_index(drop=True)
    )
    
    # Process data
    df = (
        df
        .assign(is_smoker=df['smoker'].map({'yes': True, 'no': False}))
        .drop(['smoker'], axis=1)
        .assign(age_group=pd.cut(df['age'], bins=[0, 18, 35, 50, 65, 100], labels=['0-18', '18-35', '35-50', '50-65', '65+']))
    )
    
    # Restructure data format
    df = (
        df
        .melt(id_vars=['age', 'sex', 'bmi', 'is_smoker', 'age_group'], var_name='variable', value_name='value')
    )
    
    return df



def insurance_eda(dataframe):
    # Relationship between BMI and Charges by Sex, Smoker, and Region
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    axs = axs.flatten()
    sexes = dataframe["sex"].unique()
    smokers = dataframe["smoker"].unique()
    regions = dataframe["region"].unique()

    for i, sex in enumerate(sexes):
        for j, smoker in enumerate(smokers):
            for k, region in enumerate(regions):
                subset = dataframe[(dataframe["sex"] == sex) & (dataframe["smoker"] == smoker) & (dataframe["region"] == region)]
                sns.scatterplot(x="bmi", y="charges", hue="smoker", data=subset, ax=axs[i*2+j], alpha=0.5)
                axs[i*2+j].set_title(f"{sex}, {smoker}, {region}")
                axs[i*2+j].set_xlabel("BMI")
                axs[i*2+j].set_ylabel("Charges")

    fig.subplots_adjust(hspace=0.4, wspace=0.4)
    fig.suptitle("Relationship between BMI and Charges by Sex, Smoker, and Region", fontsize=14)
    plt.show()

    # Medical Expenses by BMI and Smoking Status
    sns.scatterplot(data=dataframe, x='bmi', y='charges', hue='smoker', alpha=0.5)
    plt.xlabel('BMI')
    plt.ylabel('Medical Expenses')
    plt.title('Medical Expenses by BMI and Smoking Status')
    plt.show()

    # Distribution of BMI by Smoking Status
    sns.histplot(data=dataframe, x='bmi', hue='smoker', multiple='stack')
    plt.title('Distribution of BMI by Smoking Status')
    plt.xlabel('BMI')
    plt.ylabel('Count')
    plt.show()

    # Correlation Matrix for Numerical Variables in Insurance Dataset
    numerical_cols = ["age", "bmi", "children", "charges"]
    corr_matrix = dataframe[numerical_cols].corr()
    sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu")
    plt.title("Correlation Matrix for Numerical Variables in Insurance Dataset")
    plt.show()

    # Trend of Charges over Age in the Medical Cost Dataset
    age_grouped = dataframe.groupby("age")["charges"].mean()
    plt.plot(age_grouped.index, age_grouped.values)
    plt.xlabel("Age")
    plt.ylabel("Mean Charges")
    plt.title("Trend of Charges over Age in the Medical Cost Dataset")
    plt.show()

