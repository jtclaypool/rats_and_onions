import pandas as pd

def loader(path):
    df = pd.read_excel(path,index_col=0)
    treatment=pd.read_excel(path,sheet_name='y')
    treatment=pd.Series(treatment['y'])

    new_df=df.transpose().reset_index()
    new_df['treatment']=treatment


    return new_df