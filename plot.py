import json 
  
# Opening JSON file 
with open('timeline.json', 'r') as openfile: 
  
    result = json.load(openfile) 
  
print(result["slipping"])