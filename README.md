HR Attrition Analysis Notebook
================================

Overview
--------
- Interactive, bilingual (English/Hebrew) HR analytics notebook that explores employee attrition drivers and HR KPIs.  
- Primary deliverable: `phyton_project_final.ipynb`, which merges multiple HR tables, cleans features, performs exploratory analysis, and summarizes insights plus recommendations.

Repository Contents
-------------------
- `phyton_project_final.ipynb` – main polished analysis used for presentations.  
- `phyton_project .ipynb` – earlier working version kept for reference.  
- `connect_mysql.ipynb`, `HRDB.sql`, `hrdb2.xlsx` – data acquisition assets (SQL schema, Excel export).  
- `how_to_analyze_dataset.pdf`, `HR_Pyhotn_Final_Project.pdf` – supporting documentation and slides.

Requirements
------------
- Python 3.10+  
- Packages: `jupyterlab` or `notebook`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `openpyxl` (for Excel I/O).  
- Optional: Power BI/Slide tools if you want to reuse the presentation artifacts.

Quick Start
-----------
1. Create & activate a virtual environment (example using `venv`):
   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -U pip
   pip install jupyterlab pandas numpy matplotlib seaborn openpyxl
   ```
2. Ensure `hrdb2.xlsx` sits under `CSV & EXCEL TABLES/` relative to the project root (or update `file_path` in the notebook).  
3. Launch Jupyter and open the notebook:
   ```
   jupyter lab phyton_project_final.ipynb
   ```
4. Run the cells top-to-bottom; markdown cells outline the bilingual narrative and table-of-contents links.

Notebook Roadmap
----------------
- **Introduction & Objectives** – business framing, scope, and key assumptions.  
- **Imports & Settings** – library setup and Excel path definitions.  
- **Data Loading & Overview** – merges the two HR sheets on `EmployeeNumber`, inspects schema, and creates `Attrition_Flag`.  
- **Cleaning & Preparation** – removes constant columns, checks duplicates/missing data, and prepares analytical features.  
- **Exploratory Data Analysis** – visual and tabular summaries for satisfaction metrics, tenure, compensation, overtime, and more.  
- **Insights, Conclusions, Recommendations** – highlights drivers of attrition and suggested HR actions.

Reproducibility Tips
--------------------
- Keep raw sources read-only; derive new datasets in separate files or sheets.  
- When adapting to new HR snapshots, verify column names align before running the merge step.  
- Refresh plots after any filtering tweaks to avoid stale visuals in exported reports.

Contributing / Next Steps
-------------------------
- Expand with predictive modeling (e.g., classification baselines) or cohort dashboards.  
- Localize additional markdown if you need deeper Hebrew context.  
- When making changes, duplicate the notebook or use git branches to preserve the delivered version.

