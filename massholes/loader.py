import pandas as pd


def loader(path):
    """
    Load the file associated with the rats and onions experiment.
    """
    df = pd.read_excel(path, index_col=0)
    treatment = pd.read_excel(path, sheet_name='y', usecols=range(10, 15))

    new_df = (
        df
        .transpose()
        .reset_index()
        .assign(treatment=treatment['y'])
    )

    return new_df
