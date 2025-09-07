import unidecode
import re

def remove_spaces(df):

    """
    Remove espaços extras no início e no fim de todas as colunas de texto.
    """
    for col in df.columns:
        if df[col].dtype == object: 
            df[col] = df[col].str.strip()
    return df
    
def create_column (df, from_column = 'CITY'):
    
    """
    Cria a coluna CITY_ASCII sem acentos, em maiúsculas e sem caracteres especiais.
    """
    new_column = []
    for value in df[from_column]:
        text = str(value) 
        text = unidecode.unidecode(text) 
        text = text.upper()
        text = re.sub(r'[^A-Z0-9\- ]', '', text)
        new_column.append(text)
    df['CITY_ASCII'] = new_column
    
    return df

def clean_numbers (df, phone_column='PHONE'):

    """
    Remove os caracteres não numéricos da coluna PHONE;
    """
    if phone_column in df.columns:
        new_column = []
        for value in df[phone_column]:
            text = str(value)
            text = re.sub(r'\D', '', text)
            new_column.append(text)
        df[phone_column] = new_column
    
    return df
