from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

class RiskScorer:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.encoder = LabelEncoder()

    def train(self, X, y):
        y_encoded = self.encoder.fit_transform(y)
        self.model.fit(X, y_encoded)

    def predict(self, X):
        preds = self.model.predict(X)
        return self.encoder.inverse_transform(preds)

    def predict_proba(self, X):
        return self.model.predict_proba(X)