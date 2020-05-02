import json 
import matplotlib.pyplot as plt
import sys

# Opening JSON file 
with open(sys.argv[1], 'r') as openfile: 
    result = json.load(openfile) 

time = []
prob = []

for pair in result["slipping"]:
    time.append(pair[0])
    prob.append(pair[1])

plt.plot(time, prob, 'o-')
plt.title("Prediction Timeline for Sample")
plt.ylabel('Probability')
plt.xlabel('time (sec.)')
plt.savefig(sys.argv[2])

