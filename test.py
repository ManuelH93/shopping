import csv
import sys
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
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

    return shopping


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model


# Load data from spreadsheet and split into train and test sets


evidence, labels = load_data('shopping.csv')
X_train, X_test, y_train, y_test = train_test_split(
    evidence, labels, test_size=TEST_SIZE
)

print(evidence[0])