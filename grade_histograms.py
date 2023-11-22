import matplotlib.pyplot as plt


testscores= [62, 50,90, 55, 92, 80, 84, 88, 98, 54, 72, 60,68,
             94, 77, 86, 92, 32, 65, 86, 95]

bins=[30,40,50,60,70,80,90,100]

plt.hist(testscores, bins, histtype='bar', rwidth=0.8)

plt.show()
