%matplotlib inline
import json 
import matplotlib.pyplot as plt
  
# Opening JSON file 
with open('timeline.json', 'r') as openfile: 
    result = json.load(openfile) 

time = []
prob = []

for pair in result["slipping"]:
    time.append(pair[0])
    prob.append(pair[1])

plt.plot(time, prob, 'o-')
plt.title('Timeline')
plt.ylabel('Probability')
plt.xlabel('time (sec.)')
plt.show()