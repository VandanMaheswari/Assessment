import requests
import pandas as pd
import json

def download(url , path):
    req = requests.get(url)
    with open(path,'wb') as file:
        file.write(req.content)
# this function is to download the data from the given link
        

def read_file(path):
    with open(path, 'r',encoding='utf-8') as file:
        data = json.load(file)
    return data        
# this is to read data from inside the file
        
 
url ="https://data.nasa.gov/resource/y77d-th95.json"   
path = "data_file"
save_file = "data.xlsx" 
# url is different because the given link of yours is not working thats why i use Question 4th link
        


# download("https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json","data_file")     
# that link isn't working

download(url,path)
# file downloaded      

data = read_file(path)
# readed the json file

data = pd.DataFrame(data)
# converted it into data frame

data.to_excel(save_file, index=False)
# save it  into excel formate

