#!/usr/bin/python3
import joblib
import pandas as pd

model = joblib.load('profit.pkl')
ohe = joblib.load('state_ohe.pkl')

class Profit:
      
    def __init__(self,data):
        self.data = data
        
    def predict(self):
        d_data = ohe.transform(data)
        predict = model.predict(d_data)[0]
        print(f"This approximate profit made by the startup is: ${predict}\n")
                
if __name__ == "__main__":
    print("************************")
    print("Statup Profit Calculator")
    print("************************\n\n")
    rnd = float(input('Enter Rnd Cost: '))
    admin = float(input('Enter Administation Cost: '))
    market = float(input('Enter Marketing Spend: '))
    city = input('Enter State [New York,California,Florida]: ')
    data = pd.DataFrame([rnd,admin,market,city],index=['R&D Spend', 'Administration', 'Marketing Spend', 'State']).T
    obj = Profit(data)
    obj.predict()
