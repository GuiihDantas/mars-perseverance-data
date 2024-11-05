# Mars Perseverance Data

Repositório criado para a matéria de **Data Integration** do MBA em Data Engineering. O projeto realiza a coleta e organização de dados e imagens do rover Perseverance em Marte, usando a [API da NASA](https://api.nasa.gov/).

## Descrição do Projeto

O objetivo deste projeto é explorar a API pública da NASA para coletar dados e imagens do rover Perseverance e organizá-los de forma tabular. As imagens coletadas são organizadas em diretórios por data, e os metadados são armazenados em um arquivo CSV para posterior análise.

### Funcionalidades

- Coleta de dados JSON via API.
- Conversão dos dados para o formato tabular.
- Armazenamento das imagens em diretórios organizados por data.
- Exportação dos metadados para um arquivo CSV.

## Estrutura do Projeto

```plaintext
mars-perseverance-data/
├── .env                        # Arquivo com variáveis de ambiente, como a API_KEY
├── fotos_perseverance/         # Diretório onde as fotos são salvas organizadas por data
├── script.py                   # Script principal do projeto
├── dados_fotos_perseverance.csv  # Arquivo CSV com os metadados das fotos
├── README.md                   # Este arquivo README
└── requirements.txt            # Arquivo com as dependências do projeto
```

## Pré-requisitos

- **Python 3.6+**
- **Bibliotecas**: `requests`, `pandas`, `python-dotenv`

## Passo a Passo para Configuração e Execução

### 1. Crie e Ative o Ambiente Virtual

Para manter as dependências do projeto organizadas e isoladas:

```bash
python3 -m venv venv  # Cria o ambiente virtual
source venv/bin/activate  # Ativa o ambiente virtual no Linux/MacOS
venv\Scripts\activate  # No Windows
```

### 2. Instale as Dependências

Com o ambiente virtual ativo, instale as bibliotecas necessárias:

```bash
pip install requests pandas python-dotenv
```

Para registrar essas dependências em um arquivo `requirements.txt` e facilitar futuras instalações, execute:

```bash
pip freeze > requirements.txt
```

### 3. Configuração do Arquivo `.env`

O arquivo `.env` armazena a chave da API da NASA para acessar os dados. Na raiz do projeto, crie um arquivo `.env` e adicione a variável `API_KEY` com a sua chave:

```plaintext
API_KEY=SUA_CHAVE_API
```

Substitua `SUA_CHAVE_API` pela sua chave real obtida no [site da API da NASA](https://api.nasa.gov/).

### 4. Execute o Script

Com o ambiente configurado e as dependências instaladas, rode o script principal:

```bash
python script.py
```

O script fará o seguinte:
- Coletará dados e imagens do rover Perseverance na API da NASA.
- Organizará as imagens em pastas por data, dentro do diretório `fotos_perseverance`.
- Salvará os metadados das imagens no arquivo `dados_fotos_perseverance.csv`.

## Documentação

A documentação do código pode ser gerada automaticamente com o `pydoc`. Para gerar um arquivo HTML de documentação:

```bash
python -m pydoc -w script
```

Isso cria um arquivo `script.html` com a documentação do código, que pode ser aberta no navegador.

## Autor

- **Guilherme Dantas Barbosa**
- [LinkedIn](https://www.linkedin.com/in/guiihdantas-fab/) 

