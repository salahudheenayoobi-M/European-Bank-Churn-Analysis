# 🏦 Customer Segmentation & Churn Pattern Analytics in European Banking

A comprehensive data analytics project that explores customer churn behavior across European banking markets (France, Germany, Spain). The project combines exploratory data analysis in Jupyter Notebook with an interactive Streamlit dashboard for real-time churn insights.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Dashboard Features](#dashboard-features)
- [Key Findings](#key-findings)
- [Contributing](#contributing)
- [License](#license)

---

## 🔍 Overview

Customer churn — the loss of clients to competitors or service discontinuation — is one of the most critical challenges facing the European banking sector. Retaining existing customers is significantly more cost-effective than acquiring new ones, making churn prediction and analysis a top priority for financial institutions.

This project performs **Customer Segmentation & Churn Pattern Analytics** on a dataset of **10,000 European bank customers** to uncover the demographic, financial, and behavioral factors that drive customer attrition.

### Objectives

1. **Identify churn drivers** — Determine which customer attributes (geography, age, gender, credit score, balance, tenure) are most strongly associated with churn.
2. **Segment customers** — Create meaningful customer segments based on age, credit score, balance, and tenure to enable targeted retention strategies.
3. **Visualize patterns** — Build interactive visualizations and a real-time dashboard to communicate findings to stakeholders.
4. **Enable data-driven decisions** — Provide actionable insights that banking institutions can use to reduce customer attrition.

---

## 📊 Dataset

**File:** `European_Bank.csv`  
**Records:** 10,000 customers  
**Year:** 2025  
**Source:** European banking customer records  

### Original Features (14 columns)

| Feature           | Type    | Description                                      |
|-------------------|---------|--------------------------------------------------|
| `Year`            | int64   | Year of the record (2025)                        |
| `CustomerId`      | int64   | Unique customer identifier                       |
| `Surname`         | string  | Customer surname                                 |
| `CreditScore`     | int64   | Credit score (350–850)                           |
| `Geography`       | string  | Country — France, Germany, or Spain              |
| `Gender`          | string  | Male or Female                                   |
| `Age`             | int64   | Customer age (18–92)                             |
| `Tenure`          | int64   | Years with the bank (0–10)                       |
| `Balance`         | float64 | Account balance (€0 – €250,898)                  |
| `NumOfProducts`   | int64   | Number of banking products held (1–4)            |
| `HasCrCard`       | int64   | Has credit card (0 = No, 1 = Yes)                |
| `IsActiveMember`  | int64   | Active member status (0 = No, 1 = Yes)           |
| `EstimatedSalary` | float64 | Estimated annual salary (€11.58 – €199,992.48)   |
| `Exited`          | int64   | **Target variable** — Churned (1) or Retained (0)|

### Engineered Features (4 columns added during analysis)

| Feature          | Type   | Description                                                 |
|------------------|--------|-------------------------------------------------------------|
| `AgeGroup`       | string | Age buckets: `<30`, `30-45`, `45-60`, `60+`                 |
| `CreditBand`     | string | Credit score bands: `Low` (≤580), `Medium` (581-670), `High` (>670) |
| `BalanceSegment`  | string | Balance segments: `Zero` (€0) or `High` (>€0)              |
| `TenureGroup`    | string | Tenure groups: `New` (0-2 yrs), `MidTerm` (3-5), `LongTerm` (6-10) |

---

## 🔬 Methodology

### 1. Data Exploration & Validation
- Inspected shape, data types, and column structure
- Checked for missing values (none found)
- Identified zero/negative values in numerical columns
- Validated binary columns (`HasCrCard`, `IsActiveMember`, `Exited`)

### 2. Data Cleaning
- Replaced zero/negative values in `CreditScore`, `Age`, and `EstimatedSalary` with median imputation
- Dropped non-analytical columns (`Surname`, `CustomerId`)
- Retained zero-balance records as a valid segment

### 3. Feature Engineering & Segmentation
- **Age Groups:** `<30`, `30-45`, `45-60`, `60+`
- **Credit Bands:** `Low`, `Medium`, `High`
- **Balance Segments:** `Zero`, `High`
- **Tenure Groups:** `New`, `MidTerm`, `LongTerm`

### 4. Churn Analysis
- Calculated overall churn rate and churn counts
- Performed segment-level churn analysis by Geography, Gender, Age Group, Credit Band, Balance Segment, and Tenure Group

### 5. Visualization
- Created interactive Plotly charts (pie/donut, bar charts) in the Jupyter Notebook
- Built a multi-tab Streamlit dashboard with sidebar filters and KPI metrics

---

## 🛠️ Tech Stack

| Category        | Technology                              |
|-----------------|----------------------------------------|
| Language        | Python 3.x                             |
| Data Analysis   | Pandas, NumPy                          |
| Visualization   | Plotly Express, Matplotlib, Seaborn    |
| Dashboard       | Streamlit                              |
| Notebook        | Jupyter Notebook                       |
| Version Control | Git & GitHub                           |

---

## 📂 Project Structure

```
European Banking/
│
├── European Banking.ipynb    # Jupyter Notebook — full EDA & analysis pipeline
├── European_Bank.csv         # Dataset (10,000 customer records, 16 columns)
├── app.py                    # Streamlit dashboard application
├── requirements.txt          # Python dependencies
├── RESEARCH_PAPER.md         # Detailed research paper & findings
├── README.md                 # This file
├── .gitignore                # Git ignore rules
└── LICENSE                   # MIT License
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/european-banking-churn-analysis.git
   cd european-banking-churn-analysis
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit dashboard**
   ```bash
   streamlit run app.py
   ```

5. **Or open the Jupyter Notebook**
   ```bash
   jupyter notebook "European Banking.ipynb"
   ```

---

## 🚀 Usage

### Streamlit Dashboard
Run `streamlit run app.py` and open the URL shown in your terminal (typically `http://localhost:8501`).

Use the **sidebar filters** to slice the data by:
- Geography (France, Germany, Spain)
- Gender (Male, Female)
- Age Group (<30, 30-45, 45-60, 60+)

### Jupyter Notebook
Open `European Banking.ipynb` to walk through the full analysis pipeline — from data loading and cleaning through segmentation, churn computation, and interactive Plotly visualizations.

---

## 📈 Dashboard Features

The Streamlit dashboard is organized into **four tabs**:

| Tab | Contents |
|-----|----------|
| **Overview** | Donut chart showing overall churn vs. retention split |
| **Geography & Demographics** | Bar charts for churn rate by Geography, Gender, Age Group, and Tenure Group |
| **Financial Profile** | Churn by Credit Score Band and Balance Segment + High-Value Customer Explorer with dedicated KPIs |
| **Drill-Down Data** | Full interactive data table with CSV download capability |

**Top-level KPIs** are always visible:
- Total Customers
- Churned Customers
- Retained Customers
- Churn Rate (%)

---

## 🔑 Key Findings

| Insight | Detail |
|---------|--------|
| **Overall churn rate** | **20.37%** — 2,037 out of 10,000 customers churned |
| **Germany leads churn** | 32.44% churn rate vs. ~16% for France and Spain |
| **Female customers churn more** | 25.07% vs. 16.46% for males |
| **Age 45-60 is highest risk** | 51.12% churn rate — over 3× the rate of customers under 30 |
| **High-balance customers churn more** | 24.08% vs. 13.82% for zero-balance customers |
| **Credit score has modest impact** | Low credit: 22.15%, Medium: 20.39%, High: 19.36% |
| **Tenure slightly reduces churn** | New (21.15%) > MidTerm (20.76%) > LongTerm (19.67%) |

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Salah**

---

> *Built with ❤️ using Python, Pandas, Plotly, and Streamlit*
