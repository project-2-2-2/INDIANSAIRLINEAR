from sklearn.neural_network import MLPClassifier

class FlightCrashModel:
    def __init__(self):
        self.model = MLPClassifier(
            hidden_layer_sizes=(8,),
            alpha=0.05,
            max_iter=300,
            early_stopping=False,
            validation_fraction=0.0,
            random_state=42
            # class_weight is NOT supported
        )
    def fit(self, X, y):
        self.model.fit(X, y)
    def predict(self, X):
        return self.model.predict(X)
    def predict_proba(self, X):
        return self.model.predict_proba(X)