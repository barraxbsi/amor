import streamlit as st
from datetime import datetime
import os
import base64

# Configuração da página
st.set_page_config(
    page_title="Nossos 7 Meses ❤️",
    page_icon="💖",
    layout="centered"
)

# Função para converter imagens em base64
def get_b64(nome_arquivo):
    extensoes = [
        nome_arquivo,
        nome_arquivo.replace(".jpg", ".png"),
        nome_arquivo.replace(".jpg", ".jpeg"),
        nome_arquivo.replace(".jpg", ".JPG"),
        nome_arquivo.replace(".jpg", ".PNG"),
        nome_arquivo.replace(".jpg", ".JPEG")
    ]
    for ext in extensoes:
        if os.path.exists(ext):
            with open(ext, 'rb') as f:
                return base64.b64encode(f.read()).decode()
    return ""

# Carrega as 6 fotos do mosaico de fundo
img1 = get_b64("mosaico1.jpg")
img2 = get_b64("mosaico2.jpg")
img3 = get_b64("mosaico3.jpg")
img4 = get_b64("mosaico4.jpg")
img5 = get_b64("mosaico5.jpg")
img6 = get_b64("mosaico6.jpg")

# CSS do Mosaico no Fundo
mosaico_css = f"""
<style>
.stApp {{
    background-color: #fff0f3;
}}

.bg-mosaico {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 0;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 4px;
    opacity: 0.35;
    pointer-events: none;
}}

.bg-mosaico div {{
    background-size: cover;
    background-position: center;
    border-radius: 8px;
}}

.main .block-container {{
    position: relative;
    z-index: 1;
    background-color: rgba(255, 255, 255, 0.92);
    padding: 2rem;
    border-radius: 20px;
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}}

h1 {{ color: #d62828 !important; text-align: center; font-weight: bold; }}
h2, h3 {{ color: #9e2a2b !important; text-align: center; }}
p, span, div, label {{ color: #2b2b2b !important; }}
[data-testid="stMetricValue"] {{ color: #d62828 !important; font-size: 2rem !important; font-weight: bold; }}
</style>

<div class="bg-mosaico">
    <div style="background-image: url('data:image/jpg;base64,{img1}');"></div>
    <div style="background-image: url('data:image/jpg;base64,{img2}');"></div>
    <div style="background-image: url('data:image/jpg;base64,{img3}');"></div>
    <div style="background-image: url('data:image/jpg;base64,{img4}');"></div>
    <div style="background-image: url('data:image/jpg;base64,{img5}');"></div>
    <div style="background-image: url('data:image/jpg;base64,{img6}');"></div>
</div>
"""

st.markdown(mosaico_css, unsafe_allow_html=True)

# Função auxiliar para exibir as imagens
def carregar_imagem(nome_arquivo, legenda=""):
    extensoes = [
        nome_arquivo,
        nome_arquivo.replace(".jpg", ".png"),
        nome_arquivo.replace(".jpg", ".jpeg"),
        nome_arquivo.replace(".jpg", ".JPG"),
        nome_arquivo.replace(".jpg", ".PNG"),
        nome_arquivo.replace(".jpg", ".JPEG")
    ]
    encontrado = None
    for ext in extensoes:
        if os.path.exists(ext):
            encontrado = ext
            break
            
    if encontrado:
        if legenda:
            st.image(encontrado, caption=legenda, use_container_width=True)
        else:
            st.image(encontrado, use_container_width=True)
    else:
        st.warning(f"⚠️ Adicione **'{nome_arquivo}'** na pasta 'amor'.")

# Função auxiliar para carregar vídeo local
def carregar_video_final(nome_arquivo):
    extensoes = [
        nome_arquivo,
        "nosso_video.mp4",
        "nosso_video.mov",
        "nosso_video.avi",
        "nosso_video.mkv",
        "nosso_video.MP4"
    ]
    encontrado = None
    for ext in extensoes:
        if os.path.exists(ext):
            encontrado = ext
            break
            
    if encontrado:
        st.video(encontrado)
    else:
        st.info(f"💡 Para exibir seu vídeo no final, adicione o arquivo **'{nome_arquivo}'** (ou **nosso_video.mp4**) na pasta 'amor'.")

# Título
st.title("❤️ 7 Meses Juntos ❤️")
st.subheader("O melhor capítulo da minha vida!")

st.divider()

# --- CONTADOR DE TEMPO ---
data_inicio = datetime(2026, 2, 17, 19, 30) 
agora = datetime.now()
diferenca = agora - data_inicio

dias = diferenca.days
horas = diferenca.seconds // 3600
minutos = (diferenca.seconds % 3600) // 60

