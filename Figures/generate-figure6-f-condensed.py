import matplotlib.pyplot as plt
import numpy as np

'''
To facilitate the quick generation of Figure6(f), we provide this file *generate-figure6-f-condensed.py*, which takes
the precomputed average success rates as input and generates the figure. 
'''


'''
The precomputed average success rates are stored in the list, namely list_of_list_of_avg_success_rates.
'''

list_of_toll_stations = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_of_list_of_avg_success_rates = [[93.73, 89.45, 88.96, 87.91, 84.41, 80.66, 79.27, 74.3, 68.91, 65.87, 63.35, 60.45], [53.75, 35.98, 32.94, 23.96, 16.52, 14.1, 12.44, 9.23, 6.48, 5.25, 4.56, 3.67],[4.96, 1.65, 1.17, 0.55, 0.28, 0.2, 0.16, 0.1, 0.06, 0.04, 0.02, 0.01]]

plt.figure()
plt.grid()
for j, list_of_avg_success_rate in enumerate(list_of_list_of_avg_success_rates):
    colors = ['r', 'b', 'g']

    plt.plot(list_of_toll_stations, list_of_avg_success_rate, '--', color=colors[j], marker='o', markerfacecolor='black', markersize=4, linewidth=2)
    labels1 = np.arange(9, 21, 1)
    plt.xticks(labels1, labels1)
    plt.xlim(9, 20)

    labels2 = np.arange(0, 101, 10)
    plt.yticks(labels2, labels2)
    max_y_range = 101
    plt.ylim(0, max_y_range)

    plt.xlabel('Number of toll stations')
    plt.ylabel('Average success rate (%)')

plt.savefig("ASR-num-of-tolls.pdf", format="pdf", bbox_inches="tight")

plt.show()

