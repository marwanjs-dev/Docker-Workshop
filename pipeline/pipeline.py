import sys
import pandas as pd

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2, 3], "month": [month, month, month], "value": [10, 20, 30]})