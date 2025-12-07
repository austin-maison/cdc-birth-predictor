import csv
from pathlib import Path


# Get relative paths to input and output directories
RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
INTERIM_DIR = Path(__file__).resolve().parents[1] / "data" / "interim"

# Input and output files
input_file = RAW_DIR / "raw_data.txt"
output_file = INTERIM_DIR / "raw_data.csv"

# Enumerate slices of data to be used
fields = [
    (12, 14),   # birth month (01-12)
    (18, 22),   # time of birth (0000-2359)
    (22, 23),   # day of week (1-7)
    (49, 50),   # birth place (1-3)
    (74, 76),   # mom age (12-50)
    (83, 84),   # mom nativity (1-3)
    (123, 124), # mom education (1-9)
    (237, 239), # num of prenatal visits (00-99)
    (250, 251), # enrolled in WIC (Y,N,U)
    (268, 269), # cigarette use (Y,N,U)
    (282, 286), # mom bmi (13.0-69.9,99.9)
    (312, 313), # pre-preg diabetes (Y,N,U)
    (313, 314), # gestational diabetes (Y,N,U)
    (314, 315), # pre-preg hypertension (Y,N,U)
    (315, 316), # gestational hypertension (Y,N,U)
    (316, 317), # hypertension eclampsia (Y,N,U)
    (317, 318), # previous pre-term birth (Y,N,U)
    (324, 325), # infertility treatment (Y,N,U)
    (330, 331), # previous c-section (Y,N,U)
    (352, 353), # no infections (1,0,9)
    (382, 383), # induction (Y,N,U)
    (384, 385), # steroids (Y,N,U)
    (385, 386), # antibiotics (Y,N,U)
    (387, 388), # anesthesia (Y,N,U)
    (407, 408), # delivery method (1,2,9)
]

# Column names for CSV
headers = ['month', 'time', 'day', 'place', 'm_age', 'm_nativity', 'm_edu',
           'num_of_prenatals', 'WIC', 'smoker', 'm_bmi', 'pre_diabetes',
           'gest_diabetes', 'pre_hypertension', 'gest_hypertension',
           'eclampsia', 'preterm_births', 'infert_treatment',
           'prev_c_section', 'no_infections', 'induction', 'steroids',
           'antibiotics', 'anesthesia', 'delivery_method']

with open(input_file, "r") as f_in, open(output_file, "w", newline="") as f_out:
    writer = csv.writer(f_out)
    writer.writerow(headers)

    for line in f_in:
        row = [line[start:end].strip() for start, end in fields]
        writer.writerow(row)
