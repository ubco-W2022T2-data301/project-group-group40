import pandas as pd

def load_data(url):
    
    # loaded the data and dealt with the missing data in method chain 1.
    
    df = (
        pd.read_csv(url)
        .drop_duplicates()
        .dropna()
    )

    # Created new column, dropped others, did processing and data warngling in the second method chain 
    
    region_sex_map = {
        ('yes', 'northwest', 'male'): 'M-NW',
        ('yes', 'northwest', 'female'): 'F-NW',
        ('yes', 'northeast', 'male'): 'M-NE',
        ('yes', 'northeast', 'female'): 'F-NE',
        ('yes', 'southwest', 'male'): 'M-SW',
        ('yes', 'southwest', 'female'): 'F-SW',
        ('yes', 'southeast', 'male'): 'M-SE',
        ('yes', 'southeast', 'female'): 'F-SE',
    }

    df = (
        df
        .rename(columns={'smoker': 'is_smoker'})
        .replace({'is_smoker': {'yes': 'y', 'no': 'n'}})
        .assign(region_sex=lambda x: x.apply(lambda row: region_sex_map.get((row['is_smoker'], row['region'], row['sex']), 0), axis=1))
        .drop(columns=['is_smoker'])
    )

    # Returned the cleaned dataframe
    return df
