import pandas as pd
import json

from src.fetch import get_data
from os.path import abspath

data = get_data()

# Write string to CSV file
with open(abspath("./data/superforecasts.csv"), 'w') as f:
    f.write(data)
