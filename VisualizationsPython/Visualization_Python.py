#VISUALIZATION WITH PYTHON
import pandas as pd
import matplotlib.pyplot as plt

#load data 
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
covid_data = pd.read_csv(url)

#Overall instructions:
#As described in the homework description, each graphic you make must:
#1. Have a thoughtful title
#2. Have clearly labelled axes
#3. Be legible
#4. Not be a pie chart
#I should be able to run your .py file and recreate the graphics without error.
#As per usual, any helper variables or columns you create should be thoughtfully named.



'''VIS_1
Create a visualization that shows all of the counties in Utah as a time series,
similar to the one shown in slide 22 during the lecture. The graphic should
-Show cases over time
-Have all counties plotted in a background color (something like grey)
-Have a single county plotted in a contrasting color (something not grey)
-Have well formatted dates as the X axis
'''
#isolate Utah data 
utah_data = covid_data[covid_data["Province_State"] == "Utah"]

#drop unnecessary columns to keep only the time series
time_series = utah_data.drop(columns=['UID', 'iso2', 'iso3', 'code3', 'FIPS',
                                      'Admin2', 'Province_State', 'Country_Region',
                                      'Lat', 'Long_', 'Combined_Key'])

#make it so dates are in rows 
time_series = time_series.T
time_series.columns = utah_data['Admin2'].values  # county names as column headers

#convert dates to datetime format
time_series.index = pd.to_datetime(time_series.index)

#plot all counties in grey in the background 
plt.figure(figsize=(12, 6))
for county in time_series.columns:
    plt.plot(time_series.index, time_series[county], color='grey', alpha=0.5)

#chose a county to highlight 
highlight_county = 'Utah'
plt.plot(time_series.index, time_series[highlight_county], color='blue', linewidth=1, label=highlight_county)

#labels 
plt.title("Confirmed COVID-19 Cases Over Time: Utah Counties")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



'''VIZ_2
Create a visualization that shows the contrast between the county in Utah with
the most cases to date to a county in Florida with the most cases to date.
The graphic should:
-Have only two counties plotted
-Highlight the difference between the two comparison counties
You may use any style of graphic you like as long as it is effective (dense)
and readable
'''
#isolate county with the most cases in a given state
def get_top_county(state_name):
    state_data = covid_data[covid_data['Province_State'] == state_name]
    # Drop non-date columns
    time_series = state_data.drop(columns=['UID', 'iso2', 'iso3', 'code3', 'FIPS',
                                           'Country_Region', 'Lat', 'Long_', 'Combined_Key'])
    #add up cases for each county
    latest_cases = time_series.iloc[:, -1]
    top_index = latest_cases.idxmax()
    top_county_row = time_series.loc[top_index]
    county_name = state_data.loc[top_index, 'Admin2']
    return county_name, top_county_row.drop(['Admin2','Province_State'])

#isolate counties with most cases in Utah/Florida
utah_county, utah_series = get_top_county("Utah")
florida_county, florida_series = get_top_county("Florida")

#turn date string into datetime objects 
utah_series.index = pd.to_datetime(utah_series.index)
florida_series.index = pd.to_datetime(florida_series.index)

#plot both counties
plt.figure(figsize=(12, 6))
plt.plot(utah_series.index, utah_series.values, color='orange', linewidth=1, label=f"{utah_county} County, Utah")
plt.plot(florida_series.index, florida_series.values, color='purple', linewidth=1, label=f"{florida_county} County, Florida")

#labels 
plt.title("Most Confirmed Counties with COVID-19 Cases: Utah vs Florida")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



'''VIZ_3
Create a visualization that shows BOTH the running total of cases for a single
county AND the daily new cases. The graphic should:
-Use two y-axes
(https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
-Use color to contrast the two series being plotted
-Have well formatted dates as the X axis
'''

#choose a county
county_data = covid_data[(covid_data['Province_State'] == 'Utah') & (covid_data['Admin2'] == 'Utah')]

#keep only the date columns
time_series = county_data.drop(columns=['UID', 'iso2', 'iso3', 'code3', 'FIPS',
                                        'Country_Region', 'Lat', 'Long_', 'Combined_Key',
                                        'Admin2', 'Province_State'])

#make is so dates are rows 
time_series = time_series.T
time_series.columns = ['TotalCases']

#convert index to datetime
time_series.index = pd.to_datetime(time_series.index)

#calculate daily new cases (difference between consecutive days)
time_series['DailyNewCases'] = time_series['TotalCases'].diff().fillna(0)

#create dual-axis plot
fig, ax1 = plt.subplots(figsize=(12, 6))

#plot running total on left y-axis
ax1.plot(time_series.index, time_series['TotalCases'], color='blue', linewidth=1, label='Running Total Cases')
ax1.set_xlabel("Date")
ax1.set_ylabel("Total Cases", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

#create second y-axis for daily new cases
ax2 = ax1.twinx()
ax2.bar(time_series.index, time_series['DailyNewCases'], color='red', alpha=0.5, label='Daily New Cases')
ax2.set_ylabel("Daily New Cases", color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

#labels 
plt.title("COVID-19 Cases in Utah County)")
fig.autofmt_xdate()  
fig.tight_layout()
plt.show()



'''VIZ_4
Create a visualization that shows a stacked bar chart of county contributions
to a given state's total cases. You may choose any state (or states).
(https://matplotlib.org/stable/gallery/lines_bars_and_markers/
bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
The graphic should:
-Have a single column delineate a state
-Have each 'slice' or column compontent represent a county
'''

#pick a state
state_name = "Utah"
state_data = covid_data[covid_data['Province_State'] == state_name]

#most recent case counts (last column in the dataset)
latest_cases = state_data.iloc[:, -1].values
counties = state_data['Admin2'].values

#create stacked bar chart with different colors
fig, ax = plt.subplots(figsize=(10, 10))
bottom_val = 0
colors = plt.cm.tab20.colors  #colormap with 20 distinct colors

for i, county in enumerate(counties):
    ax.bar(state_name, latest_cases[i], bottom=bottom_val, 
           color=colors[i % len(colors)], label=county)
    bottom_val += latest_cases[i]

#labels 
ax.set_ylabel("Confirmed Cases")
ax.set_title(f"County Contributions to {state_name}'s Total COVID-19 Cases")
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
