# mlsetup

One command ML project scaffolding CLI. Works on Windows, Mac, and Linux.

## Install

```bash
pip install mlsetup
```

## Usage

```bash
mlsetup init project_name
```

That single command will:

- Create the project folder
- Create all directories — `data`, `src`, `notebooks`, `configs`, `logs`, `tests`
- Create all required files — `.gitignore`, `.env`, `config.yaml`, `train.py`, `eda.ipynb`
- Generate `SETUP_GUIDE.md` — full manual reference inside every project
- Create and configure a virtual environment inside `.venv`
- Upgrade `pip`, `setuptools`, `wheel`
- Install common ML dependencies with pinned versions
- Save `requirements.txt`
- Generate a `README.md`
- Initialize a Git repository with an initial commit

## Version Control

By default mlsetup installs pinned, stable versions of every package. You can override any of them with `--pkg`.

```bash
# Use all defaults
mlsetup init my_project

# Pin specific versions
mlsetup init my_project --pkg numpy==1.24.0 --pkg pandas==2.0.0

# Install latest (no pin)
mlsetup init my_project --pkg numpy==latest

# Add a package not in the defaults
mlsetup init my_project --pkg torch --pkg transformers

# Mix and match
mlsetup init my_project --pkg numpy==1.24.0 --pkg torch --pkg transformers==4.40.0
```

## Default Packages

| Package | Default Version |
|---|---|
| numpy | 1.26.4 |
| pandas | 2.2.2 |
| scikit-learn | 1.4.2 |
| matplotlib | 3.9.0 |
| seaborn | 0.13.2 |
| jupyter | 1.0.0 |
| mlflow | 2.13.0 |
| fastapi | 0.111.0 |
| uvicorn | 0.30.1 |
| python-dotenv | 1.0.1 |

See all defaults anytime:

```bash
mlsetup packages
```

## Project Structure Created

```
project_name/
├── .venv/                 Virtual environment (auto-generated, never touch)
├── data/
│   ├── raw/               Original, untouched data.
│   └── processed/         Cleaned and transformed data.
├── notebooks/
│   └── eda.ipynb          Exploration and visualization only.
├── src/
│   ├── features/          Feature engineering logic.
│   ├── models/            Model definition.
│   ├── training/
│   │   └── train.py       Main training entry point.
│   └── inference/         Prediction and serving logic.
├── configs/
│   └── config.yaml        All settings and hyperparameters.
├── logs/                  Training logs.
├── tests/                 Unit and integration tests.
├── .env                   Secret keys. Never commit.
├── .gitignore
├── requirements.txt
├── SETUP_GUIDE.md         Full manual setup reference.
└── README.md
```

## After Setup

```bash
cd project_name

# Mac / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Run training
python src/training/train.py
```

## All Commands

```bash
mlsetup init <project_name>               Create project with default packages
mlsetup init <project_name> --pkg <spec>  Override specific package versions
mlsetup packages                          List all default packages and versions
mlsetup --version                         Show version
mlsetup --help                            Show help
```

## Requirements

- Python 3.8 or higher
- Git (optional, for auto git init)

## License

MIT
