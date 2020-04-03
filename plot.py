import json 
import matplotlib.pyplot as plt

for i in range(1,6):
    # Opening JSON file 
    with open("sample"+str(i)+".json", 'r') as openfile: 
        result = json.load(openfile) 

<<<<<<< HEAD
for pair in result["crawling"]:
    time.append(pair[0])
    prob.append(pair[1])

plt.plot(time, prob, 'o-')
plt.title('Timeline')
plt.ylabel('Probability')
plt.xlabel('time (sec.)')
plt.show()
=======
    time = []
    prob = []

    for pair in result["crawling"]:
        time.append(pair[0])
        prob.append(pair[1])

    plt.plot(time, prob, 'o-')
    plt.title("Prediction Timeline for Sample "+str(i))
    plt.ylabel('Probability')
    plt.xlabel('time (sec.)')
    plt.show()
>>>>>>> 2178cfdd68a5e2fb20deb310cae8e3a9f871bb2b
