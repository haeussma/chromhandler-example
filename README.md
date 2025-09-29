# ChromHandler Example: HPLC Data Analysis Training Course

This repository contains a hands-on training course for analyzing HPLC data using the ChromHandler library. Learn to process chromatographic data from calibration to kinetic modeling.

## Outline

1. **Calibration** - Build quantitative standard curves
2. **Kinetics** - Analyze time-course enzyme experiments
3. **Modeling** - Fit statistical models to kinetic data

## How to Use This Repository

### Option One: Install and Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/haeussma/chromhandler-example.git
   cd chromhandler-example
   ```

2. Install uv (Python package manager):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # or with pipx:
   pipx install uv
   ```

3. Install dependencies:
   ```bash
   uv sync --frozen
   ```

4. Activate environment and start Jupyter:
   ```bash
   source .venv/bin/activate
   jupyter lab
   ```

### Option Two: Try Out in Colab

For quick experimentation without local setup:
- [1-calibration.ipynb](https://colab.research.google.com/github/haeussma/chromhandler-example/blob/main/1-calibration.ipynb)
- [2-kinetic.ipynb](https://colab.research.google.com/github/haeussma/chromhandler-example/blob/main/2-kinetic.ipynb)
- [3-model.ipynb](https://colab.research.google.com/github/haeussma/chromhandler-example/blob/main/3-model.ipynb)

## Data Structure

```
data/
├── hplc/
│   ├── calibration/
│   │   ├── adenosine/        # 6 concentration standards (25-800 μM)
│   │   └── adenine/          # 6 concentration standards (25-800 μM)
│   └── kinetics/
│       ├── CF6/, CF7/, CF8/, CF9/, CF10/  # Time-course experiments (0-240 min)
│       └── init_conditions.csv           # Initial concentrations
├── molecules/                # Pre-defined molecular entities
├── proteins/                 # Enzyme definitions (SAHH)
└── enzymeml.json            # Complete experimental metadata
```

## Notebooks

### 🧪 [1-calibration.ipynb](https://colab.research.google.com/github/haeussma/chromhandler-example/blob/main/1-calibration.ipynb)
Learn to build quantitative calibration curves from HPLC data. Create standard curves for adenosine and adenine, define molecular entities, and prepare for kinetic analysis.

### ⏱️ [2-kinetic.ipynb](https://colab.research.google.com/github/haeussma/chromhandler-example/blob/main/2-kinetic.ipynb)
Process time-course enzyme kinetic experiments. Convert raw chromatograms to concentration data using calibration curves and export standardized EnzymeML files.

### 📊 [3-model.ipynb](https://colab.research.google.com/github/haeussma/chromhandler-example/blob/main/3-model.ipynb)
Fit statistical models to kinetic data using Bayesian inference. Estimate kinetic parameters with uncertainty quantification and validate model predictions.