# CDC Birth Data Analysis



A predictive modeling project using CDC birth data to classify whether or not a delivery
will be a C-section.


## Overview


This project applies classification models to CDC birth records to predict C‑section
outcomes and attempts to identify key maternal and pregnancy factors associated with
them. The genesis of this project came out of a conversation I had with my wife after 
we noticed that, in our social circle, induced labor seemed to have a strong positive
correlation with having an unplanned C-section. We wanted to know if this was more 
broadly true, so I set out to test this hypothesis (it in fact has a negative 
correlation). Since then, the project has evolved into looking for *any* pre-birth 
predictors of C-sections. 


## Dataset

- **Source:** [CDC Birth Statistics](https://www.cdc.gov/nchs/data_access/VitalStatsOnline.htm), 
2024 birth data

- **Data:** `raw_data.txt`, fixed-width format, ~3.6M rows, ~280 columns

- **Processing:** Selected 25 relevant features and converted to csv format with
`raw_to_csv.py`, dropped rows with missing values, reformatted columns, and optimized 
data types using pandas

- **Outputs:** `raw_data.csv`, `processed_data.csv`


## Methodology

- **Tools:** Python, pandas, numpy, scipy, matplotlib, seaborn, scikit-learn

- **Models:** Decision Tree as a benchmark, Random Forest, Gradient Boosting  

- **Training:** Used 67/33 train test split on random sample of 10000 records for
experimentation and model selection, then on full dataset for final model

- **Hyperparameters:** Compared default settings with GridSearchCV tuning  

- **Evaluation:** Accuracy and recall, with emphasis on recall to minimize 
false negatives (critical in healthcare contexts)


## Results

- **Best model:** Random Forest

- **Accuracy score** = 79%, an 11.4% improvement over the trivial classifier

- **Recall score** = 54%

- **Most predictive features:** Previous C-sections, mother's BMI, number of prenatal visits, 
mother's age, mother's education, induced labor, use of antibiotics, time of day   


## Future work

The final results leave much to be desired for a healthcare context. However, comparing these
results to [a 2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10422959/) whose model 
achieves a 72% accuracy score, I believe that this is only the beginning of a fascinating and 
important line of investigation which deserves more attention.

One potential reason for the suboptimal performance is that the data doesn't include many of 
the known predictors of a C-section e.g. having twins, prolonged labor, fetal position, etc. 
It also doesn't distinguish between emergency C-sections and C-sections planned in advance.
However, I believe this can be seen as a strength rather than weakness. A further investigation 
of factors which are *not* known to be predictive of a C-section have the potential to 
contribute more to the understanding of C-sections than the already well-studied factors. And, 
indeed, this project shows that there is a nontrivial amount of signal to be found in a wide 
range of factors.


The future of this project lies in incorporating more pre-birth factors, both unintuitive and
well-established, to see just how far a predictive model can be pushed.