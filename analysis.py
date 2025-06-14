import pandas as pd
import numpy as np

reports = pd.read_csv('Reports.csv')
details = pd.read_csv('Details.csv')

reports = reports[['id', 'date', 'author', 'subreddit', 'permalink']]

df = pd.merge(reports, details, on='id', how='inner')
df['race_name'] = df['race_name'].fillna('Unknown')
df['race_name'] = df['race_name'].replace({'California International Marathon (CIM)' : 'California International Marathon',
                                           'New York City Marathon' : 'NYC Marathon',
                                           'LA Marathon' : 'Los Angeles Marathon',
                                           'TCS Amsterdam Marathon' : 'Amsterdam Marathon',
                                           'CIM' : 'California International Marathon',
                                           'BMO Vancouver Marathon' : 'Vancouver Marathon',
                                           'Chevron Houston Marathon' : 'Houston Marathon',
                                           'The San Francisco Marathon' : 'San Francisco Marathon',
                                           'Bank of America Chicago Marathon' : 'Chicago Marathon',
                                           'TCS NYC Marathon' : 'NYC Marathon',
                                           'Chicago' : 'Chicago Marathon',
                                           '47th Marine Corps Marathon' : 'Marine Corps Marathon', '49th Marine Corps Marathon' : 'Marine Corps Marathon', 
                                           '2016 Boston Marathon' : 'Boston Marathon', '126th Boston Marathon' : 'Boston Marathon',
                                           'Virgin London Marathon' : 'London Marathon', 'NCH Columbus Marathon' : 'Columbus Marathon',
                                           'Indianapolis Monumental Marathon' : 'Indy Monumental Marathon', 'Nationwide Children\'s Columbus Marathon' : 'Columbus Marathon',
                                           'Go! St. Louis Marathon' : 'St. Louis Marathon', 'Amica Insurance Seattle Marathon' : 'Seattle Marathon',
                                           'Novo Nordisk NJ Marathon' : 'New Jersey Marathon', 'Amica Seattle Marathon' : 'Seattle Marathon',
                                           'CNO Financial Indianapolis Monumental Marathon' : 'Indy Monumental Marathon',
                                           'Trinidad Alfonso EDP Valencia Marathon' : 'Valencia Marathon', '2016 TCS NYC Marathon' : 'NYC Marathon',
                                           'Athens Ohio Marathon' : 'Athens (Ohio) Marathon', 'Berlin Marathon 2023' : 'Berlin Marathon',
                                           '2018 London Marathon' : 'London Marathon', 'BMW Berlin Marathon' : 'Berlin Marathon',
                                           'Publix Atlanta Marathon' : 'Atlanta Marathon', 'Marine Corp Marathon' : 'Marine Corps Marathon',
                                           'Boston Marathon 2022' : 'Boston Marathon', 'London Marathon 2023' : 'London Marathon',
                                           'Philadelphia AACR Marathon' : 'Philadelphia Marathon', 'Kiawah Island Resort Marathon' : 'Kiawah Island Marathon',
                                           'Union Home Mortgage Cleveland Marathon' : 'Cleveland Marathon', 'TCS New York City Marathon' : 'NYC Marathon',
                                           '2023 Boston Marathon' : 'Boston Marathon', 'AACR Philadelphia Marathon' : 'Philadelphia Marathon',
                                           'NYCRuns Brooklyn Marathon' : 'Brooklyn Marathon', 'Dublin Marathon 2022' : 'Dublin Marathon',
                                           'Christie Clinic Illinois Marathon' : 'Illinois Marathon', 'BMO Harris Mesa-PHX Marathon' : 'Mesa Marathon',
                                           '2022 Philadelphia Marathon' : 'Philadelphia Marathon', 'Rock n Roll San Diego Marathon' : 'San Diego Marathon',
                                           'Philadelphia Marathon 2024' : 'Philadelphia Marathon', '121st Boston Marathon' : 'Boston Marathon',
                                           '2015 Boston Marathon' : 'Boston Marathon', '2017 Boston Marathon' : 'Boston Marathon', '2022 Boston Marathon' : 'Boston Marathon',
                                           '2023 Chicago Marathon' : 'Chicago Marathon', 'TCS London Marathon' : 'London Marathon',
                                           'TCS London Marathon 2022' : 'London Marathon', 'Berlin' : 'Berlin Marathon', 'Philly Marathon' : 'Philadelphia Marathon',
                                           '2024 California International Marathon' : 'California International Marathon',
                                           "Grandma’s Marathon" : "Grandma's Marathon", "Grandmas Marathon" : "Grandma's Marathon",
                                           '2022 LA Marathon' : 'Los Angeles Marathon', 'LA Marathon 2022' : 'Los Angeles Marathon',
                                           'Columbus Marathon 2022' : 'Columbus Marathon', 'The Columbus Marathon' : 'Columbus Marathon',
                                           "Nationwide Children's Hospital Columbus Marathon" : "Columbus Marathon", 'RNR San Diego' : 'San Diego Marathon',
                                           'Amsterdam Marathon 2023' : 'Amsterdam Marathon', 'Richmond Anthem Marathon' : 'Richmond Marathon'})


