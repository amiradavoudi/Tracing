# Artifact Appendix

Paper title: **Why Privacy-Preserving Protocols Are Sometimes Not Enough: A Case Study of the Brisbane Toll Collection Infrastructure**

Artifacts HotCRP Id: **#6**

Requested Badge: **Reproducible**

## Description
This repository contains the source codes for reproducing the results shown in Tables 1 and 2. The codes also generate the plots of the figures in the main body of the paper, including 2(a), 2(b), 3(a), 3(b), 3(c), 3(d), 3(e), 3(f), as well as Figures 5 and 7 shown in the appendix.
### Security/Privacy Issues and Ethical Concerns
There is no Security/Privacy Issues and Ethical Concerns.

## Basic Requirements
64-bit version of Windows 10 1809 and later, or Windows Server 2019 and later <br>
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
64-bit version of Windows 10 1809 and later, or Windows Server 2019 and later. <br>
Microsoft Visual C++ 2015-2022 Redistributable Package (x64). [Download link](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022) <br>
Download *IBM ILOG CPLEX Optimization Studio Free Edition* (Windows edition) from the below link. [Download link](https://www.ibm.com/account/reg/us-en/signup?formid=urx-20028) <br>
Note that you should fill out the form to download the file *IBM ILOG CPLEX Optimization Studio Free Edition*, namely *cos_installer_preview-22.1.1.0.R0-M08SVML-win-x86-64.exe*.

### Estimated Time and Storage Consumption
Estimated Time depends on the file and varies between 2 mintues up to 3 days. <br>
5 GB free disk space

## Environment
In the following, we describe how to access our artifact and all related and necessary data and software components. <br>
Afterward, we describe how to set up everything and how to verify that everything is set up correctly.

### Accessibility
Describe how to access your artifacts via persistent sources.

### Set up the environment
First, install *Microsoft Visual C++ 2015-2022 Redistributable Package* as it is needed by the program in the next step. <br>
Install *IBM ILOG CPLEX Optimization Studio Free Edition*. Please follow the instructions during the installation. <br> 
Install Python 3.11.4 or later. (Add python.exe to PATH	) <br>
The following python packages are required: <br>
docplex 2.23.222 or later <br>
numpy  1.25.2 <br>
matplotlib 3.5.2 or later <br>
Node.js 18.17.1

### Testing the Environment
File *test.py* includes all the packages required for the exectution of the source codes in this project. <br>
If the file is executed without any error, it means all the required packages are installed properly. <br>
Run the file *test.py*, and it should not produce any errors.

## Artifact Evaluation
This section includes all the steps required to evaluate our artifact's functionality and validate our paper's key results and claims. <br>
We highlight our paper's main results and claims in the first subsection and we describe the experiments that support our claims in the subsection after that.

### Main Results and Claims
Here, we list all our paper's main results and claims that are supported by our submitted artifacts.

#### Main Result 1: toll-based-algorithm
The results are the ASRs regarding the toll-based attacking algorithm, shown in Table 1. <br>
The results are w.r.t wallet ranges [0 ,10], [10, 20], and [20, 40]. <br>
The number of plausible wallets include 91, 721, and 2000 and the ASRs include 61.38%, 14.31% and 11.12%. <br>
Please refer to Section 5.1 (Table 1) and the experiment 1. 

#### Main Result 2: Figure 2(a)
The result is Figure 2(a) showing the number of solutions per each wallet balance (in dollar). <br>  
Please refer to Section 5.1.3 (Figure 2) and the experiment 2. 

#### Main Result 3: Figure 2(b)
The result is Figure 2(b) showing the run-time (in ms) for each wallet balance (in dollar). <br>
Please refer to Section 5.1.3 (Figure 2) and the experiment 3. 

#### Main Result 4: toll-based-algorithm-with-heuristic
The ASRs and APDS regarding the toll-based attacking algorithm using the first heuristic are shown in Table 2. <br>
The results are w.r.t wallet ranges [0, 10], [10, 20], and [20, 40]. <br> 
Please refer to Section 5.2 (Table 2) and the experiment 4. 

#### Main Result 5: Figure 3(a)
The result is Figure 3(a) showing the average success rate for each toll price range w.r.t wallet range [0, 10]. <br>
Please refer to Section 5.3 (Figure 3) and the experiment 5.

#### Main Result 6: Figure 3(b)
The result is Figure 3(b) showing the average success rate for each toll price range w.r.t wallet range [10, 20]. <br>
Please refer to Section 5.3 (Figure 3) and the experiment 6.

#### Main Result 7: Figure 3(c)
The result is Figure 3(c) showing the average success rate for each toll price range w.r.t wallet range [20, 40]. <br>
Please refer to Section 5.3 (Figure 3) and the experiment 7.

#### Main Result 8: Figure 3(d)
The result is Figure 3(d) showing the success rate for each wallet balance (in dollar). <br>
Please refer to Section 5.3 (Figure 3) and the experiment 8. 

#### Main Result 9: Figure 3(e)
The result is Figure 3(e) showing the average success rate for each billing period length(in week). <br>
Please refer to Section 5.3 (Figure 3) and the experiment 9. 

#### Main Result 10: Figure 3(f) 
The result is Figure 3(f) showing the average success rate for each number of toll station. <br>
Please refer to Section 5.3 (Figure 3) and the experiment 10. 

#### Main Result 11: cycle-based-algorithm
The results are the ASRs regarding the cycle-based attacking algorithm, shown in Table 1. <br>
The results are w.r.t wallet ranges [0, 10], [10, 20], and [20, 40]. The number of plausible wallets include
91, 721, and 2000 and the ASRs include 51%, 11% and 0.28%. <br>
Please refer to Sections 5.1 (Table 1), 6.2 and the experiment 11.

#### Main Result 12: Figure 5
The result is Figure 5 showing the distribution of success rates across all plausible wallets with the range [w<sub>l</sub>, w<sub>u</sub>]. <br>
The results are w.r.t the toll-based attacking algorithm and the wallet ranges [0, 10], [10, 20], and [20, 40]. <br> 
Please refer to Appendix F and the experiment 12.  

#### Main Result 13: Figure 7
The result is Figure 7 showing the distribution of success rates across all plausible wallets with the range [w<sub>l</sub>, w<sub>u</sub>]. <br>
The results are w.r.t the cycle-based attacking algorithm and the wallet ranges [0, 10], [10, 20], and [20, 40]. <br>
Please refer to Appendix M and the experiment 13.  

### Experiments
Here, we list all required experiments to generate our paper's results.
We describe each experiment as follows: 
 - How to execute it in detailed steps. <br>
 - What the expected result is. <br>
 - How long it takes and how much space it consumes on disk. (approximately) <br>
 - Which claim and results does it support, and how.

#### Experiment 1: toll-based-algorithm
The experiment is about the evaluation of the toll-based attacking algorithm. <br>
Run the file *toll-based-attacking-algorithm.py* and the results will be written to *toll-based-algo.log* file. <br>
The results show the average success rate (ASR) and number of plausible wallets w.r.t the wallet range [w<sub>l</sub>, w<sub>u</sub>]. <br>
It takes about 2 minutes to get the results. <br>
The results show that the adversary's ASR is significantly high, 94%, affecting 61% of drivers and nearly 54% affecting 14% of drivers. <br>
The results are shown in Table 1, Section 5.1.

#### Experiment 2: Figure 2(a)
The experiment is about the algorithm's effectiveness. <br>
Run the file *generate-figure2(a).py* and the graph will be saved in a pdf file name *solutions.pdf*. <br>
For more details see the generated log file named *figure2(a).log*. <br>
The result is Figure 2(a) showing the number of solutions per each wallet balance. <br>
It takes about 2 minutes to get the results. <br>
The Figure shows that although solving a linear diophantine equation is NP-complete in general, the equation can be solved, given the real settings of Brisbane's ETC system. The graph shows that for wallets below 10$ (93 red points), the number of plausible solutions is one or two, meaning that a significant proportion of drivers (61.38%) have very low privacy. <br>
The result is shown Figure 2(a), Section 5.1.3.

#### Experiment 3: Figure 2(b)
The experiment is about the algorithm's effectiveness. <br>
Run the file *generate-figure2(b).py* and the graph will be saved in a pdf file name *runtimes.pdf*. <br>
For more details see the generated log file named *figure2(b).log*. <br>
The result is Figure 2(b) showing the run-time (in ms) for each wallet balance. <br>
It takes about 2 minutes to get the results. <br>
The result is shown Figure 2(b), Section 5.1.3. <br>
The Figure shows that although solving a linear diophantine equation is NP-complete in general, the equation can be solved quickly, given the real settings of Brisbane's ETC system. <br>
Note: Note: Since the runtimes heavily depend on the hardware on which the code is executed, the results will probably vary.

#### Experiment 4: toll-based-algorithm-with-heuristic
The experiment is about the evaluation of the toll-based attacking algorithm using the first heuristic. <br>
Run the file *toll-based-attacking-algorithm-with-heuristic.py* and the results will be written to *toll-based-algo-with-heuristic.log* file. <br>
The results show the thresholds, ASR and APDs w.r.t the wallet range [w<sub>l</sub>, w<sub>u</sub>]. <br>
It takes about 2 minutes to get the results. <br>
The results shows that the metrics ASR and APDs show an upward trend as the threshold decreases. This trend is particularly noticeable in larger wallet ranges ([20, 40], [40, 60]), indicating a contribution to the improvement in ASR compared to the lower ASRs before applying the heuristic. <br>
The results are shown in Table 2, Section 5.2.

#### Experiment 5: Figure 3(a)
The experiment is about the impact of toll price settings on privacy. <br>
Run the file *generate-figure3(a).py* and the results will be written to *figure3(a).log* file. <br>
The results show the average success rate w.r.t each toll price range [1,j], 1 <= j <= 10. <br>
It takes about 90 minutes to get the results, and the amount of needed space is about 10MB. <br>
Figure 3(a) demonstrates that the ASR increases as the toll price range gets larger. The ASR increases from zero to almost 96%. <br>
The result is shown Figure 3(a), Section 5.3.

#### Experiment 6: Figure 3(b)
The experiment is about the impact of toll price settings on privacy. <br>
Run the file *generate-figure3(b).py* and the results will be written to *figure3(b).log* file. <br>
The results show the average success rate w.r.t each toll price range [1,j], 1 <= j <= 10. <br>
It takes about 90 hours to get the results, and the amount of needed space is about 1GB. <br>
Figure 3(b) demonstrates that the ASR increases as the toll price range gets larger. The ASR increases from zero to almost 73%. <br>
The result is shown Figure 3(b), Section 5.3.

#### Experiment 7: Figure 3(c)
The experiment is about the impact of toll price settings on privacy. <br>
Run the file *generate-figure3(c).py* and the results will be written to *figure3(c).log* file. <br>
The results show the average success rate w.r.t each toll price range [1,j], 1 <= j <= 10. <br>
It takes about 240 hours to get the results, and the amount of needed space is about 1GB. <br>
Figure 3(c) demonstrates that the ASR increases as the toll price range gets larger. The ASR increases from zero to almost 15%. <br>
The result is shown Figure 3(c), Section 5.3.

#### Experiment 8: Figure 3(d)
The experiment is about the impact of wallet balances on privacy. <br>
Run the file *generate-figure2(d).py* and the graph will be saved in a pdf file name *success-rate-wallet.pdf*. <br>
For more details see the generated log file named *figure2(d).log*. <br>
The result is Figure 3(d) showing the success rate for each wallet balance. <br>
It takes about 2 minutes to get the results. <br>
Overall, small wallet balances lead to higher ASRs. Figure 3(d) shows that drivers (above %75 of total drivers) with wallet balances below 35$ are more at risk of a privacy violation. <br>
The result is shown Figure 3(d), Section 5.3.

#### Experiment 9: Figure 3(e)
The experiment is about the impact of billing period length on privacy. <br>
Run the file *generate-figure2(e).py* and the graph will be saved in a pdf file name *ASR-billing-period.pdf*. <br>
For more details see the generated log file named *figure2(e).log*. <br>
The result is Figure 3(e) showing the ASR per each billing period length. <br> 
It takes about 5 hours to get the results. <br>
Figure 3(e) shows that a short billing period leads to a high average success rate. <br>
The result is shown Figure 3(e), Section 5.3.

#### Experiment 10: Figure 3(f)
The experiment is about the impact of number of toll stations on privacy. <br>
Run the file *generate-figure2(f).py* and the graph will be saved in a pdf file name *ASR-num-of-tolls.pdf*. <br>
For more details see the generated log file named *figure2(f).log*. <br>
The result is Figure 3(f) showing the ASR for each number of toll stations. <br>
It takes about 48 hours to get the results. <br>
Figure 3(f) illustrates that the algorithm's ASR remains high for a low number of toll stations. <br>
The result is shown Figure 3(f), Section 5.3.

#### Experiment 11: cycle-based-algorithm
The experiment is about the evaluation of the cycle-based attacking algorithm. <br> 
To generate the results, the following three steps should be performed: <br>

(1) First, set the wallet range [w<sub>l</sub>, w<sub>u</sub>], where w_l and w_u indicate the lower and upper bounds of the range.
To set the range, in the file *write-the-plausible-traces.py* set the two variables *lower_bound_wallet* and *upper_bound_wallet*. 
For example, in the file the variables are set to 0 and 10 indicating the wallet range [0, 10]. 
Then, run the file *write-the-plausible-traces.py*, which generates all plausible traces corresponding to all
plausible wallet balances within the range [w<sub>l</sub>, w<sub>u</sub>], written to the file *plausible_traces.txt*. <br>
(2) Run the file *create_partitions.js* getting the file *plausible_traces.txt* as its
input and creates all the corresponding partitions, written to the file *partitions.txt*. <br>
(3) Run the file *cycle-based-attacking-algorithm.py* that computes the ASRs given the partitions
stored in the file *partitions.txt*. The results will be written to *cycle-based-algo.log* file. <br>
The results show the average success rate (ASR) w.r.t the wallet range [w<sub>l</sub>, w<sub>u</sub>]. <br>
The ASR for approximately 61.38% of drivers is around 51%, which is relatively high ,and the ASR for approximately 14.31% of drivers is relatively low, i.e., 11%. <br>
It takes about 2 minutes to get the results. <br>
The results are shown in Table 1, Section 5.1.

#### Experiment 12: Figure 5
The experiment is about the distribution of success rates across the plausible traces within the range [w<sub>l</sub>, w<sub>u</sub>]. <br>
Run the file *generate-figure5.py* and the graph will be saved in a pdf file name *distribution-of-SR.png*. <br>
For more details see the generated log file named *figure5.log*. <br>
The result is Figure 5 showing box plots indicating the distribution of success rates per range [w<sub>l</sub>, w<sub>u</sub>]. <br>
It takes about 2 minutes to get the results. <br>
The figure shows that almost all of the success rates (SRs) within the range of [0, 10]$ are 100% (shown in the first box plot). <br>
The result is shown Figure 5, Appendix F.

#### Experiment 13: Figure 7
The experiment is about the distribution of success rates across the plausible traces within the range [w<sub>l</sub>, w<sub>u</sub>]. <br>
Run the file *generate-figure7.py* which reads the file *distribution-SR.txt* including three lists of success rate each of
which corresponds to the following wallet ranges: [0, 10], [10, 20], [20, 40]. After running the file, the graph will be saved
in a pdf file name *distribution-of-SR-cycles.png*. <br>
For more details see the generated log file named *figure7.log*. <br>
The result is Figure 7 showing box plots indicating the distribution of success rates per range [w<sub>l</sub>, w<sub>u</sub>]. <br>
It takes about 1 minutes to get the results. <br>
The figure shows that half of the success rates (SRs) corresponding to the range of [0, 10]$ are nearly 50%, while the other half falls between 25% and 50% (shown in the first box plot). <br>
The result is shown Figure 7, Appendix M.

## Limitations
There is no limitations.

## Notes on Reusability
First, this section might not apply to your artifacts.
Use it to share information on how your artifact can be used beyond your research paper, e.g., as a general framework.
The overall goal of artifact evaluation is not only to reproduce and verify your research but also to help other researchers to re-use and improve on your artifacts.
Please describe how your artifacts can be adapted to other settings, e.g., more input dimensions, other datasets, and other behavior, through replacing individual modules and functionality or running more iterations of a specific part.
