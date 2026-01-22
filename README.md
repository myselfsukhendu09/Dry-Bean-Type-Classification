# Dry Bean Type Classification

A machine learning project for classifying different types of dry beans based on their physical characteristics using supervised learning techniques.

## 📋 Project Overview

This project builds a predictive model to classify dry beans into different types using 16 morphological features extracted from bean images. The model is trained on a comprehensive dataset and deployed with a Streamlit web application for easy predictions.

### Bean Types
- SEKER
- BARBUNYA
- BOMBAY
- CALI
- HOROZ
- SIRA
- DERMASON

## 🎯 Features

The classification model uses the following 16 morphological features:
- **Area** - Bean area in pixels
- **Perimeter** - Bean perimeter
- **Major Axis Length** - Length of the major axis
- **Minor Axis Length** - Length of the minor axis
- **Aspect Ratio** - Ratio of major to minor axis
- **Eccentricity** - Measure of bean elongation
- **Convex Area** - Area of convex hull
- **Equivalent Diameter** - Diameter of equivalent circle
- **Extent** - Ratio of bean area to bounding rectangle
- **Solidity** - Ratio of bean area to convex area
- **Roundness** - Measure of roundness
- **Compactness** - Measure of compactness
- **ShapeFactor1-4** - Additional shape characteristics

## 🏗️ Project Structure

```
Dry-Bean-Type-Classification/
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Git ignore rules
├── app.py                              # Streamlit web application
├── model.pkl                           # Trained machine learning model
├── scaler.pkl                          # Feature scaler
├── lebel.pkl                           # Label encoder
├── Worksheet in Beans Multiclass Classification.csv  # Dataset
└── Sukhendu_Biswas_Batch_12Mini Project_Dry Bean Type Classification.ipynb  # Analysis notebook
```

## 💾 Dataset

The dataset contains physical measurements of dry beans with 13,611 samples across 7 different bean types. Each sample includes 16 morphological features.

**Source**: Beans Dataset (Available on Kaggle and UCI Machine Learning Repository)

## 🤖 Model Details

- **Algorithm**: Supervised Classification (details in notebook)
- **Features**: 16 morphological characteristics
- **Classes**: 7 bean types
- **Training**: Scikit-learn with feature scaling
- **Performance**: Model metrics available in the analysis notebook

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

1. Clone the repository:
```bash
git clone https://github.com/myselfsukhendu09/Dry-Bean-Type-Classification.git
cd Dry-Bean-Type-Classification
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Run the Web Application
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

#### Use the Notebook
Open and run the Jupyter notebook to see the complete analysis, model training, and evaluation:
```bash
jupyter notebook "Sukhendu_Biswas_Batch_12Mini Project_Dry Bean Type Classification.ipynb"
```

## 📊 How to Use the Application

1. Launch the Streamlit app using the command above
2. Enter the 16 morphological feature values for your bean
3. Click the prediction button
4. View the predicted bean type and confidence scores

## 📈 Model Performance

Detailed performance metrics including:
- Accuracy, Precision, Recall, F1-Score
- Confusion Matrix
- Classification Report
- Feature Importance Analysis

See the Jupyter notebook for complete evaluation.

## 📁 Key Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit web application for predictions |
| `model.pkl` | Trained classification model |
| `scaler.pkl` | Feature StandardScaler for data preprocessing |
| `lebel.pkl` | Label encoder for bean type labels |
| `*.csv` | Training and testing dataset |
| `*.ipynb` | Complete analysis and model development notebook |

## 🔧 Technologies Used

- **Python 3.x** - Programming language
- **Scikit-learn** - Machine learning library
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Streamlit** - Web application framework
- **Joblib** - Model serialization
- **Matplotlib/Seaborn** - Data visualization

## 📝 Analysis Highlights

The Jupyter notebook includes:
- Exploratory Data Analysis (EDA)
- Data preprocessing and feature scaling
- Model training with cross-validation
- Hyperparameter tuning
- Performance evaluation
- Visualization of results

## 👤 Author

**Sukhendu Biswas**
- GitHub: [@myselfsukhendu09](https://github.com/myselfsukhendu09)

## 📄 License

This project is provided as-is for educational purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

## 📧 Contact

For questions or suggestions, please reach out through GitHub.

---

**Note**: The pickle files (`model.pkl`, `scaler.pkl`, `lebel.pkl`) contain the trained model and preprocessing objects. These should not be modified manually.
