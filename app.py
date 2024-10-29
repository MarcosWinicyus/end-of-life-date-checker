import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# URL base da API
BASE_URL = "https://endoflife.date/api/"

# Função para consultar a API com cache
@st.cache_data(ttl=3600)
def fetch_data(endpoint):
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            st.error(f"Erro 404: O endpoint '{endpoint}' não foi encontrado.")
        else:
            st.error(f"Erro HTTP {response.status_code}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao buscar dados: {e}")
        return None

# Função para processar dados do produto
def process_product_data(data):
    df = pd.DataFrame(data)
    # Converter colunas de datas se existirem
    date_columns = ['eol', 'releaseDate', 'support']
    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], format='%Y-%m-%d', errors='coerce')
    return df

# Função para colorir células com base na data de EOL
def life_cycle_alerts(val):
    if pd.isnull(val):
        color = ''
    else:
        days_remaining = (val - datetime.now()).days
        if days_remaining < 0:
            color = 'red'
        elif days_remaining < 180:
            color = 'yellow'
        else:
            color = 'green'
    return f'background-color: {color}'

# Interface do Streamlit
st.title("Verificador de Datas de Suporte (End of Life Date Checker)")
st.write("""
Verifique as datas de suporte de tecnologias populares. 
Manter-se atualizado com as datas de fim de vida (EOL) é crucial para garantir a segurança e estabilidade de seus sistemas.
""")

# Carregar lista de produtos
all_products = fetch_data("all.json")  # Endpoint de produtos

if all_products is not None:
    # Ordenar produtos para melhor usabilidade
    all_products.sort()
    # Menu para selecionar o produto
    product = st.selectbox("Selecione um produto:", all_products)
    
    # Carregar dados do produto selecionado
    data_product = fetch_data(f"{product}.json")  # Endpoint de versões
    
    if data_product is not None:
        df = process_product_data(data_product)
        
        # Filtro por data de suporte
        st.subheader(f"Versões de {product}")
        show_only_supported = st.checkbox("Mostrar apenas versões com suporte ativo", value=False)
        if show_only_supported:
            today = pd.to_datetime(datetime.now())
            df = df[df['eol'] > today]
        
        # Exibir dataframe com coloração condicional
        styled_df = df.style.applymap(life_cycle_alerts, subset=['eol'])
        st.dataframe(styled_df)
        
        # Alertas para versões próximas do EOL
        st.subheader("Alertas:")
        days_threshold = st.slider("Definir limiar de dias para alerta de EOL:", min_value=30, max_value=365, value=180)
        today = datetime.now()
        df['days_to_eol'] = (df['eol'] - today).dt.days
        alert_df = df[(df['days_to_eol'] >= 0) & (df['days_to_eol'] <= days_threshold)]
        
        if not alert_df.empty:
            st.warning("As seguintes versões estão próximas do fim de suporte:")
            st.table(alert_df[['cycle', 'eol', 'days_to_eol']])
        else:
            st.success("Nenhuma versão próxima do fim de suporte dentro do limiar definido.")
    else:
        st.error("Não foi possível carregar os dados do produto selecionado.")
else:
    st.error("Não foi possível carregar a lista de produtos.")
