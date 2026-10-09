from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import joblib

def train_models(X_train, y_train):
    """
    Train Random Forest and XGBoost regressors.
    """
    print("Training Random Forest Regressor...")
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    print("Training XGBoost Regressor...")
    xgb = XGBRegressor(n_estimators=100, learning_rate=0.05, random_state=42)
    xgb.fit(X_train, y_train)

    return {"RandomForest": rf, "XGBoost": xgb}

def save_best_model(model, filepath="models/best_aqi_model.pkl"):
    joblib.dump(model, filepath)
    print(f"\nBest model successfully saved to: {filepath}")