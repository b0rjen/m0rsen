# m0rsen 🔤📡

![m0rsen demo](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzEzOG05cXgxM3NlOXl3dWNmZnF2M2I5aHFxNm5xYWs5ajZiaDloMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l3vRo4I3onaS1Mz6M/giphy.gif)

**m0rsen** es una aplicación interactiva desarrollada en Python con Streamlit que permite traducir texto a código Morse y viceversa de manera sencilla e intuitiva. Ideal para aprender, practicar, o simplemente divertirte con el lenguaje Morse.

---

## 🚀 Características principales

- 🔤 **Conversión de texto a código Morse** con soporte para letras, números y símbolos de puntuación comunes.
- 📡 **Conversión de código Morse a texto** con validación automática del formato.
- 📚 **Diccionario interactivo** en la barra lateral para añadir caracteres rápidamente al texto.
- 🧠 **Validación de formato Morse** para evitar errores de entrada.
- 🧼 **Botones de borrar, traducir y copiar** (simulados) para ambas direcciones.
- 💬 **Interfaz clara y amigable** con explicaciones y ejemplos integrados.
- ✍️ **Uso de `st.session_state`** para mantener el texto entre interacciones.

---

## 📦 Requisitos

- Python 3.8+
- Streamlit

Puedes instalar Streamlit ejecutando:

```bash
pip install streamlit
```

---

## ▶️ Cómo ejecutar

Simplemente ejecuta el siguiente comando en tu terminal dentro del directorio del proyecto:

```bash
streamlit run app.py
```

---

## 🧪 Ejemplos de uso

### Texto a Morse:

```
Hola mundo
```

Se convierte en:

```
.... --- .-.. .- / -- ..- -. -.. ---
```

### Morse a texto:

```
-. --- / -- . / --. ..- ... - .- -. / .-.. .- ... / .- .-.. -.-. .- -.-. .... --- ..-. .- ... -.-.--
```

Se convierte en:

```
(averígualo tú mismo 🤪)
```

---

## 🛠️ Próximos pasos y versiones en las que estoy trabajando

- 🎤 Integración con reconocimiento de voz para traducir audio en tiempo real.
- 📱 Versión optimizada para dispositivos móviles.
- 🧩 Exportación a audio Morse (beeps y tonos).

---

## 📌 Créditos

Desarrollado por [b0rjen] como parte de su portfolio y como curiosidad.  
Con mucho 💙 por python 🐉 como siempre!

---

## 🧭 Licencia

Este proyecto es de uso libre. Cópialo, modifícalo o aprende de él.  
Eso sí, cualquier cambio o mejora que lo hagas, dímelo que me interesa 🙂🤝🙂