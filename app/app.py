from flask import Flask
import joblib
from flask.globals import request
from flask.json import jsonify
import pandas as pd


app=Flask(__name__)

@app.route('/api/DiabetesModel',methods=['POST'])

def makePrediction():
     data=request.get_json()
     print(data)
     prediction=list(loaded_model.predict(pd.DataFrame(data)))
     return jsonify(prediction)
     
if __name__=='__main__':
    loaded_model=joblib.load(open('model.pkl','rb'))
    app.run(debug=True)

