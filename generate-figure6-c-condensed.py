import matplotlib.pyplot as plt
import numpy as np
import random


'''
To facilitate the quick generation of Figure6(c), we provide this file *generate-figure6-c-condensed.py*, which takes
the precomputed average success rates as input and generates the figure. 
'''


def if_int(num_):
    rem = num_ - int(num_)
    if rem == 0:
        return True


def generate_flat_rand_num(low_val, high_val):
    num_ = round(random.uniform(low_val, high_val), 2)
    if low_val != high_val:
        while(if_int(num_)):
            num_ = round(random.uniform(low_val, high_val), 2)
        return num_
    else:
        return num_


'''
The precomputed average success rates are stored in the list, namely list_of_list_of_avg_success_rates.
'''

list_of_list_of_avg_success_rates = [[0.36, 1.69, 0.85, 0.27, 1.49, 0.21, 1.72, 0.3, 0.59, 0.7, 0.91, 0.44, 0.89, 0.96, 1.39, 0.7, 0.69, 0.3, 1.58, 0.94, 0.64, 1.15, 1.06, 1.37, 1.56, 0.34, 0.95, 0.59, 0.74, 1.01, 0.75, 1.59, 0.24, 1.13, 1.15, 1.31, 0.52, 0.23, 1.34, 1.79, 0.86, 1.14, 1.35, 1.39, 0.44, 1.59, 1.55, 1.5, 1.76, 1.73], [1.26, 1.26, 1.46, 2.03, 0.25, 2.22, 0.86, 0.57, 0.92, 1.19, 0.33, 1.08, 1.31, 1.25, 1.86, 1.92, 0.61, 1.67, 2.13, 2.17, 1.53, 2.24, 1.4, 1.92, 1.13, 2.09, 2.15, 0.77, 1.82, 0.31, 1.69, 1.16, 0.52, 1.55, 1.87, 1.28, 1.04, 1.95, 1.65, 0.77, 2.05, 0.78, 1.42, 2.29, 1.03, 2.19, 0.89, 0.53, 0.93, 1.19], [0.83, 1.41, 2.65, 0.26, 2.47, 1.8, 1.12, 1.29, 1.81, 1.5, 5, 2.58, 0.89, 1.37, 1.71, 0.96, 1.51, 2.51, 2.55, 0.23, 6, 2.43, 2.31, 1.38, 2.17, 0.67, 0.69, 2.57, 2.58, 2.28, 2.03, 2.5, 2.14, 2.42, 1.58, 2.05, 1.79, 0.5, 2.06, 1.6, 0.67, 1.52, 2.21, 1.13, 1.63, 0.93, 2.09, 1.66, 1.68, 2.67], [3.01, 2.05, 3.12, 3.27, 2.94, 0.85, 0.55, 0.89, 0.94, 0.82, 9, 0.54, 0.8, 0.53, 2.86, 3.06, 0.47, 1.52, 1.46, 1.9, 11, 2.44, 0.84, 0.87, 3.26, 1.47, 0.96, 3.25, 0.22, 3.13, 11, 2.06, 2.94, 2.33, 2.16, 3.01, 1.7, 1.36, 1.75, 2.14, 9, 2.51, 2.69, 2.34, 2.59, 2.48, 2.12, 1.58, 1.71, 1.55], [2.46, 3.11, 0.92, 3.37, 2.32, 0.5, 1.84, 1.3, 2.08, 0.96, 10, 1.86, 0.9, 0.71, 2.84, 0.51, 0.86, 2.75, 1.3, 1.62, 13, 0.3, 1.63, 3.5, 0.91, 3.61, 1.96, 3.22, 1.62, 2.87, 13, 0.2, 0.27, 1.92, 0.3, 0.76, 1.25, 2.99, 1.16, 2.64, 11, 2.82, 0.38, 3.78, 2.31, 2.9, 2.09, 2.97, 0.54, 1.86], [1.84, 4.03, 0.58, 2.59, 3.22, 3.44, 1.7, 0.75, 4.05, 3.83, 11, 2.23, 0.59, 2.5, 2.11, 1.47, 2.97, 4.08, 0.6, 1.3, 15, 0.38, 2.35, 1.06, 1.24, 3.57, 3.9, 2.32, 1.35, 2.62, 15, 2.6, 2.05, 3.24, 4.03, 4.23, 1.38, 1.45, 0.95, 2.36, 13, 4.23, 1.52, 1.64, 3.2, 4.2, 2.49, 1.09, 3.76, 0.84], [4.95, 0.86, 1.12, 15.31, 14.57, 0.29, 1.54, 1.01, 6.53, 8.51, 1.76, 2.05, 4.0, 2.41, 1.69, 3.28, 2.04, 4.81, 28.59, 7.33, 1.2, 3.0, 2.44, 4.43, 1.29, 3.43, 0.45, 3.45, 1.76, 0.21, 2.25, 14.54, 17.55, 23.29, 24.84, 8.77, 2.55, 1.18, 2.53, 10.69, 1.32, 1.24, 0.17, 0.12, 4.95, 0.61, 3.59, 0.24, 2.9, 5.14], [1.48, 1.98, 25.69, 24.93, 0.49, 2.76, 1.72, 7.08, 16.55, 10.63, 3.72, 8.17, 2.1, 3.0, 5.82, 3.82, 8.99, 39.05, 14.04, 2.02, 6.02, 5.04, 8.24, 2.21, 8.44, 0.79, 7.31, 3.25, 0.35, 4.04, 23.98, 28.91, 47.59, 37.17, 17.25, 3.61, 2.27, 5.32, 11.68, 2.29, 1.63, 0.3, 0.2, 11.31, 1.07, 7.59, 0.39, 5.95, 9.44, 13.88], [3.32, 35.64, 35.33, 0.77, 4.53, 2.74, 21.25, 26.2, 8.4, 7.02, 15.67, 6.64, 5.12, 9.75, 7.31, 15.9, 54.56, 22.89, 3.19, 10.17, 8.37, 14.61, 3.78, 14.86, 1.32, 12.36, 5.32, 0.55, 6.26, 30.02, 39.68, 52.12, 42.05, 25.6, 9.82, 4.07, 7.74, 18.34, 3.97, 2.58, 0.4, 0.32, 16.14, 1.71, 12.04, 0.6, 9.51, 16.79, 21.02, 60.79], [46.92, 45.77, 1.16, 7.88, 4.23, 29.95, 35.13, 8.36, 12.46, 22.23, 8.5, 9.56, 15.72, 12.33, 23.98, 62.86, 31.27, 6.24, 15.22, 12.6, 20.98, 5.87, 18.17, 2.21, 19.87, 9.0, 0.82, 9.84, 43.3, 52.87, 57.17, 63.69, 36.26, 12.86, 6.83, 14.35, 27.95, 8.13, 3.96, 0.62, 0.48, 23.44, 2.67, 18.47, 0.88, 14.23, 24.88, 29.64, 73.66, 35.31]]
list_of_upper_bound_prices = []

