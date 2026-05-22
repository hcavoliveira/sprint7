import pandas as pd
from scipy import stats as st
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

result_01 = pd.read_csv('project_sql_result_01.csv')
result_04 = pd.read_csv('project_sql_result_04.csv')
result_07 = pd.read_csv('project_sql_result_07.csv')

#print(result_01.info(), end="\n\n")
#print(result_01.head(), end="\n\n\n")

#print(result_04.info(), end="\n\n")
#print(result_04.head(), end="\n\n\n")

#print(result_07.info(), end="\n\n")
#print(result_07.head(10), end="\n\n\n")

result_07['start_ts'] = pd.to_datetime(result_07['start_ts'])

result_04 = result_04.sort_values(by='average_trips', ascending=False)
#print(result_04.head(10))

#result_01.plot(kind='bar',
#               x='company_name',
#               y='trips_amount',
#               title='Trips by Company',
#               xlabel='Company Name',
#               ylabel='Trips Taken',
#               figsize=(15, 8),
#               legend=False)
#plt.show()

# result_04.head(10).plot(kind='bar',
#                         x='dropoff_location_name',
#                         y='average_trips',
#                         title='Top 10 Destination Neighborhoods',
#                         xlabel='Neighborhood',
#                         ylabel='Average Trips',
#                         figsize=(10, 8),
#                         legend=False,
#                         rot=45)
# plt.show()

#print(result_01.query('company_name == "Flash Cab" or company_name == "Taxi Affiliation Services" or company_name == "Medallion Leasin" or company_name == "Yellow Cab" or company_name == "Taxi Affiliation Service Yellow"')['trips_amount'].sum())
#print(result_01.query('company_name != "Flash Cab" and company_name != "Taxi Affiliation Services" and company_name != "Medallion Leasin" and company_name != "Yellow Cab" and company_name != "Taxi Affiliation Service Yellow"')['trips_amount'].sum())

#print(result_07.info())
#print(result_07[result_07['start_ts'].dt.weekday == 5])

alpha = 0.05

print(result_07.query('start_ts.dt.weekday == 5 and weather_conditions == "Bad"')['duration_seconds'].var() == result_07.query('start_ts.dt.weekday == 5 and weather_conditions == "Good"')['duration_seconds'].var())
results = st.ttest_ind(result_07.query('start_ts.dt.weekday == 5 and weather_conditions == "Bad"')['duration_seconds'],
                       result_07.query('start_ts.dt.weekday == 5 and weather_conditions == "Good"')['duration_seconds'],
                       equal_var=False
                      )

print('valor-p: ', results.pvalue)

if results.pvalue < alpha:
    print("Rejeitamos a hipótese nula")
else:
    print("Não podemos rejeitar a hipótese nula")