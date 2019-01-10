from tiingo import TiingoClient
import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd

import scipy
# import statsmodels.api as sm


from sklearn import mixture as mix
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


import bt
import ffn
import jhtalib as jhta
import datetime

# import matplotlib as plt
import seaborn as sns
sns.set()


# Get
# data from Tiingo


config = {}

# To reuse the same HTTP Session across API calls (and have better performance), include a session key.
config['session'] = True

# If you don't have your API key as an environment variable,
# pass it in via a configuration dictionary.
config['api_key'] = "539f5b3fef6e2386a8e71ad5ba2a2b4fbc55d90a"

# Initialize

client = TiingoClient(config)
# ticker_history = client.get_dataframe("GOOGL")

Real_Es_Sector = ['IIPR', 'MJNE', 'PRRE',
                  'GRWC', 'ZDPY', 'TURV',
                  'AGTK', 'DPWW', 'CGRA',
                  'DPWWD', 'FUTL', 'FTPM']


try:
    for i in range(len(Real_Es_Sector)):
        df = pd.DataFrame({"Name": list(dict.values(
            client.get_ticker_metadata((Real_Es_Sector[i]))))[5]})


except:
    pass

# try:
#     for i in range(len(Real_Es_Sector)):
#         #         df = pd.DataFrame(len(Real_Es_Sector))

#         x = print(
#             list(dict.values(client.get_ticker_metadata((Real_Es_Sector[i]))))[5])
# except:
#     pass
