from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


class ParetoScaler(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        pareto = np.sqrt(np.std(X, axis=1))
        X_trans = np.divide(X, pareto.to_frame()) 
        return X_trans


class BandSelector(BaseEstimator, TransformerMixin):
    """
    Band selector selects a spectra between start and stop
    Example:
    selector = BandSelector(start = 1, stop = 3)
    selector.fit_transform(spectra_df)
    """
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return X.loc[:, self.start:self.stop]