# df = df[df['race_name'].str.contains('Richmond')]
# print(df.groupby('distance').size().reset_index(name='Reports').sort_values(by='Reports', ascending=False))
# print(df.groupby('race_name').size().reset_index(name='Reports').sort_values(by='Reports', ascending=False))
# quit()

df['Year'] = pd.to_datetime(df['date']).dt.year
df = df[df['distance'] == 'Marathon']
df = df[df['Year'] >= 2016]

conditions = [df['training_plan'].str.contains('Pfitz'),
              df['training_plan'].str.contains('Jack'),
              df['training_plan'].str.contains('Hal'),
              df['training_plan'].str.contains('Hanson')]
values = ['Pfitz', 'Jack', 'Hal', 'Hanson']
df['Plan'] = np.select(conditions, values, df['training_plan'])
df['peak_miles_per_week'] = np.where(df['peak_miles_per_week'] == '60-65', '65', df['peak_miles_per_week'])
df['peak_miles_per_week'] = pd.to_numeric(df['peak_miles_per_week'], errors='coerce')
df['MPW'] = pd.cut(df['peak_miles_per_week'], bins=[0, 40, 55, 70, 85, 100, 1000], labels=['Under 40', '40-54', '55-69', '70-84', '85-99', '100+'], right=False)
df['runner_age'] = pd.to_numeric(df['runner_age'])
df['Age Group'] = pd.cut(df['runner_age'], bins=[0, 20, 30, 40, 50, 60, 100], labels=['Under 20', '20-29', '30-39', '40-49', '50-59', '60+'], right=False)
df['Finish'] = pd.to_timedelta(df['finish_time'], errors='coerce').dt.total_seconds()
df['Finish Time'] = pd.cut(df['Finish'], bins=[0, 9000, 9900, 10800, 11700, 12600, 13500, 14400, 50000], 
                           labels=['< 2:30', '2:30-2:45', '2:45-3:00', '3:00-3:15', '3:15-3:30', '3:30-3:45', '3:45-4:00', '> 4:00'])
######## Limit the reports to analyze
df = df[df['main_goal_reached'].isin(['True', 'False'])].copy()
df = df[df['runner_gender'].isin(['Female', 'Male'])]
# df = df[df['subreddit'] == 'AdvancedRunning']

# print(df.groupby('Year').size())
# print(df.groupby('Plan').size().reset_index(name='Reports').sort_values(by='Reports', ascending=False))

# print(df[(df['MPW'] == '100+') & (df['Finish Time'] == '3:30-3:45')])

############ Basic Demographics

