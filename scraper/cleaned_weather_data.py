import pandas as pd

df = pd.read_csv('./weather_data.csv')
#print(df.head())

# strip the white space

df['City'] = df['City'].str.strip()

df['Country'] = df['Country'].str.strip()

df['Date'] = df['Date'].str.strip()

df['Weather Condition'] = df['Weather Condition'].str.strip()

df['Temperature'] = df['Temperature'].str.strip()


#Country formatting


df['Country']= df['Country'].str.replace("-", " ").str.title()
#print(df['Country'])

# #City Formating
# cities = [letter.replace("*", "").title() for letter in cities]
# print(cities)
df['City']= df['City'].str.replace("*", "").str.title()
#print(df['City'])

# formate Date from str to datetime obj
df['Date'] = pd.to_datetime(df['Date'], format='%a %I:%M %p')
df['Date'] = df['Date'].dt.strftime('%a %I:%M %p')
#print(df['Date'].head())

# Temperature removing degree and F and renaming the header and changing str to int
df.rename(columns={'Temperature': 'Temperature in F'}, inplace=True)

df['Temperature in F'] = df['Temperature in F'].str.replace('°F', '').astype(int)

print(df.head())


# removing Duplicate
df = df.drop_duplicates()

# reseting index

df = df.reset_index(drop=True)

# saving the cleaned data to new csv file

df.to_csv('./cleaned_weather_data.csv', index = False)
print(df.head())