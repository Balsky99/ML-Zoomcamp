#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle

model_file = f'model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)
    
client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

X = dv.transform([client])
model.predict_proba(X)[0,1]