# pd.crosstab(df['Age Group'], df['runner_gender']).to_csv('Output\\Runners by Age and Gender.csv')
# pd.crosstab(df['Year'], df['runner_gender']).to_csv('Output\\Runners by Gender and Year.csv')
# df.groupby(['race_name']).size().reset_index(name='Reports').sort_values(by='Reports', ascending=False).nlargest(25, 'Reports').to_csv('Output\\Popular Races.csv', index=False)
# pd.crosstab(df['Finish Time'], df['runner_gender']).to_csv('Output\\Times by Gender.csv')
# pd.crosstab(df['MPW'], df['runner_gender']).to_csv('Output\\Mileage by Gender.csv')

# pd.crosstab(df['Finish Time'], df['MPW']).to_csv('Output\\Finish Time by Mileage.csv')

# subset = df[(df['runner_gender'] == 'Male') & (df['Age Group'] == '20-29')]
# pd.crosstab(subset['Finish Time'], subset['MPW']).to_csv('Output\\20s MPW.csv')

# subset = df[(df['runner_gender'] == 'Male') & (df['Age Group'] == '30-39')]
# pd.crosstab(subset['Finish Time'], subset['MPW']).to_csv('Output\\30s MPW.csv')

# subset = df[(df['runner_gender'] == 'Male') & (df['Age Group'] == '40-49')]
# pd.crosstab(subset['Finish Time'], subset['MPW']).to_csv('Output\\40s MPW.csv')

df = df[df['Plan'].isin(['Other', 'Pfitz', 'Jack', 'Hal', 'Hanson'])]
# print(pd.crosstab(df['Plan'], df['Year']))
# print(df.groupby('Plan').size().reset_index(name='Reports'))



############### Was goal reached based on plan?
# df = df[(df['Finish Time'].isin(['2:45-3:00', '3:00-3:15']) & (df['runner_gender'] == 'Male'))]
# print(df.groupby('main_goal_reached').size().reset_index(name='Reports').nlargest(10, 'Reports'))
main = df[df['main_goal_reached'].isin(['True', 'False'])]
# pd.crosstab(main['Plan'], main['main_goal_reached']).to_csv('Output\\Main Goal by Plan.csv')
# print(pd.crosstab(main['Plan'], main['main_goal_reached'], normalize='index'))

secondary = df[df['secondary_goal_reached'].isin(['True', 'False'])]
# pd.crosstab(secondary['Plan'], secondary['secondary_goal_reached']).to_csv('Output\\Secondary Goal by Plan.csv')
# print(pd.crosstab(secondary['Plan'], secondary['secondary_goal_reached'], normalize='index'))

d1 = pd.crosstab(main['Plan'], main['main_goal_reached']).reset_index()
d1['Goal'] = 'Primary'
d2 = pd.crosstab(secondary['Plan'], secondary['secondary_goal_reached']).reset_index()
d2['Goal'] = 'Secondary'
pd.concat([d1, d2], ignore_index=True).to_csv('Output/Goals Met by Plan.csv', index=False)

############## End analysis on type of plan


######## Was goal reached based on MPW?
subset = df[df['main_goal_reached'].isin(['True', 'False'])].copy()
# pd.crosstab(subset['MPW'], subset['main_goal_reached']).to_csv('Output\\Main Goal by MPW.csv')
# print(pd.crosstab(subset['MPW'], subset['main_goal_reached'], normalize='index'))
# print(subset.groupby('peak_miles_per_week').size().reset_index(name='Reports').nlargest(50, 'Reports'))

secondary = df[df['secondary_goal_reached'].isin(['True', 'False'])]
# pd.crosstab(secondary['MPW'], secondary['secondary_goal_reached']).to_csv('Output\\Secondary Goal by MPW.csv')
# print(pd.crosstab(secondary['MPW'], secondary['secondary_goal_reached'], normalize='index'))

d1 = pd.crosstab(subset['MPW'], subset['main_goal_reached']).reset_index()
d1['Goal'] = 'Primary'
d2 = pd.crosstab(secondary['MPW'], secondary['secondary_goal_reached']).reset_index()
d2['Goal'] = 'Secondary'
pd.concat([d1, d2], ignore_index=True).to_csv('Output/Goals Met by MPW.csv', index=False)