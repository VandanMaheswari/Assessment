import requests
import pandas as pd
import json

def download(url , path):
    req = requests.get(url)
    with open(path,'wb') as file:
        file.write(req.content)
        
        

def read_file(path):
    with open(path, 'r',encoding='utf-8') as file:
        data = json.load(file)
    return data      



url ="https://data.nasa.gov/resource/y77d-th95.json"   
path = "data_file"
save_file = "processed_data.csv"


download(url,path)

data = read_file(path)


new_data = []

for i in data:
    
    new_rows  = {
        "Name of Earth Meteorite" : i["name"],
        "ID of Earth Meteorite" : i["id"],
        "nametype" : i["nametype"],
        "recclass" : i["recclass"],
        "Mass of Earth Meteorite" : float(i.get("mass",0)),
        "Year at which Earth Meteorite was hit" : i.get("year",0),
        "point coordinates" : [int(j) for j in i.get('geolocation',{}).get('coordinates',{})]     
        
    }
    
    new_data.append(new_rows)
         
         

new_data = pd.DataFrame(new_data,columns=new_data[0].keys())

new_data.to_csv(save_file)

