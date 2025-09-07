import pandas as pd
import chardet
import unidecode
import re
from pathlib import Path

"""
2.	Processar o arquivo de 1000 em 1000 linhas;
3.	Remover os espaços das colunas. Ex. ' Porto Alegre ' -> 'Porto Alegre'; ok
4.	Criar uma coluna CITY_ASCII no arquivo, a qual deve ser construída com base na coluna CITY. Esta coluna não pode conter acentos, minúsculas e caracteres especiais. Apenas letras, números e hífen são permitidos. Ex. 'São Paulo - abç' -> 'SAO PAULO - ABC'
5.	Remover os caracteres não numéricos da coluna PHONE; 
6.	Salvar o arquivo .csv com a nova coluna em UTF-8;

"""
def detect_encoding(path_file: str, sample_size: int = 100000) -> str:
    #Identificar o encoding do arquivo;

    with open(path_file, 'rb') as f:
        result = chardet.detect(f.read(sample_size))
    return result['encoding']


path = '01-bronze-raw/natal2025.csv'

def remove_spaces(df):
    "remove spaces"
    for col in df.columns:
        if df[col].dtype == object: 
            df[col] = df[col].str.strip()
    return df

def create_column (df, from_column = 'CITY'):
    #4.	Criar uma coluna CITY_ASCII no arquivo, a qual deve ser construída com base na coluna CITY. Esta coluna não pode conter acentos, minúsculas e caracteres especiais. Apenas letras, números e hífen são permitidos. Ex. 'São Paulo - abç' -> 'SAO PAULO - ABC'

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
    # Remover os caracteres não numéricos da coluna PHONE; 
    if phone_column in df.columns:
        new_column = []
        for value in df[phone_column]:
            text = str(value)
            text = re.sub(r'\D', '', text)
            new_column.append(text)
        df[phone_column] = new_column
    
    return df

def process_file(path_enter, path_out, chuncksize=1000):

    detected_encode = detect_encoding(path_enter)
    print(f'Processando : {path_enter} (encoding: {detected_encode})')

    processed_chunks = []

    for chunk in pd.read_csv(path_enter, chunksize=chuncksize, encoding=detected_encode):
        chunk = remove_spaces(chunk)
        chunk = create_column(chunk)
        chunk = clean_numbers(chunk)
        processed_chunks.append(chunk)

    df_final = pd.concat(processed_chunks, ignore_index=True)    

    df_final.to_csv(path_out, index=False, encoding='utf-8')
    print(f'Arquivo salvo em: {path_out}')



if __name__ == "__main__":
    enter_path = "01-bronze-raw/natal2025.csv"
    out_path = "02-silver-validated/natal2025_trusted.csv"
    process_file(enter_path, out_path)