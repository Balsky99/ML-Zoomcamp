#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pickle
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("https://raw.githubusercontent.com/alexeygrigorev/datasets/master/AER_credit_card_data.csv")

features = ['reports', 'share', 'expenditure', 'owner']
dicts = df[features].to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X = dv.fit_transform(dicts)
y = df.card.values

output_file = f'model.bin'
model = LogisticRegression(solver='liblinear').fit(X, y)

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)


# In[ ]:




