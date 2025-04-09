import pandas as pd

# Load data
df = pd.read_csv('/Users/kavin/Downloads/olympic_data/athlete_events.csv')
region_df = pd.read_csv('/Users/kavin/Downloads/olympic_data/noc_regions.csv')

# Preprocessing function
def preprocess(df, region_df):
    

    # Filter only Summer Olympics
    df = df[df['Season'] == 'Summer']

    # Merge with region data
    df = df.merge(region_df, on='NOC', how='left')

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # One-hot encode Medal column (adds Gold, Silver, Bronze columns)
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)

    return df

