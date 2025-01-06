# 🤖 Chatbot con IA usando Groq, Streamlit y Codespaces 🚀

¡Bienvenido a mi primer proyecto de chatbot interactivo! 🌟 Este proyecto fue creado con el objetivo de aprender a trabajar con **modelos de lenguaje de IA**, explorar la integración con **Groq**, y desarrollar una interfaz gráfica utilizando **Streamlit**. Además, todo el desarrollo se realiza directamente en **Codespaces** con integración automática a **GitHub**. 🎯

---

## 🛠️ Tecnologías utilizadas:

- **Groq**: Plataforma de IA avanzada con modelos como `Mixtral` y `Llama 3`, que permiten generar respuestas de manera eficiente y precisa. 🌐
- **Streamlit**: Herramienta que permite crear interfaces web interactivas de forma sencilla y rápida. 📊
- **GitHub Codespaces**: Entorno de desarrollo en la nube que permite programar y probar el proyecto en un ambiente completamente configurado. ☁️
- **Python**: Lenguaje de programación principal utilizado en el desarrollo del chatbot. 🐍

---

## 🌟 Descripción del Proyecto

Este chatbot permite interactuar con modelos avanzados de IA para responder consultas en lenguaje natural. 🧠 El usuario puede:
1. **Seleccionar un modelo de IA** (por ejemplo, `Mixtral` o `Llama 3`).
2. **Ingresar una pregunta** y recibir una respuesta generada por el modelo seleccionado.
3. Visualizar un **historial de consultas y respuestas** en la misma interfaz. 📝

La aplicación utiliza un diseño limpio y funcional para que la experiencia de usuario sea fluida y agradable. 😄

---

## 🔑 Configuración de la API Key de Groq

Para poder utilizar los modelos de **Groq**, necesitas obtener una **API Key** desde su consola web:

1. **Crea una cuenta o inicia sesión** en [Groq Console](https://console.groq.com).
2. Navega a la sección de **API Keys** y genera una nueva clave.
3. Copia la API key generada.

Luego, crea un archivo llamado `.env` en la raíz del proyecto y agrega la API key de la siguiente manera:

```plaintext
groq_api_key=TU_API_KEY_AQUÍ
```

---

## 🖥️ ¿Cómo funciona la aplicación?

1. **Ejecución en Codespaces**:
   - Abre tu repositorio en **GitHub Codespaces** y asegúrate de que el entorno esté configurado con Python y Streamlit.
   - Inicia la aplicación con:
     ```bash
     streamlit run app.py
     ```
   - Accede al puerto que se muestra en la terminal para ver la interfaz web.

2. **Interfaz en Streamlit**:
   - **Panel lateral**: Selección del modelo de IA y personalización.
   - **Caja de texto**: Ingreso de la consulta.
   - **Sección de resultados**: Visualización de la respuesta generada por el modelo.

---

## 🚀 Objetivo de aprendizaje

Este proyecto tiene como finalidad:
- Familiarizarme con la creación de **interfaces web con Streamlit**.
- Comprender cómo interactuar con APIs de **modelos de IA en Groq**.
- Gestionar y desplegar un proyecto directamente desde **Codespaces** con integración continua a GitHub.
- Mejorar mis habilidades en el manejo de **Python** y herramientas de colaboración.

---

## 📚 Requisitos de instalación

Para ejecutar esta aplicación localmente, asegúrate de tener las siguientes dependencias:

```bash
pip install streamlit python-dotenv groq
```

---

## 📂 Estructura del Proyecto

```
📦 LLM-Groq
 ┣ 📜 .env              # Variables de entorno (API key)
 ┣ 📜 .gitignore        # Archivos a excluir del control de versiones
 ┣ 📜 LICENSE           # Licencia del proyecto
 ┣ 📜 app.py            # Archivo principal de la aplicación
 ┗ 📜 README.md         # Archivo de documentación
```

---

## 🌐 Integración con GitHub

Gracias a **Codespaces**, puedo trabajar en mi proyecto desde cualquier lugar sin necesidad de configurar un entorno local. Los cambios se sincronizan automáticamente con el repositorio de GitHub, asegurando un flujo de trabajo ágil y eficiente. 🖥️🔄

---

## 💡 Próximos pasos

🔧 Mejoras planeadas:
- Implementar un sistema de autenticación de usuarios.
- Añadir más opciones de personalización en la interfaz.
- Probar nuevos modelos de IA compatibles.

---

## 📢 ¡Conéctate conmigo!

Si tienes alguna sugerencia o pregunta sobre el proyecto, ¡no dudes en contactarme o dejar tus comentarios! 🤗

---

### ✨ Gracias por visitar mi proyecto ✨
