def medal_tally(df, year, country):
    medal_df = df.dropna(subset=['Medal'])

    if year != 'Overall':
        medal_df = medal_df[medal_df['Year'] == int(year)]

    if country != 'Overall':
        medal_df = medal_df[medal_df['region'] == country]

    medal_df = medal_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    tally = medal_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()
    tally['Total'] = tally['Gold'] + tally['Silver'] + tally['Bronze']

    return tally


def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    countries = df['region'].dropna().unique().tolist()
    countries.sort()
    countries.insert(0, 'Overall')

    return years, countries

def data_over_time(df,col):
    nations_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index()
    nations_over_time.columns = ['Edition',col]
    return nations_over_time.sort_values('Edition')

def most_successful(df, sport):
    temp_df = df.dropna(subset=['Medal'])

    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]

    top_athletes = temp_df['Name'].value_counts().reset_index()
    top_athletes.columns = ['Name', 'Medals']

    # merge using 'Name' (not 'index') and get required columns
    merged_df = top_athletes.head(15).merge(df, on='Name', how='left')[['Name', 'Medals', 'Sport', 'region']]

    # drop duplicates to avoid repeated athlete entries
    return merged_df.drop_duplicates('Name')

def yearwise_medal_tally(df,country):
    temp_df = df.dropna(subset = ['Medal'])
    temp_df.drop_duplicates(subset = ['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace = True)
    new_df = temp_df[temp_df['region'] == country]
    final_df = new_df.groupby('Year').count()['Medal'].reset_index()
    return final_df

def country_event_heatmap(df,country):
    temp_df = df.dropna(subset = ['Medal'])
    temp_df.drop_duplicates(subset = ['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace = True)
    new_df = temp_df[temp_df['region'] == country]
    pt = new_df.pivot_table(index='Sport', columns = 'Year', values = 'Medal', aggfunc = 'count').fillna(0)
    return pt    

def most_successful_countrywise(df, country):
    temp_df = df.dropna(subset=['Medal'])

   
    temp_df = temp_df[temp_df['region'] == country]

    top_athletes = temp_df['Name'].value_counts().reset_index()
    top_athletes.columns = ['Name', 'Medals']

    # merge using 'Name' (not 'index') and get required columns
    merged_df = top_athletes.head(10).merge(df, on='Name', how='left')[['Name', 'Medals', 'Sport']]

    # drop duplicates to avoid repeated athlete entries
    return merged_df.drop_duplicates('Name')

def weight_v_height(df, sport):
    athlete_df = df.drop_duplicates(subset = ['Name', 'region'])
    athlete_df['Medal'].fillna('No Medal', inplace = True)
    if sport !='Overall':
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        return temp_df
    else:
        return athlete_df

def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset = ['Name', 'region'])
    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()
    final = men.merge(women, on = 'Year', how = 'left')
    final.rename(columns={'Name_x':'Male', 'Name_y':'Female'}, inplace = True)
    final.fillna(0, inplace = True)
    return final