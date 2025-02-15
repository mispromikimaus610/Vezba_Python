dict1={'a':1,'b':2}
dict2={'b':3,'c':4}

for key, value in dict2.items():
    dict1[key]=dict1.get(key,0) + value
    
print(dict1)