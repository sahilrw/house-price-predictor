# 🏠 House Price Predictor - Ames Housing
This project is a machine learning pipeline built to predict house prices using the [Ames Housing dataset](https://www.kaggle.com/datasets/prevek18/ames-housing-dataset). It's designed as a beginner-friendly project to explore core machine learning workflows like data preprocessing, feature engineering, and model building.

---

## 📂 Project Structure

```
.
├── data/                  # Raw and processed datasets
├── notebooks/             # EDA, preprocessing, and model development notebooks
├── src/                   # Custom Python modules (e.g., outlier removal)
├── outputs/               # Model outputs, plots, predictions
├── README.md              # Project overview
├── requirements.txt       # Python dependencies
└── .gitignore             # Files to be excluded from version control
```

---

## 📊 Dataset
- **Name:** Ames Housing Dataset  
- **Source:** [Kaggle - prevek18](https://www.kaggle.com/datasets/prevek18/ames-housing-dataset)  
- **Shape:** ~2,900 rows × 80 features  
- **Target Variable:** `SalePrice` (continuous)

---

## ✅ Completed Steps

- ✅ Loaded the dataset from `data/raw/AmesHousing.csv`
- ✅ Performed **Exploratory Data Analysis (EDA)** using:
  - Seaborn and Matplotlib for visualizations
  - Feature distribution, missing values, and correlation checks
- ✅ Removed extreme outliers using a custom function

---

## 🔜 Upcoming Steps

- ⏳ Data Cleaning
  - Handle missing values
  - Encode categorical variables
- ⏳ Feature Engineering
  - Create new features (e.g., total square footage)
- ⏳ Model Building
  - Try Linear Regression, Random Forest, XGBoost
- ⏳ Evaluation
  - Use RMSE, MAE for performance tracking
- ⏳ Deployment
  - Save model with `joblib` or `pickle`
  - Create a simple Flask or Streamlit app

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/MakaiRonin01/house-price-predictor.git

# Set up environment
pip install -r requirements.txt
```

---

## 📌 Notes

- The dataset is not included in this repo due to size and licensing. You can download it from [Kaggle](https://www.kaggle.com/datasets/prevek18/ames-housing-dataset) and place it under `data/raw/`.

---