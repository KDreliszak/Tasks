import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

#amount of new subscriptions and views
subs = [1, 2, 3, 4]
views = [50, 70, 75, 120]

y1 = range(0, len(subs), 1)
y2 = range(0, len(views), 1)

print(y1, y2)


def linearReg(x, y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return x, intercept + slope*x


plt.subplot(2, 1, 1)
plt.plot(linearReg(subs, y1), 'r', label='fitted line')
#plt.plot(subs, y1, 'o-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(linearReg(views, y2))
#plt.plot(views, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

plt.plot(subs, y1, 'o', label='original data')
plt.plot(subs, intercept + slope*subs, 'r', label='fitted line')
plt.legend()


plt.show()





def movAverage(list):
    return np.average(list)

def movAverageWeighted(list):
    list_len = len(list)
    return np.average(list, weights=range(1, list_len*10, 10))

print("Moving Average:")
print("Expected amount of new subs in next month:", movAverage(subs))
print("Expected amount of new views in next month:", movAverage(views))

print("Moving Average Weighted:")
print("Expected amount of new subs in next month:", movAverageWeighted(subs))
print("Expected amount of new views in next month:", movAverageWeighted(views))