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

# Put information in tuple
evidence = []
label = []
for row in df.itertuples(): 
    user_session = [
        row.Administrative, row.Administrative_Duration, row.Informational,
        row.Informational_Duration, row.ProductRelated, row.ProductRelated_Duration,
        row.BounceRates, row.ExitRates, row.PageValues, row.SpecialDay, row.Month,
        row.OperatingSystems, row.Browser, row.Region, row.TrafficType, row.VisitorType,
        row.Weekend
    ]
    evidence.append(user_session)
    label.append(row.Revenue)
shopping = (evidence, label)

# return shopping