st.markdown("### ⏳ Contador do Nosso Amor")
col1, col2, col3 = st.columns(3)
col1.metric("Dias", f"{dias} dias")
col2.metric("Horas", f"{horas} hrs")
col3.metric("Minutos", f"{minutos} min")

st.divider()

# --- MÚSICA TEMA ---
st.markdown("### 🎵 Nossa Trilha Sonora: Te Vivo - Luan Santana")
youtube_music_url = "https://www.youtube.com/watch?v=dWpGsK8Md28" 
st.video(youtube_music_url, autoplay=True)

st.divider()

# --- GALERIA COM AS 50 FOTOS ---
st.markdown("### 📸 Nossa História em Fotos")

frases = [
    "O início de tudo ❤️", "Nossos momentos inesquecíveis!", "Cada dia mais juntos.", "Sorrisos que amo!", 
    "Mais um momento especial ao seu lado.", "Te amo cada dia mais!", "Parabéns para nós! ❤️", "O seu abraço é o meu lugar favorito.", 
    "Com você, tudo fica mais leve.", "Memórias que vou guardar para sempre.", "Amo tudo em você!", "O melhor presente foi te encontrar.", 
    "O meu sorriso favorito do mundo.", "Que a gente continue assim, bem juntinhos.", "Sempre ao seu lado ❤️", "Cada detalhe seu me encanta.", 
    "Você transforma meus dias.", "Amor sem fim!", "Sempre com você no meu coração.", "O destino acertou em cheio ao nos juntar.", 
    "Momentos simples que valem ouro.", "O meu porto seguro.", "Ao seu lado o tempo voa.", "Minha melhor companhia.", 
    "Construindo nossa história dia após dia.", "Eu te amo infinitamente! ❤️", "Cada segundo com você é especial.", "Meu porto seguro.", 
    "Nossa sintonia é única.", "Lugar favorito: abraçado(a) com você.", "Você é a melhor parte do meu dia.", "Sempre nós.", 
    "Risadas garantidas ao seu lado.", "Amor que não cabe no peito.", "Meu bem mais precioso.", "Coração acelerado só de te ver.", 
    "Companheiro(a) de todas as horas.", "A vida é mais bonita com você.", "Nossa cumplicidade é tudo.", "Florescendo juntos.", 
    "Te escolheria em todas as vidas.", "Tão bom viver isso com você.", "Olhar que me acalma.", "Nossas memórias favoritas.", 
    "Você é meu lar.", "Cada detalhe seu me faz suspirar.", "Meu amor maior.", "Tudo faz sentido com você.", 
    "Para sempre ao seu lado.", "Nosso amor é a minha história favorita! ❤️"
]

total_fotos = 50
for i in range(1, total_fotos + 1, 2):
    c1, c2 = st.columns(2)
    with c1:
        carregar_imagem(f"foto{i}.jpg", frases[i-1])
    if i + 1 <= total_fotos:
        with c2:
            carregar_imagem(f"foto{i+1}.jpg", frases[i])

st.divider()

# --- CARTA DE AMOR ---
st.markdown("### 💌 Uma mensagem para você")

st.write("""
Estes 7 meses ao seu lado foram os mais incríveis da minha vida. Obrigado por cada sorriso, 
cada abraço e por tornar meus dias muito mais felizes. 

A gente não precisa tá colado pra tá junto! Que venham muitos e muitos outros meses e anos ao seu lado! ❤️
""")

st.divider()

# --- VÍDEO NO FINAL COM TEXTO ESPECIAL ---
st.markdown("### 🎥 Um Vídeo Especial Para Você")

st.write("""
Lembro como se fosse hoje... da nossa primeira mensagem no celular, do frio na barriga antes de nos encontrarmos, 
do nosso primeiro abraço apertado e daquele nosso primeiro beijo inesquecível que mudou tudo. 

Parece que foi ontem que a nossa história começou, mas ao mesmo tempo sinto que te conheço de outras vidas. 
Cada segundo ao seu lado fez esses 7 meses parecerem um sonho perfeito.
Sete meses se passaram desde aquele dia que mudou tudo. Ainda me lembro do meu coração batendo forte. 
Desde então, o tempo voou e cada dia ao seu lado virou uma aventura nova. 
Obrigado por me fazer tão feliz e por ser essa pessoa incrível.
Que venham muitos outros meses e anos juntos. Eu te amo! 
Dê o play abaixo e relembre um pouquinho de nós! ❤️
""")

carregar_video_final("nosso_video.mp4")

st.divider()

# --- SURPRESA ---
if st.button("Clique aqui para uma surpresa! 🎁"):
    st.balloons()
    st.success("Eu te amo infinitamente! Obrigado por estes 7 meses incríveis! 🥰❤️")