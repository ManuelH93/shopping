#import csv
import pandas as pd
import numpy as np
#data_file = sys.argv['shopping.csv']
filename = 'shopping.csv'


df = pd.read_csv(filename)
# Convert month data in shopping dataset to numeric data.
conditions = [
df['Month'] == 'Jan',
df['Month'] == 'Feb',
df['Month'] == 'Mar',
df['Month'] == 'Apr',
df['Month'] == 'May',
df['Month'] == 'June',
df['Month'] == 'Jul',
df['Month'] == 'Aug',
df['Month'] == 'Sep',
df['Month'] == 'Oct',
df['Month'] == 'Nov',
df['Month'] == 'Dec'
]
outputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
df['Month'] = np.select(conditions, outputs)
# Convert weekend data in shopping dataset to numeric data.
conditions = [df['Weekend'] == True]
outputs = [1]
df['Weekend'] = np.select(conditions, outputs, 0)
# Convert wisitor type data in shopping dataset to numeric data.
conditions = [df['VisitorType'] == 'Returning_Visitor']
outputs = [1]
df['VisitorType'] = np.select(conditions, outputs, 0)
# Convert wevenue data in shopping dataset to numeric data.
conditions = [df['Revenue'] == True]
outputs = [1]
df['Revenue'] = np.select(conditions, outputs, 0)
print(df.info())
# Create separate dataframe for evidence and label
df_label = df['Revenue']
df.drop("Revenue", axis=1, inplace=True)


# Put information in tuple
evidence = df.values.tolist()
label = df_label.values.tolist()
shopping = (evidence, label)

for l1 in shopping:
    print(len(l1))

print(evidence[0])
for value in evidence[0]:
    print(type(value))
print(label[0])