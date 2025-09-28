# ChromHandler Example: HPLC Data Analysis Training Course

This repository contains a comprehensive training course for analyzing HPLC (High-Performance Liquid Chromatography) data using the ChromHandler library. The course is structured as a series of Jupyter notebooks that guide participants through the complete workflow of chromatographic data analysis.

## 📊 Data Structure

The `data/` directory contains HPLC experimental data organized as follows:

- **`hplc/calibration/`** - Standard calibration curves for quantitative analysis
  - `adenosine/` - 6 concentration standards (25-800 μM) for adenosine calibration
  - `adenine/` - 6 concentration standards (25-800 μM) for adenine calibration
- **`hplc/kinetics/`** - Time-course kinetic experiments
  - `CF6/`, `CF7/`, `CF8/`, `CF9/`, `CF10/` - Multiple experimental conditions with time points from 0-240 minutes
- **`molecules/`** - Pre-defined molecular entities (adenosine, adenine)
- **`proteins/`** - Protein definitions (SAHH enzyme)
- **`enzymeml.json`** - Complete experimental metadata in EnzymeML format

## Installation

This project uses [**uv**](https://docs.astral.sh/uv/) for reproducible dependency management.

1. Install uv  
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  # or with pipx:
  pipx install uv
  ```

2. Install dependencies  
  ```bash
  uv sync --frozen
  ```

3. activate the virtual environment
  ```bash
  source .venv/bin/activate
  ```

## 🧪 Notebook 1: Calibration Analysis (`1-calibration.ipynb`)

This notebook introduces participants to the fundamental concept of HPLC calibration - establishing quantitative relationships between peak areas and analyte concentrations.

### What You'll Learn:
- **Data Loading**: How to load multiple chromatograms from calibration experiments
- **Peak Detection**: Automatic identification of chromatographic peaks
- **Molecule Definition**: Creating molecular entities with retention time parameters
- **Peak Assignment**: Matching detected peaks to known compounds
- **Standard Curve Creation**: Building linear calibration curves for quantitative analysis
- **Data Visualization**: Interactive plotting of chromatograms and calibration curves

### Key Concepts Demonstrated:
1. **Adenosine Calibration**: Step-by-step calibration using 6 concentration standards (25-800 μM)
2. **Adenine Calibration**: Hands-on exercise repeating the calibration process
3. **Protein Definition**: Introduction to protein entities for enzyme kinetics

### Learning Outcomes:
By completing this notebook, participants will understand:
- How HPLC calibration enables quantitative analysis
- The relationship between peak area and analyte concentration
- How to validate calibration curves for accuracy
- Best practices for molecular and protein data management

This foundation prepares participants for the more advanced kinetic analysis covered in subsequent notebooks.

## ⏱️ Notebook 2: Kinetic Analysis (`2-kinetic.ipynb`)

This notebook builds upon the calibration foundation to analyze time-course kinetic experiments, demonstrating how to track enzymatic reactions over time and convert raw chromatographic data into quantitative kinetic insights.

### What You'll Learn:
- **Data Integration**: Loading pre-calibrated molecules and proteins from previous analysis
- **Multi-Sample Processing**: Handling multiple experimental conditions simultaneously
- **Initial Conditions Management**: Working with experimental setup data (concentrations, enzyme amounts)
- **Time-Course Analysis**: Processing chromatograms across different time points (0-240 minutes)
- **Concentration Calculation**: Converting peak areas to actual concentrations using calibration curves
- **EnzymeML Export**: Creating standardized kinetic data files for further analysis

### Key Concepts Demonstrated:
1. **Batch Processing**: Efficiently processing 5 different experimental conditions (CF6-CF10)
2. **Concentration Tracking**: Monitoring adenine and adenosine concentrations over time
3. **Enzyme Kinetics**: Analyzing SAHH (S-adenosylhomocysteine hydrolase) activity
4. **Data Standardization**: Exporting results in EnzymeML format for reproducibility

### Learning Outcomes:
By completing this notebook, participants will understand:
- How to integrate calibration data with kinetic experiments
- The workflow from raw chromatograms to quantitative kinetic data
- How to handle multiple experimental conditions in batch processing
- The importance of standardized data formats (EnzymeML) in enzyme kinetics
- How to visualize time-course data for kinetic analysis

This notebook bridges the gap between basic calibration and advanced kinetic modeling, providing the quantitative foundation needed for the final modeling notebook.

## 🔍 Notebook 3: Model Fitting (`3-model.ipynb`)

This notebook introduces participants to the concept of model fitting - using statistical models to interpret chromatographic data.

### What You'll Learn:
- **Model Definition**: Creating mathematical models of enzymatic reactions
- **Parameter Estimation**: Fitting models to experimental data using MCMC methods
- **Model Evaluation**: Assessing the goodness of fit and parameter uncertainty
- **Data Visualization**: Plotting model predictions alongside experimental data