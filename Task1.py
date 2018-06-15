import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

#funkcja odpowiedzalna za wyznaczanie wspolczynnikow regresjiliniowej
#i na ich podstawie wyznaczanie przewidywanej wartosci na kolejny miesiac
def prediction(subs, views):
    x1 = range(1, len(subs) + 1, 1)
    x2 = range(1, len(views) + 1, 1)

    x1_pred = range(1, len(subs)+1 + 1, 1)
    x2_pred = range(1, len(subs)+1 + 1, 1)

    print("Linear Regression:")

    slope, intercept, r_value, p_value, std_err = stats.linregress(x1, subs)

    plt.subplot(2, 1, 1)
    plt.plot(x1_pred, intercept + slope*x1_pred, 'r-', label='fitted line')
    plt.plot(x1, subs, 'ro')
    plt.ylabel('Subscriptions')
    plt.grid()
    print("Expected amount of new subs in next month:", intercept + slope*x1_pred[-1])

    slope, intercept, r_value, p_value, std_err = stats.linregress(x2, views)

    plt.subplot(2, 1, 2)
    plt.plot(x2_pred, intercept + slope*x2_pred, 'b-', label='fitted line')
    plt.plot(x2, views, 'bo')
    plt.ylabel('Views')
    plt.xlabel('Months')
    plt.grid()
    print("Expected amount of new views in next month:", intercept + slope * x2_pred[-1])


#amount of new subscriptions and views
subs = np.array([100, 200, 225, 400])
views = np.array([50, 70, 75, 120])

prediction(subs, views)


#wyznaczanie wartosci z wykorzytaniem sredniej ruchomej
def movAverage(list):
    return np.average(list)


#wyznaczanie wartosci z wykorzytaniem sredniej ruchomej wazonej
#wagi rosną logarytmicznie, jest mozliwosc liniowego wzrostu wag
def movAverageWeighted(list):
    list_len = len(list)
    #return np.average(list, weights=range(1, list_len*40, 40))
    return np.average(list, weights=np.logspace(0.0, list_len-1, num=list_len))


print("\nMoving Average:")
print("Expected amount of new subs in next month:", movAverage(subs))
print("Expected amount of new views in next month:", movAverage(views))

print("\nMoving Average Weighted:")
print("Expected amount of new subs in next month:", movAverageWeighted(subs))
print("Expected amount of new views in next month:", movAverageWeighted(views))


plt.show()
