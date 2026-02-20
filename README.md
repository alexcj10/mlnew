# ML Project Setup Guide
A standard, reproducible setup process for Machine Learning and Data Science projects.

## 1. Create Project Folder

Creates a clean root folder for the project. Everything lives inside this folder.

```bash
mkdir project_name
cd project_name
```

## 2. Create Virtual Environment

Isolates project dependencies and prevents conflicts with system Python.

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

Tells the system to install and use packages only for this project.

**Windows**
```bash
venv\Scripts\activate
```

**Linux / Mac**
```bash
source venv/bin/activate
```

## 4. Upgrade Core Python Tools

Ensures latest and stable package handling.

```bash
pip install --upgrade pip setuptools wheel
```

## 5. Create Project Folder Structure

Keeps data, code, configs, and experiments organized. Matches production and industry standards.

```bash
mkdir data notebooks src configs logs tests
mkdir data/raw data/processed
mkdir src/features src/models src/training src/inference
```

## 6. Project Structure Overview

```
project_name/
├── data/
│   ├── raw/                  # Original, untouched data. Never modify this.
│   └── processed/            # Cleaned and transformed data ready for training.
│
├── notebooks/
│   └── eda.ipynb             # Exploratory analysis, visualizations, quick experiments.
│                             # Not used for final training or production code.
│
├── src/
│   ├── features/
│   │   └── build_features.py # Feature engineering logic. Transforms raw data into
│   │                         # model-ready inputs (encoding, scaling, new columns).
│   │
│   ├── models/
│   │   └── model.py          # Model definition. Defines architecture or loads a
│   │                         # pre-trained model (e.g. sklearn, PyTorch, XGBoost).
│   │
│   ├── training/
│   │   └── train.py          # Training entry point. Loads data, calls feature
│   │                         # engineering, trains model, saves it to disk.
│   │
│   └── inference/
│       └── predict.py        # Prediction logic. Loads saved model and runs it
│                             # on new data. Used in APIs or batch jobs.
│
├── configs/
│   └── config.yaml           # All tunable settings in one place: paths, hyperparameters,
│                             # model names, thresholds. No hardcoding in code.
│
├── logs/                     # Training logs, error logs, experiment outputs.
│
├── tests/
│   └── test_model.py         # Unit and integration tests for src/ code.
│
├── .env                      # Secret keys and environment variables. Never commit this.
├── .gitignore                # Files and folders Git should ignore.
├── requirements.txt          # All installed packages with exact versions.
└── README.md                 # Project documentation.
```

## 7. What Code Goes Where

**`src/features/build_features.py`**
Anything that transforms raw data before it reaches the model. Examples: handling missing values, encoding categorical columns, normalizing numerical columns, creating new derived columns.

**`src/models/model.py`**
The model definition itself. Examples: defining a neural network class, loading an XGBoost model, setting up a scikit-learn pipeline with a classifier.

**`src/training/train.py`**
The main script you run to train the model. It calls feature engineering, loads the data, trains the model defined in `model.py`, evaluates it, and saves the trained model to disk.

**`src/inference/predict.py`**
Loads the saved trained model and runs predictions on new, unseen data. This is what gets called inside a FastAPI endpoint or a batch prediction job.

**`configs/config.yaml`**
All settings that might change between runs. Examples: file paths, learning rate, number of epochs, model type, train/test split ratio. Nothing gets hardcoded in Python files.

**`notebooks/`**
Only for exploration and understanding the data. Once logic is finalized here, it gets moved into the appropriate `src/` file. Notebooks never get imported or called by other code.

## 8. Create Required Files

These files are needed for dependency tracking, configs, and execution.

**Windows**
```bash
type nul > requirements.txt
type nul > .gitignore
type nul > README.md
type nul > .env
type nul > configs/config.yaml
type nul > src/training/train.py
```

**Linux / Mac**
```bash
touch requirements.txt .gitignore README.md .env
touch configs/config.yaml
touch src/training/train.py
```

## 9. Install Common ML / DS Dependencies

Installs libraries used for data analysis, ML, APIs, and experiments. Installed inside venv only.

```bash
pip install numpy pandas scikit-learn matplotlib seaborn jupyter
pip install mlflow fastapi uvicorn python-dotenv
```

## 10. Save Installed Dependencies

Freezes exact package versions so anyone can recreate the same environment.

```bash
pip freeze > requirements.txt
```

Note: `requirements.txt` always stays in the project root, never inside `venv`.

## 11. Setup .gitignore

Prevents unnecessary or sensitive files from being pushed to GitHub.

```bash
echo venv/ >> .gitignore
echo __pycache__/ >> .gitignore
echo .ipynb_checkpoints/ >> .gitignore
echo .env >> .gitignore
echo *.log >> .gitignore
```

## 12. Write Training Entry Script

Single entry point to train models. Notebooks are not used for final training.

Edit `src/training/train.py`:

```python
def train():
    print("Training started")

if __name__ == "__main__":
    train()
```

## 13. Run Training Script

Confirms the project structure and environment are working correctly.

```bash
python src/training/train.py
```

## 14. Initialize Git Repository

Enables version control. Required for collaboration and deployment.

```bash
git init
git add .
git commit -m "Initial ML project setup"
```

## 15. Recreate Environment (If venv Is Deleted)

The venv folder is disposable and can be rebuilt anytime from `requirements.txt`.

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 16. Deactivate Virtual Environment

Exit the project environment safely.

```bash
deactivate
```

## Key Rules

- Never write code inside `venv`
- Never commit `venv` to GitHub
- Always activate venv before working
- All production code lives in `src/`
- Notebooks are for exploration only, not production

> Virtual environment isolates dependencies, `requirements.txt` guarantees reproducibility, and a clean folder structure keeps ML projects production-ready.
