import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

'''
df = pd.read_csv("features.csv")
print(df)

print(df.hist(bins=6))
plt.show()
'''
def draw_feature_hist_chart(data):
    num = 10
    X = np.arange(num)
    W = np.random.randint(1, num*2, num)

    hist = plt.hist(X, bins=num, weights=W, density=False, cumulative=False, label='A', range=(X.min(), X.max()), color='r', edgecolor='black', linewidth=1.2)

    plt.title('scatter', pad=10)
    plt.xlabel('X axis', labelpad=10)
    plt.ylabel('Y axis', labelpad=10)

    plt.minorticks_on()
    plt.tick_params(axis='both', which='both', direction='in', pad=8, top=True, right=True)

    plt.show()


if __main__ == True:
    draw_feature_hist_chart('')