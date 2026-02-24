# MLFlow:

It is a tool to manage the ML lifecycle. 

It mainly:
    
    - Tracks experiments.

    - Log parameters.

    - Log metrices.

    - Store artifacts (models, plots, files, etc.)

    - Register and manages model.

    - Deploy model.

## Core concepts and components:

1. Experiment:

    - One experiment = Logical container. Inside one experiment, there are multiple runs.

2. Run:

    - One run = One training execution.

3. Parameters:

    - Inputs the user can control (Eg. Learning rate, Batch size, Epochs, etc.)

4. Metrics:

    - Performance numbers (Eg. Accuracy, Loss, RMSE, etc.)

5. Artifacts:

    - Saved outputs (Eg. Model files, Confusion matrix, Plots, etc.)

6. Model Registry:

    - Production-level feature (Store models and Version models)

## How to view results:

```
mlflow ui
```