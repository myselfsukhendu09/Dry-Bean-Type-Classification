# Dry Bean Classification - Project Report

## Executive Summary

This project develops a machine learning classification system to predict dry bean types based on morphological features. A Streamlit web application provides an intuitive interface for real-time predictions.

## Problem Statement

Accurate classification of dry beans is important for:
- Quality control in agricultural processing
- Automated sorting systems
- Inventory management
- Market classification

## Solution

A supervised machine learning model trained on 13,611 bean samples with 16 morphological features to classify 7 bean types.

## Key Achievements

✅ Developed a robust classification model
✅ Created an interactive web application
✅ Professional project documentation
✅ Clean code structure and organization

## Model Architecture

- **Input**: 16 morphological features (Area, Perimeter, Eccentricity, etc.)
- **Processing**: Feature scaling using StandardScaler
- **Algorithm**: Supervised classification (see notebook for specific algorithm)
- **Output**: Predicted bean type with probabilities

## Files Description

| Component | File | Purpose |
|-----------|------|---------|
| Application | `app.py` | Streamlit web interface for predictions |
| Model | `model.pkl` | Trained classification model |
| Preprocessor | `scaler.pkl` | Feature normalization |
| Encoder | `lebel.pkl` | Class label encoding |
| Dataset | `Worksheet in Beans Multiclass Classification.csv` | Training data |
| Analysis | Jupyter notebook | Complete EDA and model training |

## Installation & Deployment

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## Feature Documentation

### Input Features (16 total)

1. **Area** - Number of pixels within bean boundaries
2. **Perimeter** - Outer boundary length in pixels
3. **Major Axis Length** - Length of longest axis
4. **Minor Axis Length** - Length of shortest axis
5. **Aspect Ratio** - Ratio of major to minor axis
6. **Eccentricity** - Elongation measure (0=circle, 1=line)
7. **Convex Area** - Area of convex hull
8. **Equivalent Diameter** - Diameter of circle with same area
9. **Extent** - Bean area divided by bounding box area
10. **Solidity** - Bean area divided by convex area
11. **Roundness** - 4π × Area / Perimeter²
12. **Compactness** - Length of major axis / Perimeter
13. **ShapeFactor1** - Convex area / Area
14. **ShapeFactor2** - Aspect ratio × Solidity
15. **ShapeFactor3** - Perimeter² / Area
16. **ShapeFactor4** - Major axis × Minor axis / Area

### Output Classes

1. SEKER
2. BARBUNYA
3. BOMBAY
4. CALI
5. HOROZ
6. SIRA
7. DERMASON

## Development Stack

- **Language**: Python 3.8+
- **ML Framework**: Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Web Framework**: Streamlit
- **Visualization**: Matplotlib, Seaborn
- **Model Serialization**: Joblib

## Performance Evaluation

Detailed metrics available in the Jupyter notebook including:
- Classification accuracy
- Precision, recall, F1-score per class
- Confusion matrix analysis
- Cross-validation results

## Future Enhancements

- [ ] Model explainability (SHAP/LIME)
- [ ] Batch prediction capability
- [ ] Model versioning and A/B testing
- [ ] Advanced data visualization
- [ ] REST API development
- [ ] Docker containerization
- [ ] CI/CD pipeline integration

## Usage Instructions

### Web Application

1. Launch the Streamlit app
2. Enter bean measurements in input fields
3. Click "Predict" button
4. View classification result and confidence

### Batch Processing

Use the Jupyter notebook to:
- Load the pre-trained model
- Process multiple samples
- Generate predictions with probabilities
- Visualize results

## Code Quality

- Clean, modular Python code
- Comments and docstrings included
- Professional project structure
- Version controlled with Git

## Author

**Sukhendu Biswas** (Batch 12)

GitHub: https://github.com/myselfsukhendu09

## License

Educational Project - All Rights Reserved

---

For questions or contributions, please visit the GitHub repository.
