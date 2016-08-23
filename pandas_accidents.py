import pandas as pd

# Read the file
data = pd.read_csv("./statsdata/Accidents7904.csv", low_memory=False)
# Output the number of rows
print("Total rows: {0}".format(len(data)))
# See which headers are available
print(list(data))

print("\nAccidents")
print("-----------")

# Accidents which happened on a Sunday
accidents_sunday = data[data.Day_of_Week == 1]
print "type(accidents_sunday)=", type(accidents_sunday)
print("Accidents which happened on a Sunday: {0}".format(
    len(accidents_sunday)))

# Accidents in London on a Sunday
london_data = data[data['Police_Force'] == 1 & (data.Day_of_Week == 1)]
print("\nAccidents in London from 1979-2004 on a Sunday: {0}".format(
    len(london_data)))

# Accidents which happened on a Sunday, > 20 cars
accidents_sunday_twenty_cars = data[
    (data.Day_of_Week == 1) & (data.Number_of_Vehicles > 20)]
print("Accidents which happened on a Sunday involving > 20 cars: {0}".format(
    len(accidents_sunday_twenty_cars)))


# Accidents which happened on a Sunday, > 20 cars, in the rain
accidents_sunday_twenty_cars_rain = data[
    (data.Day_of_Week == 1) & (data.Number_of_Vehicles > 20) &
    (data.Weather_Conditions == 2)]
print("Accidents which happened on a Sunday involving > 20 cars in the rain: {0}".format(
    len(accidents_sunday_twenty_cars_rain)))


# Convert date to Pandas date/time
#if date > 2000-01-01 & date < 2000-12-31
london_data_2000 = london_data[
    (pd.to_datetime(london_data['Date'], errors='coerce') > pd.to_datetime('2000-01-01', errors='coerce')) &
    (pd.to_datetime(london_data['Date'], errors='coerce') < pd.to_datetime('2000-12-31', errors='coerce'))
]
print("(uses > & <)  Accidents in London in the year 2000 on a Sunday: {0}".format(
    len(london_data_2000)))
london_data_2000 = london_data[
    (pd.to_datetime(london_data['Date'], errors='coerce') >= pd.to_datetime('2000-01-01', errors='coerce')) &
    (pd.to_datetime(london_data['Date'], errors='coerce') <= pd.to_datetime('2000-12-31', errors='coerce'))
]
print("(uses >= & <=)  Accidents in London in the year 2000 on a Sunday: {0}".format(
    len(london_data_2000)))

# from pandas.to_datetime api docs : if errors='coerce', then invalid parsing will be set as NaT
#NB: coerce=True has been deprecated from pandas.to_datetime
#original logic incorrectly used > instead of >=  (and < instead of <=)

print "type(london_data_2000)=", type(london_data_2000)
print "list(london_data_2000.columns.values)=", list(london_data_2000.columns.values)
print "london_data_2000.columns.values.tolist()=", london_data_2000.columns.values.tolist()

london_data_2000.rename(columns={'\xef\xbb\xbfAccident_Index': 'Accident_Index'}, inplace=True)
#UnicodeDecodeError: 'ascii' codec can't decode byte 0xef in position 7: ordinal not in range(128)
#still getting this 'error' message.
#SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
#See the caveats in the documentation:
# http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
# the intended change is made and saved to the exported file, so the warning can be ignored.
# the warning should be supressible ?
print "london_data_2000.columns.values.tolist()=", london_data_2000.columns.values.tolist()
#
# Save to Excel
writer = pd.ExcelWriter('London_Sundays_2000.xlsx', engine='xlsxwriter')
london_data_2000.to_excel(writer, 'Sheet1')
writer.save()



"""
https://realpython.com/blog/python/working-with-large-excel-files-in-pandas/
http://xlsxwriter.readthedocs.io/working_with_pandas.html
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html
"""