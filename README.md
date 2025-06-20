# Equipe:
## Dante de Oliveira Dantas - 2518583
## Rafael Lima Tavares - 2517595

# Projeto_fundamentos_Python

# Projeto de Pipeline de Dados - Engenharia de Dados

Este projeto implementa um pipeline de Extração, Transformação e Carga (ETL) em Python, com foco em modularidade e boas práticas.

## 🎯 Objetivo

Construir um pipeline de dados robusto e modular, aplicando conceitos de:

- **Orientação a Objetos**: Estruturação de tarefas como classes.
- **Modularidade**: Separação de responsabilidades em diferentes arquivos e pacotes.
- **Decorators**: Uso de decoradores para funcionalidades transversais como logging.
- **Tratamento de Exceções**: O pipeline é resiliente e interrompe a execução em caso de falhas.
- **Logging**: Geração de logs detalhados tanto no console quanto em um arquivo persistente.

## ⚙️ Como Executar

### 1. Pré-requisitos

- Python 3.8 ou superior

### 2. Instalação (Essa parte nao e obrigatoria para esse projeto especifico.)

Crie um ambiente virtual e ative-o (altamente recomendado):

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar no Linux/macOS
source venv/bin/activate

# Ativar no Windows
venv\Scripts\activate.bat
```

Instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Execução do Pipeline (Execução sem DVC)

Para rodar o pipeline completo, execute o script `main.py` a partir da raiz do projeto:

```bash
 python -m src.main
```

Na primeira execução, a tarefa de extração criará um arquivo `data/input.csv` com 10.000 linhas de dados sintéticos.

### 4. Versionamento dos Dados com DVC

Execute o pipeline completo com DVC:

```bash
dvc repro
```

Envie os dados versionados para o armazenamento remoto:

```bash
dvc push
```
