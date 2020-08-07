#import csv
import pandas as pd
import numpy as np
#data_file = sys.argv['shopping.csv']
data_file = 'shopping.csv'

# Additional functions

def numeric_conversion(shopping):
    """
    Function that converts all non numeric data in shopping
    dataset to numeric data.
    """
    # Month data
    conditions = [
    shopping['Month'] == 'Jan',
    shopping['Month'] == 'Feb',
    shopping['Month'] == 'Mar',
    shopping['Month'] == 'Apr',
    shopping['Month'] == 'May',
    shopping['Month'] == 'June',
    shopping['Month'] == 'Jul',
    shopping['Month'] == 'Aug',
    shopping['Month'] == 'Sep',
    shopping['Month'] == 'Oct',
    shopping['Month'] == 'Nov',
    shopping['Month'] == 'Dec'
    ]
    outputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    shopping['Month'] = np.select(conditions, outputs)
    # Weekend
    conditions = [shopping['Weekend'] == True]
    outputs = [1]
    shopping['Weekend'] = np.select(conditions, outputs, 0)
    # Visitor type
    conditions = [shopping['VisitorType'] == 'Returning_Visitor']
    outputs = [1]
    shopping['VisitorType'] = np.select(conditions, outputs, 0)
    # Revenue
    conditions = [shopping['Revenue'] == True]
    outputs = [1]
    shopping['Revenue'] = np.select(conditions, outputs, 0)



shopping_df = pd.read_csv(data_file)

numeric_conversion(shopping_df)

print(shopping_df.head())

evidence = []
label = []
shopping = (evidence, label)