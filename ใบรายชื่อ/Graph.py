import numpy as np
import matplotlib.pyplot as plt

fin = open("score.csv", 'r')
DATA = fin.readlines()
fin.close()

S = sorted([float((line.split(',')[1]).strip()) for line in DATA], reverse = True)
print(S[30:38])
     
plt.xticks(np.arange(0, 101, 5))
plt.yticks(np.arange(0, 261, 1))
plt.hist(np.array(S), edgecolor = 'black', linewidth = 1.5)
plt.show()
