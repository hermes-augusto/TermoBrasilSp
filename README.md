# TermoBrasilSp

Este repositório foi criado como parte de um trabalho de análise de dados climáticos para o **MBA**, na disciplina de **Data Visualization**.

## 📌 Estrutura do Projeto

```
📁 TermoBrasilSp/
│── 📁 data/                  # Dados brutos
│── 📁 scripts/               # Módulos Python reutilizáveis
│   ├── utils.py              # Funções para carregar/processar dados
│── analise_dados_api.ipynb   # Notebook com a análise de dados via API
│── analise_dados_file.ipynb  # Notebook com a análise de dados via arquivo
│── .gitignore                # Arquivo de configuração do Git
│── pyproject.toml            # Configuração do Poetry
│── README.md                 # Documentação do projeto
```

## Como Configurar o Projeto com Poetry

Este projeto utiliza **Poetry** para gerenciamento de dependências. Se ainda não tem o Poetry instalado, siga os passos abaixo:

### 1 **Instalar o Poetry**

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 2️ **Criar um ambiente virtual e instalar as dependências**

```bash
poetry install
```

### 3️ **Ativar o ambiente virtual**

```bash
poetry shell
```

## Executando o Jupyter Notebook com Poetry

Para abrir o **Jupyter Notebook** dentro do ambiente gerenciado pelo Poetry:

```bash
poetry run jupyter notebook
```
Isso abrirá o navegador com a interface do Jupyter, onde você pode rodar os notebooks disponíveis em `notebooks/`.

## Executando o Jupyter Notebook no VScode
localizar seu ambiente virtual do Poetry e executar o comando abaixo para instalar o kernel do Jupyter:

```bash
poetry env info --path
```
Criar um kernel do Jupyter Notebook para o ambiente virtual do Poetry:

```bash
poetry run python -m ipykernel install --user --name <nome_do_kernel>
```
Apos *reniciar* o VScode você pode selecionar o kernel do Poetry no VS Code e executar os notebooks normalmente.
##  Rodando a Análise de Dados

Se quiser **baixar novos dados** diretamente da API [Open-Meteo](https://open-meteo.com/), basta executar o notebook analise_dados_api.ipynb. 

Caso **não queira fazer requisições**, já existem dados armazenados na pasta `data/` que podem ser usados diretamente basta executar o notebook analise_dados_file.ipynb. 


