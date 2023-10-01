# Tracing
# Artifact Appendix

Paper title: **Why Privacy-Preserving Protocols Are Sometimes Not Enough: A Case Study of the Brisbane Toll Collection Infrastructure**

Artifacts HotCRP Id: **#6**

Requested Badge: **Reproducible**

## Description
This repository contains three main folders: `CD-Attack`, `Figures`, and `TSD-Attack`. The CD-Attack folder contains
source codes related to the CD-Attack. The Figures folder contains files for reproducing the figures in the
paper, including Figures 3, 4(a), 4(b), 5, 6(a), 6(b), 6(c), 6(d), 6(e), and 6(f). Finally, the TSD-Attack folder
includes files related to the TSD-Attack.
### Security/Privacy Issues and Ethical Concerns
There are no Security/Privacy Issues and Ethical Concerns.

## Basic Requirements
The 64-bit version of Windows 10 1809 and later, or Windows Server 2019 and later <br>
x86 64-bit CPU (Intel / AMD architecture) <br>
4 GB RAM <br>
5 GB free disk space <br>
1024x768 minimum screen resolution

### Hardware Requirements
The hardware should at least satisfy the following requirements. <br> 
x86 64-bit CPU (Intel / AMD architecture) <br>
4 GB RAM <br>
5 GB free disk space

