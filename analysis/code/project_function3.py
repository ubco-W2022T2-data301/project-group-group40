import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd

def load_and_process(url_or_path_to_csv_file):
    
    # Method chain 1: Load data and drop unused columns
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(['charges'], axis=1)
    )
    
    # Method chain 2: Clean data
    df = (
        df
        .dropna()
        .reset_index(drop=True)
        .assign(age=lambda x: round(x['age'])) # advanced operation 1: round age to nearest integer
    )
    
    # Method chain 3: Process data
    df = (
        df
        .assign(is_smoker=df['smoker'].map({'yes': True, 'no': False})) # advanced operation 2: map smoker column to boolean
        .drop(['smoker'], axis=1)
        .assign(age_group=pd.cut(df['age'], bins=[0, 18, 35, 50, 65, 100], labels=['0-18', '18-35', '35-50', '50-65', '65+']))
        .assign(bmi_category=lambda x: pd.cut(x['bmi'], bins=[0, 18.5, 25, 30, 100], labels=['underweight', 'normal', 'overweight', 'obese'])) # advanced operation 3: categorize BMI
    )
    
    # Method chain 4: Restructure data format
    df = (
        df
        .melt(id_vars=['age', 'sex', 'bmi', 'is_smoker', 'age_group', 'bmi_category'], var_name='variable', value_name='value')
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

def add_age_and_bmi_categories(df):
    age_bins = [0, 18, 30, 45, 60, 100]
    age_labels = ['<18', '18-30', '30-45', '45-60', '60+']
    df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

    bmi_bins = [0, 18.5, 25, 30, 100]
    bmi_labels = ['underweight', 'normal', 'overweight', 'obese']
    df['bmi_category'] = pd.cut(df['bmi'], bins=bmi_bins, labels=bmi_labels)
    
    return df


def data_wrangling(dataframe):
    region_coords = {"northeast": (42.246163,-73.856465), 
                     "northwest": (47.037874,-121.695988), 
                     "southeast": (31.243618,-84.256385), 
                     "southwest": (34.739734,-106.693466)}
    dataframe["latitude"] = dataframe["region"].apply(lambda x: region_coords[x][0])
    dataframe["longitude"] = dataframe["region"].apply(lambda x: region_coords[x][1])
    dataframe["smoking_status"] = dataframe["smoker"].apply(lambda x: True if x == "yes" else False)
    dataframe.to_csv("processed_medicalCost_AbhinavMalik.csv", index=False)

