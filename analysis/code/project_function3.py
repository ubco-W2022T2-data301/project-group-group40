import pandas as pd

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
