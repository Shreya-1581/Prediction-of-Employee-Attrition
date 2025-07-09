import pandas as pd
import pickle

MODEL_VERSION="1.0"

with open("D:\Downloads\Employee\model\model.pkl","rb") as f:
    model=pickle.load(f)

def predict_output(user_input: dict):
    
    input_df = pd.DataFrame([user_input])
    output=model.predict(input_df)
    return output

    