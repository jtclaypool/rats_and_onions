import pandas as pd


def loader(path):
    """
    Load the file associated with the rats and onions experiment.
    """
    xl = pd.ExcelFile(path)
    spectra = pd.read_excel(xl, sheet_name='X', index_col=0)
    treatment = pd.read_excel(xl, sheet_name='y', usecols=range(10, 15))
    return spectra, treatment['y']