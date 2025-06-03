import streamlit as st
import re
import time

# Diccionario de código Morse
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

# Diccionario inverso (Morse a letra)
MORSE_TO_LETTER = {v: k for k, v in MORSE_CODE.items()}

def morse_to_text(morse_code):
    """Convierte código Morse a texto"""
    # Separar por espacios (cada grupo es una letra)
    morse_letters = morse_code.strip().split(' ')
    result = []
    
    for morse_letter in morse_letters:
        if morse_letter == '/':  # Separador de palabras
            result.append(' ')
        elif morse_letter in MORSE_TO_LETTER:
            result.append(MORSE_TO_LETTER[morse_letter])
        elif morse_letter == '':  # Espacios vacíos
            continue
        else:
            result.append(f'[{morse_letter}?]')  # Código no reconocido
    
    return ''.join(result)

def text_to_morse(text):
    """Convierte texto a código Morse"""
    text = text.upper()
    result = []
    
    for char in text:
        if char == ' ':
            result.append('/')  # Separador de palabras
        elif char in MORSE_CODE:
            result.append(MORSE_CODE[char])
        else:
            result.append(f'[{char}?]')  # Carácter no soportado
    
    return ' '.join(result)

def validate_morse(morse_code):
    """Valida si el código Morse tiene formato correcto"""
    # Solo permitir puntos, rayas, espacios y barras
    pattern = r'^[.\-\s/]+$'
    return bool(re.match(pattern, morse_code.strip()))

# Configuración de la página
st.set_page_config(
    page_title="Traductor de Código Morse",
    page_icon="📡",
    layout="wide"
)

# Título principal
st.title("📡 Traductor de Código Morse")
st.markdown("*Convierte entre texto y código Morse de forma bidireccional*")

# Sección de información antes de los traductores
st.header("ℹ️ Cómo usar")
col_info1, col_info2 = st.columns(2)

with col_info1:
    st.markdown("""
    **Formato del código Morse:**
    - Punto: `.`
    - Raya: `-`
    - Espacio entre letras: ` ` (espacio simple)
    - Separador de palabras: `/`
    
    **Ejemplo:**
    `.... --- .-.. .-` = HOLA
    """)

with col_info2:
    st.markdown("""
    **Letras soportadas:**
    - A-Z (todas las letras)
    - 0-9 (números)
    - Puntuación básica (. , ? ! / etc.)
    
    **Tip:** Los espacios en el texto se convierten en `/` en Morse
    """)

# Separador
st.markdown("---")

# Crear diseño principal con sidebar y contenido principal
# Sidebar para el diccionario
with st.sidebar:
    with st.expander("📚 Diccionario Morse", expanded=False):
        # Crear tabla de referencia
        morse_items = list(MORSE_CODE.items())
        
        st.markdown("**Letras A-Z**")
        for char, morse in morse_items:
            if char.isalpha():
                st.text(f"{char}: {morse}")
        
        st.markdown("**Números 0-9**")
        for char, morse in morse_items:
            if char.isdigit():
                st.text(f"{char}: {morse}")
                
        st.markdown("**Puntuación**")
        for char, morse in morse_items:
            if not char.isalnum() and char != ' ':
                st.text(f"{char}: {morse}")

# Crear dos columnas principales
col1, col2 = st.columns(2)

with col1:
    st.header("🔤 Texto a Morse")
    
    # Usar session state para el texto
    if 'text_input' not in st.session_state:
        st.session_state.text_input = ""
    
    text_input = st.text_area(
        "Escribe tu texto aquí:",
        value=st.session_state.text_input,
        height=150,
        placeholder="Escribe cualquier texto...",
        key="text_area_input"
    )
    
    # Botones para texto a morse
    col1_1, col1_2, col1_3 = st.columns([1, 1, 1])
    
    with col1_1:
        if st.button("🔄 Traducir", key="translate_text"):
            st.session_state.text_input = text_input
    
    with col1_2:
        if st.button("🗑️ Borrar", key="clear_text"):
            st.session_state.text_input = ""
            st.rerun()
    
    with col1_3:
        if st.button("📋 Copiar", key="copy_morse"):
            if text_input:
                st.success("¡Código Morse copiado! (simulado)")
    
    # Mostrar resultado
    if text_input or st.session_state.text_input:
        morse_output = text_to_morse(text_input if text_input else st.session_state.text_input)
        st.text_area(
            "Código Morse:",
            value=morse_output,
            height=150,
            key="morse_output",
            disabled=True
        )

with col2:
    st.header("📡 Morse a Texto")
    
    # Usar session state para el morse
    if 'morse_input' not in st.session_state:
        st.session_state.morse_input = ""
    
    morse_input = st.text_area(
        "Introduce código Morse aquí:",
        value=st.session_state.morse_input,
        height=150,
        placeholder="Ejemplo: .... --- .-.. .-",
        key="morse_area_input"
    )
    
    # Botones para morse a texto
    col2_1, col2_2, col2_3 = st.columns([1, 1, 1])
    
    with col2_1:
        if st.button("🔄 Traducir", key="translate_morse"):
            st.session_state.morse_input = morse_input
    
    with col2_2:
        if st.button("🗑️ Borrar", key="clear_morse"):
            st.session_state.morse_input = ""
            st.rerun()
    
    with col2_3:
        if st.button("📋 Copiar", key="copy_text"):
            if morse_input and validate_morse(morse_input):
                st.success("¡Texto copiado! (simulado)")
    
    # Mostrar resultado
    if morse_input or st.session_state.morse_input:
        current_morse = morse_input if morse_input else st.session_state.morse_input
        if validate_morse(current_morse):
            text_output = morse_to_text(current_morse)
            st.text_area(
                "Texto traducido:",
                value=text_output,
                height=150,
                key="text_output",
                disabled=True
            )
        else:
            st.error("⚠️ Formato de Morse inválido. Usa solo puntos (.), rayas (-), espacios y barras (/)")

# Footer
st.markdown("---")
st.markdown("*Creado para el portfolio de desarrollo* 🚀")
st.markdown("**Próximo paso:** Integración con reconocimiento de audio en tiempo real")