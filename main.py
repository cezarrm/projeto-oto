from utils.transform import remove_spaces, create_column, clean_numbers
from utils.files import detect_encoding
import pandas as pd

def process_file(path_enter, path_out, chunksize=1000):
    
    """
    Processa um arquivo CSV de 1000 em 1000,
    aplica as transformações e salva em UTF-8.

    """

    detected_encode = detect_encoding(path_enter)
    print(f'Processing: {path_enter} (encoding: {detected_encode})')

    processed_chunks = []

    for chunk in pd.read_csv(path_enter, chunksize=chunksize, encoding=detected_encode):
        chunk = remove_spaces(chunk)
        chunk = create_column(chunk)
        chunk = clean_numbers(chunk)
        processed_chunks.append(chunk)

    df_final = pd.concat(processed_chunks, ignore_index=True)    

    df_final.to_csv(path_out, index=False, encoding='utf-8')
    print(f'File saved: {path_out}')


if __name__ == "__main__":
    enter_path = "01-bronze-raw/natal2025.csv"
    out_path = "02-silver-validated/natal2025_trusted.csv"
    process_file(enter_path, out_path)


