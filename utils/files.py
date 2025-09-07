import chardet
import pandas as pd

def detect_encoding(path_file: str, sample_size: int = 100000) -> str:
    """
    Detecta o encoding do arquivo lendo uma amostra
    """

    with open(path_file, 'rb') as f:
        result = chardet.detect(f.read(sample_size))
    return result['encoding']
