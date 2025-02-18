import pandas as pd
data = pd.read_csv('data/Cardiovascular_Disease_Dataset.csv')

heart_disease_filter = data['target'] == 1
print('TEST CASES FOR POSITIVE HEART DISEASE')
print(data[heart_disease_filter].head(5))

no_heart_disease_filter = data['target'] == 0
print('TEST CASES FOR NO HEART DISEASE')
print(data[no_heart_disease_filter].head(5))