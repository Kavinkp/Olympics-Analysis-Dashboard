import streamlit as st
import pandas as pd

# Load the data
df = pd.read_csv('olympic_data/athlete_events.csv')
region_df = pd.read_csv('olympic_data/noc_regions.csv')

# Preprocess
df = df[df['Season'] == 'Summer']
df = df.merge(region_df, on='NOC', how='left')
df.drop_duplicates(inplace=True)
df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)

# Medal tally
medal_counts = df.groupby('NOC')[['Gold', 'Silver', 'Bronze']].sum()
medal_counts = medal_counts.sort_values('Gold', ascending=False).reset_index()

# Streamlit UI
st.title("Olympic Medal Tally")
st.dataframe(medal_counts.head(10))  # Show top 10 countries
