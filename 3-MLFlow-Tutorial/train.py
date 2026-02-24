from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import mlflow
import mlflow.sklearn

X, y= load_iris(return_X_y= True)

X_train, X_test, y_train, y_test= train_test_split(
    X, y, test_size= 0.2, random_state= 42
)

mlflow.set_experiment("Iris Classification")

learning_rate= 0.01
max_iter= 10

with mlflow.start_run():

    mlflow.log_param("Learning_Rate", learning_rate)
    mlflow.log_param("Max_Iterations", max_iter)

    model= LogisticRegression(max_iter= max_iter)
    model.fit(X_train, y_train)

    y_pred= model.predict(X_test)

    accuracy= accuracy_score(y_test, y_pred)

    mlflow.log_metric("Accuracy", accuracy)

    mlflow.sklearn.log_model(model, "model")

    print(f"Accuracy: {accuracy}")

