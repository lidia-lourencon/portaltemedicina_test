import sys, getopt, os
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier


def log(message):
    print()
    print(message)


def main(argv):
    inputfile = ""

    try:
        opts, _ = getopt.getopt(argv, "hi:o:", ["inputfile="])
    except getopt.GetoptError:
        log("--inputfile <inputfile>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            log("sex_predictor.py --inputfile <inputfile>")
            sys.exit()
        elif opt in ("-i", "--inputfile"):
            inputfile = arg

    if not os.path.isfile(inputfile):
        log("Error: file not found")
        sys.exit()

    log("Starting")
    columns = [
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "oldpeak",
        "slope",
        "ca",
        "thal",
        "nar",
        "hc",
        "sk",
        "trf",
    ]

    learn_data = pd.read_csv("learn_data.csv", delimiter=",", usecols=columns)

    log("Learning...")
    x_train = []
    y_train = []
    for _, rows in learn_data.iterrows():
        aux_list = list(rows)
        aux_list.pop(1)  # Remove sex

        x_train.append(aux_list)
        y_train.append(rows["sex"])

    log("Reading csv...")
    columns.pop(1)
    predict_csv = pd.read_csv(inputfile, delimiter=",", usecols=columns)
    predict_data = [list(rows) for index, rows in predict_csv.iterrows()]

    # Handle nan values inside list
    imp = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
    imp = imp.fit(x_train)

    x_trin_imp = imp.transform(x_train)
    predict_data_imp = imp.transform(predict_data)

    # Predict
    dtc_clf = DecisionTreeClassifier()
    dtc_clf = dtc_clf.fit(x_trin_imp, y_train)
    result = dtc_clf.predict(predict_data_imp)

    # Write file with result
    log("Writing result file...")
    df = pd.DataFrame({"sex": result})
    df.to_csv("newsample_PREDICTIONS_Lidia.csv", sep=",", index=False)

    log("End")


if __name__ == "__main__":
    main(sys.argv[1:])
