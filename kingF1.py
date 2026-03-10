import plotly.graph_objects as go

# 1. Dados extraídos (a "matéria-prima" que você pegou da API)
# Lógica: Criamos listas com os nomes (labels) e os valores numéricos.
labels = ['Senna (1991 - Pole)', 'Referência Atual (2023)']
tempos = [76.392, 93.35]  # Tempos em segundos

# 2. Criando o Objeto do Gráfico
# Lógica: Usamos o 'graph_objects' do Plotly. Dizemos que queremos um gráfico de barras (go.Bar).
fig = go.Figure(data=[go.Bar(
    x=labels,              # O que fica no eixo X (os nomes)
    y=tempos,              # O que fica no eixo Y (os números)
    text=tempos,           # O texto que aparece sobre a barra (para ser interativo)
    textposition='auto',   # Onde o texto fica (automático)
    marker_color=['#f1c40f', '#0071e3'], # Cores Apple: Amarelo Senna e Azul Moderno
    hoverinfo='text+x'     # Lógica: O que aparece quando passa o mouse (valor + nome)
)])

# 3. Customizando o Layout
# Lógica: Adicionamos títulos, rótulos de eixo e garantimos a fonte padrão do site (para combinar).
fig.update_layout(
    title={
        'text': "Evolução em Interlagos: Senna vs Era Moderna",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title="Piloto / Era",
    yaxis_title="Tempo de Volta (segundos)",
    font=dict(
        family="Helvetica, Arial, sans-serif", # Mesma fonte do seu site Apple
        size=12,
        color="#1d1d1f" # Cor de texto padrão Apple
    ),
    paper_bgcolor='rgba(0,0,0,0)', # Fundo transparente para casar com o site
    plot_bgcolor='rgba(0,0,0,0)',   # Fundo do plot transparente
    bargap=0.4 # Espaço entre as barras (layout mais limpo)
)

# 4. SALVANDO COMO HTML (O "Pulo do Gato" para o Portfólio)
# Lógica: Como seu site é estático, não podemos rodar Python nele.
# Salvar como .html gera um arquivo que contém o gráfico e o JavaScript necessário.
# O parâmetro include_plotlyjs='cdn' faz o arquivo ficar leve, puxando a biblioteca da nuvem.
fig.write_html('grafico_f1.html', include_plotlyjs='cdn')

print("✅ Gráfico interativo gerado e salvo como 'grafico_f1.html'!")