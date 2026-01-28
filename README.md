# 🌱 KICHWA – Clasificación de Vestimenta Tradicional

**KICHWA** es una aplicación web interactiva desarrollada con **Streamlit** y **Deep Learning**, cuyo objetivo es fortalecer el aprendizaje del idioma **Kichwa** mediante el reconocimiento automático de prendas de vestir y su traducción al vocabulario ancestral.

El proyecto combina **visión por computadora**, **redes neuronales convolucionales** y recursos multimedia (imágenes y audios) para promover la **preservación cultural** y el aprendizaje significativo de la vestimenta tradicional andina.

---

## 🚀 Funcionalidades principales

- 📸 **Clasificación automática de prendas** a partir de imágenes
- 🧠 Modelo de Deep Learning basado en **ResNet34 entrenado desde cero**
- 🌱 Traducción inmediata del nombre de la prenda a **Kichwa**
- 🔊 Audios explicativos para mejorar la pronunciación
- 🖼️ Galería visual educativa de prendas tradicionales
- 📊 Análisis gráfico del reconocimiento del vocabulario Kichwa
- 🌐 Despliegue en **Streamlit Cloud**

---

## 🧠 Modelo de Inteligencia Artificial

- Arquitectura: **ResNet34**
- Framework: **PyTorch**
- Enfoque: Clasificación de imágenes de vestimenta
- Número de clases: **14 prendas**
- Precisión global: **~89%**
- Dataset:
  - Imágenes de prendas comunes y tradicionales
  - Organización por clases
  - Normalización y data augmentation

El modelo fue entrenado y evaluado localmente y luego integrado directamente en la aplicación web para inferencia en tiempo real.

---

## 📂 Estructura del proyecto
KICHWA/

├── Audios/ # Audios en Kichwa

├── Imagenes/ # Imágenes educativas

├── model/

│ └── resnet_kichwa_fast.pt

├── train/

│ └── train.ipynb # Entrenamiento del modelo

├── app.py # Aplicación Streamlit

├── requirements.txt

└── README.md


---

## 🛠️ Tecnologías utilizadas

- Python 3
- Streamlit
- PyTorch
- Torchvision
- PIL / Pillow
- NumPy
- Pandas
- Matplotlib

---

## 🌎 Importancia cultural

El idioma **Kichwa** forma parte del patrimonio cultural del Ecuador.  
Este proyecto busca contribuir a su preservación mediante el uso de tecnología educativa, facilitando el acceso a recursos digitales que fortalecen la identidad cultural y el aprendizaje intercultural.

---

## 📌 Nota académica

Este proyecto fue desarrollado con fines **educativos y académicos**, como parte de un trabajo de integración tecnológica orientado al uso de **Big Data, Inteligencia Artificial y Visión por Computadora** en contextos culturales y lingüísticos.

---

## 🔗 Demo en línea

👉 https://kichwa.streamlit.app

