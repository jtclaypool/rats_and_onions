from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


class ParetoScaler(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        pareto = np.sqrt(np.std(X, axis=1))
        X_trans = np.divide(X, pareto.to_frame()) 
        return X_trans
