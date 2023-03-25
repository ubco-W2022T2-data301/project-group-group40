import pandas as pd

def load_and_process(file):

    def s(row):
        if row['smoker'] == 'y':
            if row['region'] == 'northwest':
                if row['sex'] == 'male':
                    return 'M-NW'
                else:
                    return 'F-NW'
            elif row['region'] == 'northeast':
                if row['sex'] == 'male':
                    return 'M-NE'
                else:
                    return 'F-NE'
            elif row['region'] == 'southwest':
                if row['sex'] == 'male':
                    return 'M-SW'
                else:
                    return 'F-SW'
            elif row['region'] == 'southeast':
                if row['sex'] == 'male':
                    return 'M-SE'
                else:
                    return 'F-SE'
        else:
            return 0

    df = (
        pd.read_csv(file)
          .drop(['children'], axis=1)
    )
    
    df= (
        df.drop_duplicates()
          .dropna()
    )
    
    df=(df.
          assign(smoker=lambda x: x['smoker'].map({'yes': 'y', 'no': 'n'}))
          .assign(region_sex=lambda x: x.apply(s, axis=1))
         )
    
    
   

    return df

file = '../data/raw/Medical_Cost.csv'

