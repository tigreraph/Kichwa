#KICHWA
import os
import streamlit as st

st.set_page_config(
    page_title="Kichwa",
    page_icon="🙋🏻‍♀️",
    layout="wide"
)
import base64
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ultralytics import YOLO
from PIL import Image
import tempfile

TRADUCCION_KICHWA = {
    "Anaco": "anaku",
    "Anillo": "wallka",
    "Camisa": "kamisa",
    "Collar": "wallka",
    "Faja delgada": "chumbi",
    "Manilla": "makipampa",
    "Pantalon": "wara",
    "Prendedor": "tupu",
    "Sombrero": "muchiku",
    "Zapato": "utusha",
    "blusa": "blusa",
    "camiseta": "kamisita",
    "faja madre": "hatun chumbi",
    "poncho": "ponchu"
}

@st.cache_resource
def load_model():
    from ultralytics import YOLO
    return YOLO("model/best.pt")


def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()




fondo_base64 = get_base64_image("fondo.png")

st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{fondo_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        /* Capa oscura para mejorar lectura */
        .overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.55);
            z-index: 0;
        }}

        .content {{
            position: relative;
            z-index: 1;
        }}

        h1, h2, h3, p {{
            color: white;
            text-align: center;
        }}
        
        .title-box {{
            color: white;
            text-align: center;
            background: rgba(0, 0, 0, 0.6);
            padding: 30px;
            border-radius: 20px;
            margin-bottom: 40px;
        }}

        .card {{
            background: rgba(255, 255, 255, 0.92);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-size: 20px;
            color: black;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }}
        .card h3,
        .card p {{
            color: black;
        }}

    </style>

    <div class="overlay"></div>
    """,
    unsafe_allow_html=True
)

#Audio de las prendas
def mostrar_audio(nombre):
    try:
        st.audio(f"Audios/{nombre}.mp3")
    except:
        st.info("🔊 Audio no disponible")

def mostrar_imagen(nombre):
    try:
        st.image(f"imagenes/{nombre}.png", use_container_width=True)
    except:
        st.warning("🖼 Imagen no disponible")


st.markdown('<div class="content">', unsafe_allow_html=True)

st.sidebar.title("📚 Menú")
seccion = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "🏠 Inicio",
        "👕 Aprende Kichwa – Vestimenta",
        "🧠 Clasificación de Prendas",
        "📈 Análisis gráfico del vocabulario Kichwa"
    ]
)
if seccion == "🏠 Inicio":
    st.markdown("""
    <div class="title-box">
        <h1>🌈 Proyecto Kichwa</h1>
        <h3>Aprendizaje interactivo de la vestimenta tradicional</h3>
        <p>
        Esta aplicación educativa tiene como objetivo fortalecer el aprendizaje
        del idioma Kichwa a través de recursos visuales, auditivos e interactivos,
        promoviendo la valoración de la identidad cultural andina.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="title-box">
        <h3>🎯 Objetivo del proyecto</h3>
        <p>
        Facilitar el reconocimiento y comprensión del vocabulario Kichwa
        relacionado con la vestimenta tradicional, utilizando tecnología
        como apoyo al proceso educativo y cultural.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="title-box">
        <h3>🧩 ¿Qué encontrarás en esta aplicación?</h3>
            <li>📌 Vocabulario Kichwa – Español con imágenes</li>
            <li>🔊 Audios explicativos para mejorar la pronunciación</li>
            <li>📊 Análisis gráfico del reconocimiento del vocabulario</li>
            <li>🧠 Clasificación de prendas mediante inteligencia artificial</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="title-box">
        <h3>🌱 Importancia cultural</h3>
        <p>
        El idioma Kichwa forma parte del patrimonio cultural del Ecuador.
        Su aprendizaje y preservación contribuyen a mantener vivas las
        tradiciones, conocimientos y formas de vida de los pueblos ancestrales.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "📌 Nota: Esta aplicación ha sido desarrollada con fines educativos, "
        "como parte de un proyecto académico enfocado en el uso de la tecnología "
        "para la preservación y difusión de lenguas ancestrales."
    )

    st.stop()


