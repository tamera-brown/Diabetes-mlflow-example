from flask import Flask
from flask.globals import request
from flask.json import jsonify
import pandas as pd
import joblib

modelpath = "mlflow_diabetes_model"


app=Flask(__name__)

@app.route('/api/DiabetesModel',methods=['POST'])

def makePrediction():
     data=request.get_json()
     print(data)
     prediction=list(loaded_model.predict(pd.DataFrame(data)))
     return jsonify(prediction)
     
if __name__=='__main__':
  loaded_model=joblib.load(open(modelpath+'/model.pkl','rb'))
  app.run(debug=True,host='0.0.0.0')