# ChromHandler Example: HPLC Data Analysis Training Course

This repository contains a hands-on training course for analyzing HPLC data using the ChromHandler library. Learn to process chromatographic data from calibration to kinetic modeling.

## Outline

The workflow for processing HPLC data is as follows:

1. **Calibration** - Build quantitative standard curves
2. **Kinetics** - Read and process time-course enzyme experiments
3. **Modeling** - Fit statistical models to kinetic data

## How to Use This Repository

### Option One: Install and Run Locally in Code Editor of Choice

1. Clone the repository:
   ```bash
   git clone https://github.com/haeussma/chromhandler-example.git
   cd chromhandler-example
   ```

2. Install uv (Python package manager):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # or if you have pipx:
   pipx install uv
   ```

3. Install dependencies:
   ```bash
   uv sync --frozen
   ```

### Option Two: Try it in Colab

If you don’t have a local code editor (and don’t plan to use one), you can try the notebooks in Google Colab to get a feel for the workflow. No installation is required.


| 1-calibration.ipynb | 2-kinetic.ipynb | 3-model.ipynb |
|:---:|:---:|:---:|
| [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/haeussma/chromhandler-example/blob/main/1-calibration.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/haeussma/chromhandler-example/blob/main/2-kinetic.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/haeussma/chromhandler-example/blob/main/3-model.ipynb) |

## Data Structure

The HPLC data are pre-integrated. Calibration runs and kinetic time-courses are kept in separate directories, while the initial conditions for each kinetic series are stored in a single CSV next to the time-course data. Use the table below as your lookup for where each input lives.

| Input Data Type       | Location                                                                 |
|-----------------------|--------------------------------------------------------------------------|
| Calibration           | [`data/hplc/calibration/`](./data/hplc/calibration/)                     |
| Time-course kinetics  | [`data/hplc/kinetics/`](./data/hplc/kinetics/)                           |
| Initial conditions    | [`data/hplc/init_conditions.csv`](./data/hplc/init_conditions.csv)-------|

You can take a look inside to get a feel for the data.

## Notebooks

To get started, open the first notebook to process the calibration data.

### 🧪 [1-calibration.ipynb](./1-calibration.ipynb)
Build quantitative calibration curves from HPLC data. Create standard curves for adenosine and adenine, define molecular entities, and prepare for kinetic analysis.

### ⏱️ [2-kinetic.ipynb](./2-kinetic.ipynb)
Process time-course enzyme kinetic experiments. Convert raw chromatograms to concentration data using calibration curves and export standardized EnzymeML files.

### 📊 [3-model.ipynb](./3-model.ipynb)
Fit statistical models to kinetic data using Bayesian inference. Estimate kinetic parameters with uncertainty quantification and validate model predictions.