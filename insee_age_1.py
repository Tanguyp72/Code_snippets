# Import useful libraries
import pandas as pd
import numpy as np

# Opening the national repartition of age in relation to first names
age_nat_insee = pd.read_csv("data/age_insee/nat2019.csv", sep=";", error_bad_lines=False, encoding = 'utf8')
age_nat_insee
