from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

def evaluate_models(models, X_test, y_test):
    """
    Evaluate trained models using R2, MAE, and RMSE.
    """
    results = {}
    for name, model in models.items():
        preds = model.predict(X_test)
        r2 = r2_score(y_test, preds)
        mae = mean_absolute_error(y_test, preds)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        
        results[name] = {
            "R2": r2,
            "MAE": mae,
            "RMSE": rmse,
            "Predictions": preds
        }
        print(f"\n--- {name} Performance ---")
        print(f"R² Score: {r2:.4f}")
        print(f"MAE:      {mae:.4f}")
        print(f"RMSE:     {rmse:.4f}")

    return results