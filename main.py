import pandas as pd
import chardet

"""
2.	Processar o arquivo de 1000 em 1000 linhas;
3.	Remover os espaços das colunas. Ex. ' Porto Alegre ' -> 'Porto Alegre';
4.	Criar uma coluna CITY_ASCII no arquivo, a qual deve ser construída com base na coluna CITY. Esta coluna não pode conter acentos, minúsculas e caracteres especiais. Apenas letras, números e hífen são permitidos. Ex. 'São Paulo - abç' -> 'SAO PAULO - ABC'
5.	Remover os caracteres não numéricos da coluna PHONE; 
6.	Salvar o arquivo .csv com a nova coluna em UTF-8;

"""
def detect_encoding(path_file: str, sample_size: int = 100000) -> str:
    #Identificar o encoding do arquivo;

    with open(path_file, 'rb') as f:
        result = chardet.detect(f.read(sample_size))
    return result['encoding']


caminho = '01-bronze-raw/natal2025.csv'

def remove_spaces(df):
    "remove spaces"
    for col in df.columns:
        if df[col].dtype == object: #check if it's text
            df[col] = df[col].str.strip()
    return df

df = pd.read_csv(caminho)

print("antes")
print(df.head())

df = remove_spaces(df)

print('\nDepois:')
print(df.head())
