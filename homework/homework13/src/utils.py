import joblib


def predict(features, round_prediction=False):
    """
    Predict using the loaded model.
    Optional parameter: round_prediction
    """
    loaded_model = joblib.load('../model/model.pkl')

    pred = loaded_model.predict([features])[0]
    if round_prediction:
        pred = round(pred, 2)
    return pred

def calculate_metrics(df):
    return df.describe()