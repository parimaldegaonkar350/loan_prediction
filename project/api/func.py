import pickle
def loan_predictor(data):
    loan_amt=int(data['loan_amt'])
    int_rate=float(data['int_rate'])
    emp_length=float(data['emp_length'])
    annual_inc=float(data['annual_inc'])
    dti=float(data['dti'])
    delinq_2yrs=float(data['delinq_2yrs'])
    revol_util=float(data['revol_util'])
    total_acc=float(data['total_acc'])
    longest_credit_length=float(data['longest_credit_length'])
    months_60=int(data['months_60'])
    verified=int(data['verified'])
    MORTGAGE=int(data['MORTGAGE'])
    OWN=int(data['OWN'])
    RENT=int(data['RENT'])
    model=pickle.load(open(r'C:\Users\User\AppData\Local\Programs\Python\Python38-32\Scripts\best_model_dec_tree.pickle','rb'))
    input=[[loan_amt,int_rate,emp_length,annual_inc,dti,delinq_2yrs,revol_util,total_acc,longest_credit_length,months_60,verified,MORTGAGE,OWN,RENT,]]
    output=model.predict(input)
    return output[0]
