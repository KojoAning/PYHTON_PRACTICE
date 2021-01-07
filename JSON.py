import json
data = '{"var1":"harry","var2":"srinath"}'
print(data) # (parsed['var1']) will give a error here because it is taking data as a str
parsed = json.loads(data) #dict - type
print(parsed['var1'])
data2 = '{"channel_name": "CodeWithHarry","cars": ["bmw" , "audi a8", "ferrari"],"fridge": ("roti", 540),"isbad": False}'
js_compatable = json.dumps(data2)
print(js_compatable)


# Opening JSON file
f = open('data.json', )

# returns JSON object as
# a dictionary
data3 = json.load(f)

# Iterating through the json
# list
for i in data3['emp_details']:
    print(i)

# Closing file
f.close()

#what is sort_keys parameter in dumps :