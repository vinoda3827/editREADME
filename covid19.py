# -*- coding: utf-8 -*-
"""covid19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S1abWnZXkd6ZZ9IgOgru9JXKVN23FkQw
"""

import requests
url="https://data.covid19india.org/v4/min/timeseries.min.json"
data=requests.get(url)
data

var=data.json()

var