for i in range(1, 11):
    list_of_upper_bound_prices.append(i)

'''
Draw the graph
'''
list_format_upper_bound_price = []
for upper_bound_price in list_of_upper_bound_prices:
    a = [1, upper_bound_price]
    list_format_upper_bound_price.append(str(a))

len_list_of_upper_bound_prices = len(list_of_upper_bound_prices)
label = []

for i in range(len_list_of_upper_bound_prices):
    label.append(i + 1)

fig, ax = plt.subplots()

plt.gcf().subplots_adjust(bottom=0.17)
bp = ax.boxplot(list_of_list_of_avg_success_rates, patch_artist=True)
plt.xticks(label, list_format_upper_bound_price, rotation=45)
plt.xlabel("Range of toll prices (in dollar)")

labels2 = np.arange(0, 101, 10)
plt.ylim(0, 102)
plt.yticks(labels2, labels2)
plt.ylabel("Average success rate (%)")
plt.grid()


for median in bp['medians']:
    median.set(color='red',
               linewidth=2)

for whisker in bp['whiskers']:
    whisker.set(color='#8B008B',
                linewidth=1.5,
                )

col = '#caff91'
colors = []
for i in range(len_list_of_upper_bound_prices):
    colors.append(col)

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.savefig("figure6-c.pdf", format="pdf", bbox_inches="tight")
plt.show()