# Teste Técnico - OTO  

Projeto desenvolvido como resolução do teste técnico proposto pela Oto. Este projeto tem como objetivo processar arquivos CSV aplicando algumas transformaçõe.

O processamento é feito em **chunks de 1000 linhas**, para que arquivos grandes possam ser tratados sem travar a memória.

## Funcionalidades

1. **Remove espaços** no início e fim de todas as colunas de texto.  
2. **Criar coluna `CITY_ASCII`** a partir da coluna `CITY`:
   - Remove acentos
   - Converte para maiúsculas
   - Mantém apenas letras, números, espaço e hífen
3. **Limpa números de telefone** na coluna `PHONE` (remove tudo que não for número).  
4. **Processa em chunks** de 1000 linhas para arquivos grandes.  
5. **Detecta encoding** 

## Estrutura do Projeto
```text
projeto-oto/
│
├── main.py                       # Inicia o processamento 
├── utils/
│   ├── __init__.py               # Torna a pasta um módulo Python.
│   ├── transform.py              # Funções de transformação: remove_spaces, create_column, clean_numbers.
│   └── files.py                  # Funções de detecção de encoding.
├── 01-raw-bronze                 # Pasta com arquivos CSV de entrada.
└── 02-validated-silver/          # Pasta com arquivos CSV tratados.

```


## Como usar

1. Clone o repositório.
2. Coloque seu arquivo CSV dentro da pasta **`01-raw-bronze/**`.  
3. No terminal, execute:

```bash
python main.py
```
4. O arquivo processado será salvo na pasta **'02-raw-bronze/'** com o sufixo **_trusted.csv**.

## Dependências
Todas as bibliotecas podem ser instaladas usando o pip:

```bash

pip install -r requirements.txt

```
