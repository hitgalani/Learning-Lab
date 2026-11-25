### Create a virtual environment (Windows PowerShell)

```powershell
py -3.11 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Deactivate:

```powershell
deactivate
```

**Recommendation:** Use a separate virtual environment for each major project. This prevents package conflicts between projects.

---

# 4. Data Science & Data Analysis

These libraries help you collect, clean, analyze, calculate, and visualize data.

| Library | Purpose |
|---|---|
| NumPy | Numerical calculations and multidimensional arrays |
| pandas | Data cleaning, manipulation, and analysis |
| Matplotlib | Create charts, graphs, and visualizations |
| Seaborn | Statistical data visualization |
| SciPy | Scientific and mathematical calculations |
| Plotly | Interactive charts and graphs |
| JupyterLab | Interactive data science workspace |
| IPython | Interactive Python environment |
| ipykernel | Run Python kernels in Jupyter and VS Code |

### Installation command

```powershell
python -m pip install numpy pandas matplotlib seaborn scipy plotly jupyterlab ipykernel
```

### Important uses

- NumPy: Arrays, matrices, numerical operations.
- pandas: CSV files, DataFrames, missing values, data cleaning.
- Matplotlib: Line charts, bar charts, histograms.
- Seaborn: Heatmaps, correlation graphs, statistical charts.
- SciPy: Optimization, statistics, scientific functions.
- Plotly: Interactive data dashboards.
- JupyterLab: Notebook-based experimentation.

---
