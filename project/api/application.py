from flask import Flask,request,render_template,jsonify
import func
app=Flask(__name__)
@app.route('/loan_prediction',methods=['POST'])
def loan_prediction():
    data=request.form
    print(data)
    prediction=func.loan_predictor(data)
    if int(prediction)==1:
        prediction='bad loan'
    else:
        prediction='good loan'
#return
if __name__=='__main__':
    app.run(host='0.0.0.0',port='5002')