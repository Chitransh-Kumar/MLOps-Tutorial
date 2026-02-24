# DVC (Data Version Control)

It is a tool to version datasets, machine learning models and pipelines - similar to Git for code versioning.

---

## Why do we need DVC?

1. Git cannot handle large data.

2. ML Experiments are harder to track.

## What DVC actually does?

1. Version control for data.

    - DVC stores lightweight metadata files in Git.

    - Actual data files stored in remote storages (S3, GDrive, etc.)

2. Reproducibility.

    - DVC tracks: Data, Parameters, Code, Dependencies.

3. Experiment Tracking.

---

## DVC Workflow:

1. Initialize Project.

```
git init
dvc init

git add .
git commit -m "Initialized DVC"
```

2. Add the dataset.

    - DVC creates dataset.csv.dvc, moves actual data in cache and stops Git from tracking large file.

```
dvc add data/dataset.csv

git add data/dataset.csv.dvc .gitignore
git commit -m "Track dataset with DVC"
```

3. Setup Remote Storage

```
dvc remote add -d storage s3://mybucket

dvc push
```

4. Modify dataset.

```
dvc add data/dataset.csv
git commit -m "Updated dataset"
dvc push
```

5. Define Pipeline stages.

**Stage 1**: Preprocessing:

```
dvc stage add -n preprocess \
    -d preprocess.py \
    -d data/raw.csv \
    -o data/clean.csv \
    python preprocess.py
```

Meaning: 

- Name = preprocess

- Depends on = preprocess.py, raw.csv,

- Output = clean.csv

**Stage 2**: Training:

```
dvc stage add -n train \
    -d train.py \
    -d data/clean.csv \
    -o model.pkl \
    python train.py
```

6. Reproduction.

    - DVC checks whether any dataset changed / preprocessing script changed / training script changed. If yes, then it runs only that stage.

```
dvc repro
```

