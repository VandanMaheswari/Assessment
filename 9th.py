import requests
import pandas as pd
import matplotlib.pyplot as plt

def download(url,path):
    req = requests.get(url)
    with open(path,'wb') as file:
        file.write(req.content)
    


# url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"
path = "data_file.csv"
download(url,path)

df = pd.read_csv(path)


# all the cars and their types that do not qualify for clean alternative fuel vehicle
print(df[df["Clean Alternative Fuel Vehicle (CAFV) Eligibility"] == "Clean Alternative Fuel Vehicle Eligible"][["Model","Electric Vehicle Type"]])


# all TESLA cars with the model year, and model type made in Bothell City.
df1 = pd.DataFrame(df[df["Make"] == "TESLA"])
print(df1[df1["City"] == "Bothell" ][["Make","Model","Model Year"]])


# all the cars that have an electric range of more than 100, and were made after 2015
df1 = pd.DataFrame(df[df["Electric Range"] > 100])
print(df1[df1["Model Year"] > 2015 ][["Make","Model"]])


# plots to show the distribution between city and electric vehicle type
grouped_data = df.groupby(['City', 'Electric Vehicle Type']).size().unstack()
grouped_data.plot(kind='bar', stacked=True)
plt.xlabel('City')
plt.ylabel('Count')
plt.title('Distribution of Electric Vehicle Types in Cities')
plt.show()