if seccion == "👕 Aprende Kichwa – Vestimenta":
    st.markdown("""
    <div class="title-box">
        <h1>🙋🏻‍♀️ CHURANAKUNA</h1>
        <h3>Aprendamos palabras sobre la vestimenta en Kichwa 🌱</h3>
    </div>
    """, unsafe_allow_html=True)

    prendas = [
        ("Anaku", "Anaco", "anaku",
        "El anaku es una prenda tradicional usada por las mujeres indígenas andinas. Representa identidad cultural y se utiliza en la vida diaria y en festividades."),

        ("Chumpi", "Faja", "chumpi",
        "El chumpi sirve para sujetar el anaku y simboliza fortaleza, protección y equilibrio del cuerpo."),

        ("Churana", "Ropa", "churana",
        "La churana se refiere de forma general a la vestimenta tradicional utilizada en la vida cotidiana."),

        ("Kunkallina", "Bufanda", "kunkallina",
        "La kunkallina protege del frío y es usada especialmente en zonas altas de la región andina."),

        ("Kushma", "Saco", "kushma",
        "La kushma es una prenda amplia usada tanto por hombres como mujeres, asociada a la protección y abrigo."),

        ("Pachallina", "Bayeta", "pachallina",
        "La pachallina es una tela tradicional utilizada para cargar objetos o como abrigo."),

        ("Llawtu", "Corona", "llawtu",
        "El llawtu es un símbolo de autoridad y liderazgo dentro de las comunidades indígenas."),

        ("Maki-watana", "Manilla / Pulsera", "maki_watana",
        "El maki-watana es un accesorio que representa identidad, protección espiritual y pertenencia cultural."),

        ("Mama chumpi", "Faja madre", "mama_chumpi",
        "La mama chumpi es una faja más ancha que simboliza sostén, fuerza y sabiduría ancestral."),

        ("Muchiku", "Sombrero", "muchiku",
        "El muchiku protege del sol y del frío, y su forma puede variar según la comunidad."),

        ("Muntira", "Gorra", "muntira",
        "La muntira es una prenda más moderna, adaptada a la vestimenta tradicional actual."),

        ("Pakcha", "Sábana", "pakcha",
        "La pakcha se usa como manta o sábana y forma parte del uso doméstico tradicional."),

        ("Pintu", "Camisa", "pintu",
        "El pintu es una prenda superior usada tanto en contextos cotidianos como ceremoniales."),

        ("Pintu ushuta", "Medias", "pintu_ushuta",
        "El pintu ushuta se utiliza para proteger los pies del frío, especialmente en zonas rurales."),

        ("Raku kushma", "Abrigo", "raku_kushma",
        "El raku kushma es una prenda gruesa que brinda abrigo en climas fríos."),

        ("Rinrina", "Arete", "rinrina",
        "La rinrina es un accesorio decorativo que representa belleza y expresión cultural."),

        ("Ruwana", "Poncho", "ruwana",
        "La ruwana es una prenda ancestral usada como abrigo y símbolo de identidad comunitaria."),

        ("Shikra", "Bolso", "shikra",
        "La shikra es un bolso tejido a mano, usado para transportar alimentos u objetos personales."),

        ("Shiwi", "Anillo", "shiwi",
        "El shiwi es un accesorio tradicional que representa unión y estética cultural."),

        ("Tupu", "Prendedor", "tupu",
        "El tupu se utiliza para sujetar la vestimenta y tiene un valor histórico y simbólico."),

        ("Uku kushma", "Camiseta", "uku_kushma",
        "El uku kushma es una prenda interior usada como base de la vestimenta tradicional."),

        ("Ushuta", "Zapato", "ushuta",
        "La ushuta es un calzado tradicional adaptado al entorno rural."),

        ("Alparkata", "Alpargates", "alparkata",
        "Las alparkatas son un calzado tradicional elaborado con materiales resistentes."),

        ("Wallka", "Collar", "wallka",
        "La wallka es un collar tradicional que simboliza belleza, identidad y estatus cultural."),

        ("Wara", "Pantalón", "wara",
        "La wara es una prenda masculina tradicional usada en actividades cotidianas."),

        ("Warmi wara", "Blusa", "warmi_wara",
        "La warmi wara es una prenda femenina que forma parte de la vestimenta tradicional."),

        ("Wawa chumpi", "Faja delgada", "wawa_chumpi",
        "La wawa chumpi es una faja delgada utilizada principalmente por niños y jóvenes."),
    ]

    # TEXTOS DE AUDIO
    textos_audio = {
        "anaku": "Anaku significa anaco.",
        "chumpi": "Chumpi significa faja.",
        "churana": "Churana significa ropa.",
        "kunkallina": "Kunkallina significa bufanda.",
        "kushma": "Kushma significa saco.",
        "pachallina": "Pachallina significa bayeta.",
        "llawtu": "Llawtu significa corona.",
        "maki_watana": "Maki-watana significa pulsera.",
        "mama_chumpi": "Mama chumpi significa faja madre.",
        "muchiku": "Muchiku significa sombrero.",
        "muntira": "Muntira significa gorra.",
        "pakcha": "Pakcha significa sábana.",
        "pintu": "Pintu significa camisa.",
        "pintu_ushuta": "Pintu ushuta significa medias.",
        "raku_kushma": "Raku kushma significa abrigo.",
        "rinrina": "Rinrina significa arete.",
        "ruwana": "Ruwana significa poncho.",
        "shikra": "Shikra significa bolso.",
        "shiwi": "Shiwi significa anillo.",
        "tupu": "Tupu significa prendedor.",
        "uku_kushma": "Uku kushma significa camiseta.",
        "ushuta": "Ushuta significa zapato.",
        "alparkata": "Alparkata significa alpargates.",
        "wallka": "Wallka significa collar.",
        "wara": "Wara significa pantalón.",
        "warmi_wara": "Warmi wara significa blusa.",
        "wawa_chumpi": "Wawa chumpi significa faja delgada."
    }


    for i in range(0, len(prendas), 3):
        cols = st.columns(3)
        for col, prenda in zip(cols, prendas[i:i+3]):
            with col:
                st.markdown(
                    f"""
                    <div class='card'>
                        <b>{prenda[0]}</b><br>
                        <small>{prenda[1]}</small>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                mostrar_imagen(prenda[2])
                mostrar_audio(prenda[2])

                st.caption(f"🎧 {textos_audio.get(prenda[2], 'Audio explicativo no disponible.')}")

                with st.expander("📖 Importancia cultural"):
                    st.write(prenda[3])


if seccion == "🧠 Clasificación de Prendas":
    st.title("📸 Clasificación de Prendas")

    uploaded_file = st.file_uploader(
        "Sube una imagen",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Imagen cargada", use_container_width=True)

        
        with st.spinner("Analizando imagen..."):
                # Guardar imagen temporalmente
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                    image.save(tmp.name)
                    img_path = tmp.name

                # Cargar modelo
                model = load_model()

                # Predicción
                results = model.predict(
                    source=img_path,
                    save=False
                )

                # Mostrar imagen con bounding boxes
                annotated = results[0].plot()
                st.image(
                    annotated,
                    caption="Resultado de la detección",
                    use_container_width=True
                )

                # Mostrar resultados en texto
                st.subheader("📋 Resultados")

                if len(results[0].boxes) == 0:
                    st.warning("No se detectaron prendas.")
                else:
                    for box in results[0].boxes:
                        cls_id = int(box.cls[0])
                        clase = model.names[cls_id]
                        confianza = float(box.conf[0])

                        kichwa = TRADUCCION_KICHWA.get(clase, "—")

                        st.markdown(
                            f"""
                            **Prenda:** {clase}  
                            **Confianza:** {confianza:.2f}  
                            **Kichwa:** {kichwa}
                            ---
                            """
                        )

                # Limpiar archivo temporal
                os.remove(img_path)
if seccion == "🌱 Cultura Kichwa":
    st.markdown("""
    <div class="title-box">
        <h1>🌱 Cultura Kichwa</h1>
        <p>
        El idioma Kichwa es una herencia ancestral que forma parte
        de la identidad cultural de los pueblos andinos del Ecuador.
        Preservarlo es preservar nuestra historia.
        </p>
    </div>
    """, unsafe_allow_html=True)


if seccion == "📈 Análisis gráfico del vocabulario Kichwa":
    st.markdown("""
    ### 📊 Análisis gráfico del reconocimiento del vocabulario

    La siguiente visualización presenta el nivel estimado de reconocimiento
    de las prendas de vestir en Kichwa, con el propósito de identificar
    aquellas palabras que requieren mayor refuerzo educativo.
    """)

    st.markdown("---")
    st.markdown("## 🏔️ Reconocimiento del vocabulario Kichwa – Vestimenta tradicional")

    if st.button("🌸 Mostrar gráfica"):
        
        prendas = [
            "Anaku (Anaco)", "Chumpi (Faja)", "Churana (Ropa)",
            "Kunkallina (Bufanda)", "Kushma (Saco)", "Pachallina (Bayeta)",
            "Llawtu (Corona)", "Maki-watana (Pulsera)", "Mama chumpi (Faja madre)",
            "Muchiku (Sombrero)", "Muntira (Gorra)", "Pakcha (Sábana)",
            "Pintu (Camisa)", "Pintu ushuta (Medias)", "Raku kushma (Abrigo)",
            "Rinrina (Arete)", "Ruwana (Poncho)", "Shikra (Bolso)",
            "Shiwi (Anillo)", "Tupu (Prendedor)", "Uku kushma (Camiseta)",
            "Ushuta (Zapato)", "Alparkata (Alpargates)", "Wallka (Collar)",
            "Wara (Pantalón)", "Warmi wara (Blusa)", "Wawa chumpi (Faja delgada)"
        ]

        reconocimiento = [
            70, 65, 75, 55, 60, 18, 12, 10, 25,
            58, 50, 20, 68, 22, 45, 40, 72,
            48, 35, 15, 52, 66, 30, 42,
            55, 50, 8
        ]

        df = pd.DataFrame({
            "Prenda": prendas,
            "Reconocimiento (%)": reconocimiento
        })


        cmap = plt.cm.Spectral
        colores = cmap(np.linspace(0.15, 0.85, len(prendas)))

        fig, ax = plt.subplots(figsize=(11, 10))

        barras = ax.barh(
            df["Prenda"],
            df["Reconocimiento (%)"],
            color=colores,
            edgecolor="white"
        )

        ax.set_xlim(0, 100)
        ax.set_xlabel("Nivel de reconocimiento (%)", fontsize=11)
        ax.set_ylabel("Prendas en Kichwa (con significado)", fontsize=11)
        ax.set_title(
            "Reconocimiento estimado del vocabulario Kichwa sobre vestimenta tradicional",
            fontsize=15,
            fontweight="bold"
        )

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        for i, v in enumerate(reconocimiento):
            ax.text(v + 1, i, f"{v}%", va="center", fontsize=9)

        plt.tight_layout()
        st.pyplot(fig)

        st.markdown("### 🎨 ¿Qué representan los colores de la gráfica?")
        st.markdown("""
        - 🔴 **Colores cálidos**: prendas con **bajo nivel de reconocimiento**  
        - 🟡 **Colores intermedios**: prendas **medianamente conocidas**  
        - 🟢 **Colores fríos**: prendas **ampliamente reconocidas**  

        La variación de colores permite identificar visualmente qué palabras del vocabulario Kichwa
        requieren mayor refuerzo educativo.
        """)

        st.info(
            "📌 Nota: Los datos presentados son simulados con fines educativos. "
            "La gráfica representa una estimación del nivel de reconocimiento del vocabulario Kichwa "
            "sobre vestimenta, con el objetivo de identificar palabras menos conocidas y justificar "
            "la necesidad de herramientas digitales para su enseñanza y preservación cultural."
        )
st.markdown("</div>", unsafe_allow_html=True)
