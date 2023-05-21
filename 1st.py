str1 = input("enter the sentence here :- ")
li = str1.split(" ")
unique_li = list(set(li))

dict1 = {}
count = 0
max_length = 0

for i in unique_li:
    for j in li:
        if j == i :
            count = count+1
            
    
    dict1[i] = count
    count =0


max_frequency = max(dict1.values())

for word, frequency in dict1.items():
    if frequency == max_frequency and len(word) > max_length:
        max_length = len(word)
        

print(max_length)        
     
            