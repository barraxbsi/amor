import streamlit as st
from datetime import datetime
import os
import base64

# Configuração da página
st.set_page_config(
    page_title="Nossos 8 Meses ❤️",
    page_icon="💖",
    layout="centered"
)

# Controla se já entrou no site
if 'entb' not in st.session_state:
    st.session_state.entb = False

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
    if os.path.exists(nome_arquivo):
        st.video(nome_arquivo)
    else:
        st.info(f"💡 Para exibir o vídeo, adicione o arquivo **'{nome_arquivo}'** na pasta 'amor'.")


# --- TELA INICIAL (CAPA COM BOTÃO) ---
if not st.session_state.entb:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title("💖 Uma Surpresa Para Você 💖")
    st.markdown("### Prepare o coração e aperte o botão abaixo para entrarmos juntos na nossa história...")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_centro1, col_centro2, col_centro3 = st.columns([1, 2, 1])
    with col_centro2:
        if st.button("✨ Entrar no Nosso Mundinho ❤️", use_container_width=True):
            st.session_state.entb = True
            st.rerun()
            
    st.markdown("<br><br>", unsafe_allow_html=True)

else:
    # --- SITE COMPLETO (APÓS CLICAR NO BOTÃO) ---
    
    # Título Principal
    st.title("❤️ Nossos 8 Meses Juntos ❤️")
    st.subheader("O melhor capítulo da minha vida!")

    st.divider()

    # --- TEXTO INICIAL DE ABERTURA ---
    st.markdown("### 📜 Como Tudo Começou...")
    st.write("""
    Hoje a gente completa 8 meses juntos, e olhar pra trás me faz ter certeza de como a vida é incrível.

    Tudo começou meio sem querer, de repente... Eu vi uma foto sua no Instagram, achei a menina mais linda e perfeita do mundo — uma verdadeira princesa — e tomei coragem pra te seguir e mandar aquela primeira mensagem tentando puxar assunto. Quem diria que aquele papo bobo de internet se transformaria na melhor escolha da minha vida?

    Foi como na música "Meteoro": você chegou de repente, como um raio de luz, e me conquistou por inteiro. Naquele momento, eu já estava completamente apaixonado.

    Nesses 8 meses, cada instante do seu lado só reafirma o quanto eu te amo. Hoje eu sei que você é o meu "Destino" e que o nosso encontro não foi por acaso. 
    
    Você é aquela minha "Morena" (ou "Princesa") que traz paz pro meu dia, a companheira perfeita e a minha eterna Fofuxa. Como diz o Luan em "Tudo o Que Você Quiser": “Eu cometo os erros que for / Para ter o seu amor / Te dei o meu mundo e você deu o seu”. E é exatamente assim que eu me sinto: daria o meu mundo inteiro pra ver você sorrir.

    Obrigado por ser essa namorada maravilhosa e tão especial. Que venham muitos e muitos meses — e anos! — ao seu lado. Eu amo você! ❤️✨""")

    st.divider()

    # --- MÚSICAS TEMA NO TOPO ---
    st.markdown("### 🎵 Trilha Sonora do Nosso Amor")
    st.write("Dê o play abaixo para embalar a nossa história enquanto você vê tudo por aqui! ❤️")

    st.markdown("#### 🌟 Luan Santana - METEORO")
    st.video("https://youtu.be/A8iwQscRxDY?si=jYx_yeguY1e3iyQZ")

    st.markdown("#### 🌟 Luan Santana - MEU DESTINO")
    st.video("https://youtu.be/fziTdh7aELA?si=ngtz9J37D2LkXV2S")

    st.markdown("#### 🌟 Luan Santana - MORENA")
    st.video("https://youtu.be/ZIiQ1jMqhVM?si=aHAcmZiL6Z-Jr0jE")

    st.markdown("#### 🌟 Luan Santana - TUDO QUE VOCÊ QUISER")
    st.video("https://youtu.be/-YzDsDMYqdw?si=2RvzyB_8FQlKxSmP")

    st.markdown("#### 🌟 Luan Santana - INCONDICIONAL")
    st.video("https://youtu.be/oNiGxfh-Su0?si=y076X75_r6hD9O3I")

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
    Estes 8 meses ao seu lado foram os mais incríveis da minha vida. Obrigado por cada sorriso, 
    cada abraço e por tornar meus dias muito mais felizes. 

    A gente não precisa tá colado pra tá junto! AMAR NÃO É PECADO, QUE SE DANE O MUNDO, EU QUERO SÓ VOCÊ. Que venham muitos e muitos outros meses e anos ao seu lado! ❤️
    """)

    st.divider()

    # --- VÍDEOS NO FINAL COM TEXTO ESPECIAL ---
    st.markdown("### 🎥 Nossos Vídeos Especiais")

    st.write("""
    Lembro como se fosse hoje... da nossa primeira mensagem no celular, do frio na barriga antes de nos encontrarmos, 
    do nosso primeiro abraço apertado e daquele nosso primeiro beijo inesquecível que mudou tudo. 

    Parece que foi ontem que a nossa história começou, mas ao mesmo tempo sinto que te conheço de outras vidas. 
    Cada segundo ao seu lado fez esses 8 meses parecerem um sonho perfeito.
    Oito meses se passaram desde aquele dia que mudou tudo. Ainda me lembro do meu coração batendo forte. 
    Desde então, o tempo voou e cada dia ao seu lado virou uma aventura nova. 
    Obrigado por me fazer tão feliz e por ser essa pessoa incrível.
    Que venham muitos outros meses e anos juntos. Eu te amo! 
    Dê o play abaixo e relembre um pouquinho de nós! ❤️
    """)

    carregar_video_final("nosso_video.mp4")
    
    st.markdown("<br>", unsafe_allow_html=True)
    carregar_video_final("Oito_meses_no_mesmo_caminho.mp4")

    st.divider()

    # --- ÁREA DE ENVIO DE FOTO ---
    st.markdown("### 📸 Deixe uma Lembrança Nossa!")
    st.write("Fofuxa, escolha uma foto especial nossa e escreva uma legenda para eu adicionar aqui no nosso site! ❤️")

    seu_email = "wagnerbarral7@gmail.com"

    form_html = f"""
    <form action="https://formsubmit.co/{seu_email}" method="POST" enctype="multipart/form-data" style="background-color: #fff0f3; padding: 20px; border-radius: 12px; border: 1px solid #ffccd5;">
        <input type="hidden" name="_subject" value="❤️ Nova foto enviada no site!">
        <input type="hidden" name="_captcha" value="false">
        
        <label style="font-weight: bold; color: #9e2a2b;">Selecione a foto:</label><br>
        <input type="file" name="attachment" accept="image/*" required style="margin-bottom: 15px; margin-top: 5px;"><br>
        
        <label style="font-weight: bold; color: #9e2a2b;">Sua legenda ou mensagem especial:</label><br>
        <textarea name="mensagem" placeholder="Escreva algo sobre essa foto..." required style="width: 100%; height: 80px; padding: 8px; border-radius: 8px; border: 1px solid #ccc; margin-top: 5px; margin-bottom: 15px;"></textarea><br>
        
        <button type="submit" style="background-color: #d62828; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; width: 100%;">
            💌 Enviar Foto para o Nosso Site
        </button>
    </form>
    """
    st.components.v1.html(form_html, height=270)

    st.divider()

    # --- SURPRESA ---
    if st.button("Clique aqui para uma surpresa! 🎁"):
        st.balloons()
        st.success("Eu te amo infinitamente! Obrigado por estes 8 meses incríveis, minha Fofuxa! 🥰")