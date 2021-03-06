import csv
import sys
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


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
    labels = []
    for row in df.itertuples(): 
        user_session = [
            row.Administrative, row.Administrative_Duration, row.Informational,
            row.Informational_Duration, row.ProductRelated, row.ProductRelated_Duration,
            row.BounceRates, row.ExitRates, row.PageValues, row.SpecialDay, row.Month,
            row.OperatingSystems, row.Browser, row.Region, row.TrafficType, row.VisitorType,
            row.Weekend
        ]
        evidence.append(user_session)
        labels.append(row.Revenue)
    shopping = (evidence, labels)
    return shopping


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model_kn = KNeighborsClassifier(n_neighbors=1)
    model_kn.fit(evidence, labels)
    return model_kn


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    positives = 0
    negatives = 0
    sensitivity = 0
    specificity = 0
    total = 0
    for actual, predicted in zip(labels, predictions):
        total += 1
        if actual == 1:
            positives += 1
            if predicted == 1:
                sensitivity += 1
        if actual == 0:
            negatives += 1
            if predicted == 0:
                specificity += 1
    sensitivity_prop = sensitivity / positives
    specificity_prop = specificity / negatives
    result = (sensitivity_prop, specificity_prop)
    return result


if __name__ == "__main__":
    main()
