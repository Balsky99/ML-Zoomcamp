#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = f'model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('card')

@app.route('/predict', methods=['POST','GET'])
    
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0,1]
    card = y_pred>= 0.5

    result = {
        'card_probability' : float(y_pred),
        'card':bool(card)
    }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000) 