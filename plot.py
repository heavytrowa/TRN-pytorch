import json 
import matplotlib.pyplot as plt

for i in range(1,6):
    # Opening JSON file 
    with open("sample"+str(i)+"_.json", 'r') as openfile: 
        result = json.load(openfile) 

    time = []
    prob = []

    for pair in result["slipping"]:
        time.append(pair[0])
        prob.append(pair[1])

    plt.plot(time, prob, 'o-')
    plt.title("Prediction Timeline for Sample "+str(i))
    plt.ylabel('Probability')
    plt.xlabel('time (sec.)')
    plt.show()