### Software Requirements
The 64-bit version of Windows 10 1809 and later, or Windows Server 2019 and later <br>
Download *Microsoft Visual C++ Redistributable*: [(Download link)](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022) <br>
Download *IBM ILOG CPLEX Optimization Studio Free Edition* (Windows edition), namely *cos_installer_preview-22.1.1.0.R0-M08SVML-win-x86-64.exe*: [(Download link)](https://www.ibm.com/account/reg/us-en/signup?formid=urx-20028)
Note that to download the file, you should fill out the corresponding form. <br>
Python 3.10 [(Link)](https://www.python.org/downloads/release/python-3100/) <br> 
Node.js v18 [(Link)](https://nodejs.org/en)

### Estimated Time and Storage Consumption
The estimated time depends on the file and varies between 2 minutes and ten days. <br>
5 GB free disk space

## Environment
The following describes how to access our artifact and all related and necessary data and software components. <br>
Afterward, we describe how to set up everything and verify everything is set up correctly.

### Accessibility
All the source codes are available through the below link: <br>
[Source codes](https://github.com/amiradavoudi/Tracing.git) 

### Set up the environment
First, install *Microsoft Visual C++ 2015-2022 Redistributable Package* as it is needed by the program in the next step. <br>
Install *IBM ILOG CPLEX Optimization Studio Free Edition*. Please follow the instructions during the installation. <br> 
Install Python 3.10 <br>
Install Node.js v18 or above <br>
The packages used in this repo are listed in *requirements.txt*. To install the packages, run `pip3 install -r requirements.txt`.


### Testing the Environment
File *test.py* includes all the packages required for the execution of the source codes in this project. <br> 
Run the file *test.py*. If all the required packages are installed properly, the log file *test.log* should be created, and outputs are written there,
from *output1* to *output5*. Besides, the file *test-figure.pdf* should be created, showing a graph. <br>


## Artifact Evaluation
This section includes all the steps required to evaluate our artifact's functionality and validate our paper's key results and claims. <br>
We highlight our paper's main results and claims in the first subsection and describe the experiments that support our claims in the subsection after that.

### Main Results and Claims
Here, we list all our paper's main results and claims supported by our submitted artifacts.

#### Main Result 1: tsd-attack
The results are the ASRs regarding the tsd-attack, shown in Table 1. <br>
The results are w.r.t wallet ranges [0,10], [10, 20], and [20, 40]. <br>
The number of plausible wallets includes 91, 721, and 2000; the ASRs include 94%, 54%, and 5%. <br>
Please refer to Section 5.1 of the paper (Table 1) and Experiment 1. 

#### Main Result 2: Figure 4(a)
Figure 4(a) shows the number of solutions per wallet balance (in dollars).<br>
Please refer to Section 5.2.3 of the paper (Figure 4) and Experiment 2. 

#### Main Result 3: Figure 4(b)
The result in Figure 4(b) shows the run-time (in ms) for each wallet balance (in dollars). <br>
Please refer to Section 5.2.3 of the paper (Figure 4) and Experiment 3. 

#### Main Result 4: tsd-attack-with-heuristic
The ASRs and APDS regarding the tsd-attack using the first heuristic are shown in Table 2. <br>
The results are w.r.t wallet ranges [0, 10], [10, 20], and [20, 40]. <br> 
Please refer to Section 5.3 of the paper (Table 2) and Experiment 4. 

#### Main Result 5: Figure 6(a)
Figure 6(a) shows the average success rate for each toll price range w.r.t wallet range [0, 10]. <br>
Please refer to Section 8 of the paper (Figure 6) and Experiment 5.

#### Main Result 6: Figure 6(b)
Figure 6(b) shows the average success rate for each toll price range w.r.t wallet range [10, 20]. <br>
Please refer to Section 8 of the paper (Figure 6) and Experiment 6.

#### Main Result 7: Figure 6(c)
Figure 6(c) shows the average success rate for each toll price range w.r.t wallet range [20, 40]. <br>
Please refer to Section 8 of the paper (Figure 6) and Experiment 7.

#### Main Result 8: Figure 6(d)
Figure 6(d) shows the success rate for each wallet balance (in dollars). <br>
Please refer to Section 8 of the paper (Figure 6) and Experiment 8. 

#### Main Result 9: Figure 6(e)
Figure 6(e) shows the average success rate for each billing period length (in weeks). <br>
Please refer to Section 8 of the paper (Figure 6) and Experiment 9. 

#### Main Result 10: Figure 6(f) 
The result is Figure 6(f), showing the average success rate for each number of toll stations. <br>
Please refer to Section 8 of the paper (Figure 6) and Experiment 10. 

#### Main Result 11: cd attack
The results are the ASRs regarding the cd attack, shown in Table 1. <br>
The results are w.r.t wallet ranges [0, 10], [10, 20], and [20, 40]. The number of plausible wallets includes
91, 721, and 2000 and ASRs include 51%, 11%, and 0.28%. <br>
Please refer to Sections 5.1, 7 of the paper (Table 1) and Experiment 11.

#### Main Result 12: Figure 3
The result in Figure 3 shows the distribution of success rates across all plausible wallets within the range [w<sub>l</sub>, w<sub>u</sub>]. <br>
The results are w.r.t the tsd-attack and the wallet ranges [0, 10], [10, 20], and [20, 40]. <br> 
Please refer to Section 5.2.2 and Experiment 12.  

#### Main Result 13: Figure 5
The result in Figure 5 shows the distribution of success rates across all plausible wallets within the range [w<sub>l</sub>, w<sub>u</sub>]. <br>
The results are w.r.t the cd attack and the wallet ranges [0, 10], [10, 20], and [20, 40]. <br>
Please refer to Section 7 and Experiment 13.  

### Experiments
Here, we list all required experiments to generate our paper's results.
We describe each experiment as follows: 
 - How to execute it in detailed steps. <br>
 - What the expected result is. <br>
 - How long it takes and how much space it consumes on disk. (approximately) <br>
 - Which claim and results does it support, and how.

#### Experiment 1: tsd-attack
The experiment is about the evaluation of the tsd-attack. <br>
Run the file *tsd-attack.py* (in TSD-Attack folder), and the results will be written to the *tsd-attack.log* file. <br>
The results show the average success rate (ASR) and number of plausible wallets w.r.t the wallet range [w<sub>l</sub>, w<sub>u</sub>]. <br>
It takes about 2 minutes to get the results. <br>
The results show that the adversary's ASR is significantly high, 94%, affecting 61% of drivers, and nearly 54% affecting 14% of drivers. <br>
The results are shown in Table 1, Section 5.1.

#### Experiment 2: Figure 4(a)
The experiment is about the algorithm's effectiveness. <br>
Run the file *generate-figure4-a.py*, and the graph will be saved in *figure4-a.pdf*. <br>
For more details, see the generated log file named *figure4-a.log*. <br>
The result is Figure 4(a), showing the number of solutions per wallet balance. <br>
It takes about 2 minutes to get the results. <br>
The Figure shows that although solving a linear diophantine equation is NP-complete in general, the equation can be solved, given the real settings of Brisbane's ETC system. The graph shows that for wallets below 10$ (93 red points), the number of plausible solutions is one or two, meaning that a significant proportion of drivers (61.38%) have very low privacy. <br>
The result is shown in Figure 4(a), Section 5.2.3.

#### Experiment 3: Figure 4(b)
The experiment is about the algorithm's effectiveness. <br>
Run the file *generate-figure4-b.py*, and the graph will be saved in *figure4-b.pdf*. <br>
For more details, see the generated log file named *figure4-b.log*. <br>
Figure 4(b) shows the run-time (in ms) for each wallet balance. <br>
It takes about 2 minutes to get the results. <br>
The result is shown in Figure 4(b), Section 5.2.3. <br>
The Figure shows that although solving a linear diophantine equation is NP-complete in general, the equation can be solved quickly, given the real settings of Brisbane's ETC system. <br>
Note: Since the runtimes heavily depend on the hardware on which the code is executed, the results can vary significantly. However, the overall trend should be observable, i.e., the values
of green points should be equal to or higher than those of the blue points, and the values of blue points should be equal to or higher than those of the red points. The values should be on
the millisecond scale, with most measurements taking at most a few minutes.

#### Experiment 4: tsd-attack-with-heuristic
The experiment is about the evaluation of the tsd-attack using the first heuristic. <br>
Run the file *tsd-attack-with-heuristic.py* (in TSD-Attack folder), and the results will be written to the *tsd-attack-with-heuristic.log* file. <br>
The results show the thresholds, ASR, and APDs w.r.t the wallet range [w<sub>l</sub>, w<sub>u</sub>]. <br>
It takes about 20 minutes to get the results. <br>
The results show that ASR and APD metrics show an upward trend as the threshold decreases. This trend is particularly noticeable in larger wallet ranges ([20, 40], [40, 60]), indicating a contribution to the improvement in ASR compared to the lower ASRs before applying the heuristic. <br>
The results are shown in Table 2, Section 5.3.

#### Experiment 5: Figure 6(a)
The experiment is about the impact of toll price settings on privacy. <br>
Run the file *generate-figure6-a.py*, and the graph will be saved in *figure6-a.pdf*. <br> 
For more details, see the generated log file named *figure6-a.log*. <br>
The results show the average success rate w.r.t each toll price range [1, j], 1 <= j <= 10. <br>
It takes about 90 minutes to get the results; the needed space is about 10MB. <br>
Figure 6(a) demonstrates that the ASR increases as the toll price range gets larger. The ASR increases from zero to almost 96%. <br>
The result is shown in Figure 6(a), Section 8.

#### Experiment 6: Figure 6(b)
The experiment is about the impact of toll price settings on privacy. <br>
Run the file *generate-figure6-b.py*, and the graph will be saved in *figure6-b.pdf*. <br> 
For more details, see the generated log file named *figure6-b.log*. <br>
The results show the average success rate w.r.t each toll price range [1, j], 1 <= j <= 10. <br>
It takes about 90 hours to get the results; the needed space is about 1 GB. To facilitate the quick generation of the figure, 
we also provide the file *generate-figure6-b-condensed.py*, which takes the precomputed average success rates as input and
generates the figure. <br>
Figure 6(b) demonstrates that the ASR increases as the toll price range gets larger. The ASR increases from zero to almost 73%. <br>
The result is shown in Figure 6(b), Section 8.

#### Experiment 7: Figure 6(c)
The experiment is about the impact of toll price settings on privacy. <br>
Run the file *generate-figure6-c.py*, and the graph will be saved in *figure6-c.pdf*. <br> 
For more details, see the generated log file named *figure6-c.log*. <br>
The results show the average success rate w.r.t each toll price range [1, j], 1 <= j <= 10. <br>
It takes about 240 hours to get the results; the needed space is about 1 GB. To facilitate the quick generation of the figure, we also provide the file *generate-figure6-c-condensed.py*, which takes the precomputed average success rates as input and generates the figure.<br>
Figure 6(c) demonstrates that the ASR increases as the toll price range gets larger. The ASR increases from zero to almost 15%. <br>
The result is shown in Figure 6(c), Section 8.

#### Experiment 8: Figure 6(d)
The experiment is about the impact of wallet balances on privacy. <br>
Run the file *generate-figure6-d.py*, and the graph will be saved in *figure6-d.pdf*. <br>
For more details, see the generated log file named *figure6-d.log*. <br>
The result is Figure 6(d), showing the success rate for each wallet balance. <br>
It takes about 2 minutes to get the results. <br>
Overall, small wallet balances lead to higher ASRs. Figure 6(d) shows that drivers (above %75 of total drivers) with wallet balances below 35$ are more at risk of a privacy violation. <br>
The result is shown in Figure 6(d), Section 8.

#### Experiment 9: Figure 6(e)
The experiment is about the impact of billing period length on privacy. <br>
Run the file *generate-figure6-e.py*, and the graph will be saved in *figure6-e.pdf*. <br>
For more details, see the generated log file named *figure6-e.log*. <br>
The result is Figure 6(e), showing the ASR per each billing period length. <br> 
It takes about 5 hours to get the results. <br>
Figure 6(e) shows that a short billing period leads to a high average success rate. <br>
The result is shown in Figure 6(e), Section 8.

#### Experiment 10: Figure 6(f)
The experiment is about the impact of the number of toll stations on privacy. <br>
Run the file *generate-figure6-f.py*, and the graph will be saved in *figure6-f.pdf*. <br>
For more details, see the generated log file named *figure6-f.log*. <br>
The result is Figure 6(f), showing the ASR for each number of toll stations. <br>
It takes about 48 hours to get the results. To facilitate the quick generation of the figure, we also provide the file
*generate-figure6-f-condensed.py*, which takes the precomputed average success rates as input and generates the figure. <br>
Figure 6(f) illustrates that the algorithm's ASR remains high for a low number of toll stations. <br>
The result is shown in Figure 6(f), Section 8.

#### Experiment 11: cd attack
The experiment is about the evaluation of the cd attack (Section 7 of the paper). <br> 
Run the file *write-the-plausible-traces.py* (in CD-Attack folder), and the results will be written to the *cd-attack.log* file. <br>
The results show the average success rate (ASR) w.r.t the wallet ranges: [0, 10], [10, 20], [20, 40]. <br>
The ASR for approximately 61.38% of drivers is around 51%, which is relatively high, and the ASR for approximately 14.31% is relatively low, i.e., 11%. <br>
It takes about 30 minutes to get the results. The results are shown in Table 1, Section 5.1. <br>
Folder *CD-attack-data* inside the CD-Attack folder contains data generated by running the file *write-the-plausible-traces.py*
and comprises three subfolders: *Wallet-range[0, 10]*, *Wallet-range[10, 20]*, and *Wallet-range[20, 40]*. 
Each subfolder contains three files: *plausible_traces.txt*, *partitions.txt*, and *distribution-SR.txt*. 
These files respectively represent all plausible traces, all partitions, and all success rates corresponding to the wallet range.


#### Experiment 12: Figure 3
The experiment is about the distribution of success rates across the plausible traces within the range [w<sub>l</sub>, w<sub>u</sub>]. <br>
Run the file *generate-figure3.py*, and the graph will be saved in *figure3.png*. <br>
For more details, see the generated log file named *figure3.log*. <br>
The result in Figure 3 shows box plots indicating the distribution of success rates per range [w<sub>l</sub>, w<sub>u</sub>]. <br>
It takes about 2 minutes to get the results. <br>
The figure shows that almost all the success rates (SRs) within the range of [0, 10] are 100% (shown in the first box plot). <br>
The result is shown in Figure 3, Section 5.2.2.


#### Experiment 13: Figure 5
The experiment is about the distribution of success rates across the plausible traces within the range [w<sub>l</sub>, w<sub>u</sub>]. <br>
Run the file *generate-figure5.py*, which reads the file *success-rates.txt*, including three lists of success rates, each of
which corresponds to the following wallet ranges: [0, 10], [10, 20], [20, 40]. After running the file, the graph will be saved
in a pdf named *figure5.png*. <br>
For more details, see the generated log file named *figure5.log*. <br>
The result is Figure 5, showing box plots indicating the distribution of success rates per range [w<sub>l</sub>, w<sub>u</sub>]. <br>
It takes about 1 minute to get the results. <br>
The figure shows that half of the success rates (SRs) corresponding to the range of [0, 10] are nearly 50%, while the other half falls between 25% and 50% (shown in the first box plot). <br>
The result is shown in Figure 5, Section 7.
