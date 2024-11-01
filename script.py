# Importação das bibliotecas necessárias
import requests  # Biblioteca para fazer requisições HTTP
import pandas as pd  # Biblioteca para manipulação e análise de dados
import os  # Biblioteca para operações com o sistema de arquivos
from datetime import datetime, timedelta  # Biblioteca para manipulação de datas
from dotenv import load_dotenv # Biblioteca para carregar o arquivo .env com as variáveis de ambiente


# Definição da chave de API para acesso à API da NASA
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
api_key = os.getenv('API_KEY')

# Função para obter dados da API
def obter_dados_api(url):
    """
    Esta função recebe uma URL e realiza uma requisição GET.
    Se a requisição for bem-sucedida (status 200), ela retorna os dados JSON.
    Caso contrário, exibe uma mensagem de erro com o código de status HTTP e retorna None.

    Parâmetros:
    url (str): URL da API para consulta.

    Retorno:
    dict ou None: Retorna um dicionário com os dados JSON ou None em caso de erro.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro {response.status_code} ao acessar a API para {url}")
        return None

# Função para baixar e salvar fotos
def salvar_foto(url, caminho):
    """
    Esta função baixa a imagem a partir de uma URL e salva no caminho especificado.

    Parâmetros:
    url (str): URL da imagem para download.
    caminho (str): Caminho do sistema de arquivos onde a imagem será salva.
    """
    try:
        img_data = requests.get(url).content
        with open(caminho, 'wb') as handler:
            handler.write(img_data)
    except Exception as e:
        print(f"Erro ao baixar a imagem {url}: {e}")

# Parâmetros de intervalo de datas
# Define o intervalo de datas que será consultado na API da NASA
data_inicio = datetime(2024, 9, 27)
data_fim = datetime(2024, 10, 27)
delta = timedelta(days=1)

# Lista para armazenar dados de todas as fotos obtidas
todas_as_fotos = []

# Loop para percorrer cada dia no intervalo de datas
data_atual = data_inicio
while data_atual <= data_fim:
    data_str = data_atual.strftime("%Y-%m-%d")
    # Formata a URL da API para o dia atual
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/Perseverance/photos?earth_date={data_str}&api_key={api_key}"
    
    # Obtém os dados da API para a data atual
    dados = obter_dados_api(url)
    if dados and 'photos' in dados:
        fotos = dados['photos']
        
        for foto in fotos:
            # Adiciona as informações da foto à lista de dados
            todas_as_fotos.append({
                'id': foto['id'],
                'earth_date': foto['earth_date'],
                'camera_name': foto['camera']['name'],
                'img_src': foto['img_src']
            })
            
            # Cria uma pasta para a data e salva a imagem
            pasta_data = os.path.join("fotos_perseverance", data_str)
            os.makedirs(pasta_data, exist_ok=True)
            nome_arquivo = os.path.join(pasta_data, f"{foto['id']}.jpg")
            salvar_foto(foto['img_src'], nome_arquivo)
    
    # Incrementa a data para o próximo dia
    data_atual += delta

# Converte os dados das fotos em um DataFrame e salva como CSV
df = pd.DataFrame(todas_as_fotos)
df.to_csv("dados_fotos_perseverance.csv", index=False)
print("Dados salvos com sucesso no arquivo 'dados_fotos_perseverance.csv'")