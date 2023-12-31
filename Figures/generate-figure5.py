import matplotlib.pyplot as plt
import os.path
import sys
directory = os.path.dirname(os.path.abspath("__file__"))
sys.path.append(os.path.dirname(os.path.dirname(directory)))
from Tracing.sys_logger import sys_log
logfile = 'figure5.log'
logger1 = sys_log(logfile, 'figure5', 0)

'''
This file generates Figure 5 showing the distribution of all success rates across all plausible wallets within the 
waller range [w_l, w_u].
'''

'''
Each row of the file 'success-rates.txt' includes a list of success rates associated with the wallet ranges [0, 10], 
[10, 20], and [20, 40] respectively. These lists are recorded in the files, namely 'distribution-SR.txt' located in the 
subfolders in Folder 'CD-attack-data'.  
'''

file1 = open('success-rates.txt', 'r')
list_of_list_of_success_rates = file1.readlines()
file1.close()
list_of_list_distribution_of_success_rates = []
list_of_success_rates = []
list_wallet_range = ['[$0, $10]', '[$10, $20]', '[$20, $40]']

for index_, list_distribution_of_success_rates in enumerate(list_of_list_of_success_rates):
    logger1.debug("The wallet range: " + list_wallet_range[index_])
    logger1.debug("list_distribution_of_success_rates: " + str(list_distribution_of_success_rates))
    list_distribution_of_success_rates = eval(list_distribution_of_success_rates)
    list_of_list_distribution_of_success_rates.append(list_distribution_of_success_rates)


# Draw Box graph showing the distribution of success rates

label1 = [1, 2, 3]
len_label1 = len(label1)
fig, ax = plt.subplots()
plt.gcf().subplots_adjust(bottom=0.20)
bp = ax.boxplot(list_of_list_distribution_of_success_rates, patch_artist=True)
plt.xticks(label1, list_wallet_range, rotation=45)
plt.xlabel("Wallet ranges (in dollar)")

plt.ylabel("Success rate (%)")
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
for i in range(len_label1):
    colors.append(col)

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.savefig("figure5.png", dpi=600, bbox_inches="tight")

plt.show()
