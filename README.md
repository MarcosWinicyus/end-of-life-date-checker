# End of Life Date Checker

Este é um aplicativo simples de monitoramento de datas de fim de suporte (EOL - End of Life) para tecnologias populares, construído com Streamlit. O aplicativo consome dados da API [End of Life Date](https://endoflife.date/) para fornecer informações sobre as versões e ciclos de suporte de diversos produtos de tecnologia, permitindo filtros por datas de suporte e alertas de proximidade com o fim do suporte.

## Funcionalidades

- Exibe datas de suporte de versões de diversos produtos.
- Filtros dinâmicos para mostrar apenas versões com suporte ativo.
- Alertas de versões próximas do fim de suporte (customizável pelo usuário).
- Coloração condicional para fácil visualização das versões em suporte e próximas do EOL.

## Instalação

### Pré-requisitos

- Python 3.7+
- Recomendamos o uso de um ambiente virtual para evitar conflitos de dependências.

### Passos para instalação

1. Clone o repositório:
   ```bash
    https://github.com/MarcosWinicyus/end-of-life-date-checker.git
    cd end-of-life-date-checker
   ```
2. Crie e ative um ambiente virtual:
   ```bash
    python -m venv venv
    source venv/bin/activate        # Linux/MacOS
    .\venv\Scripts\activate         # Windows
   ```
3. Instale as dependências:
   ```bash
    pip install -r requirements.txt
   ```
### Uso
1. Execute o aplicativo Streamlit:
   ```bash
    streamlit run app.py
   ```
2. Abra seu navegador e acesse o endereço fornecido pelo Streamlit (geralmente, http://localhost:8501).

## Estrutura do Projeto

- `endoflife.py`: Código principal do aplicativo.
- `README.md`: Documentação do projeto.
- `requirements.txt`: Lista de dependências para instalação.

## Exemplo de Uso

1. Abra o aplicativo no navegador e selecione o produto desejado.
2. Visualize as versões disponíveis e aplique filtros conforme necessário.
3. Ajuste o limiar de alerta para ver quais versões estão próximas do fim do suporte.

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.



