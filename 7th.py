import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("processed_data.csv")

df = pd.DataFrame(df)

for i in df["Year at which Earth Meteorite was hit"]:
    df['year'] = int(str(i).split("-")[0])

meteorite_before_2000 = df[df['year'] < 2000]
print(meteorite_before_2000)


coordinates_before_1970 = df[df['year'] < 1970]['point coordinates']
print(coordinates_before_1970)

meteorite_mass_10000 = df[df['Mass of Earth Meteorite'] > 10000]
print(meteorite_mass_10000)

plt.figure(figsize=(8, 6))
plt.hist(meteorite_before_2000['year'], bins=20, edgecolor='black')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Earth Meteorites Fell Before 2000')
plt.show()


plt.figure(figsize=(8, 6))
plt.scatter(coordinates_before_1970[0], coordinates_before_1970[1], color='blue')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Earth Meteorites Coordinates Fell Before 1970')
plt.show()


plt.figure(figsize=(8, 6))
plt.bar(meteorite_mass_10000['Name of Earth Meteorite'], meteorite_mass_10000['Mass of Earth Meteorite'])
plt.xlabel('Meteorite Name')
plt.ylabel('Mass (kg)')
plt.title('Earth Meteorites with Mass Above 10000kg')
plt.xticks(rotation=90)
plt.show()
