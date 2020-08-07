#import csv
import pandas as pd
import numpy as np
#data_file = sys.argv['shopping.csv']
data_file = 'shopping.csv'

# Additional functions

def numeric_conversion(df):
    """
    Function that converts all non numeric data in shopping
    dataset to numeric data.
    """
    # Month data
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
    # Weekend
    conditions = [df['Weekend'] == True]
    outputs = [1]
    df['Weekend'] = np.select(conditions, outputs, 0)
    # Visitor type
    conditions = [df['VisitorType'] == 'Returning_Visitor']
    outputs = [1]
    df['VisitorType'] = np.select(conditions, outputs, 0)
    # Revenue
    conditions = [df['Revenue'] == True]
    outputs = [1]
    df['Revenue'] = np.select(conditions, outputs, 0)



shopping_df = pd.read_csv(data_file)

numeric_conversion(shopping_df)

#print(shopping_df.head())

evidence = []
label = []
shopping = (evidence, label)


print(len(shopping_df['Administrative'].tolist()))

tracker = 5
for row in shopping_df:
    #print(row)
    evidence.append(row[0:17])
    label.append(row[-1])
    tracker += -1
    if tracker < 0:
            break