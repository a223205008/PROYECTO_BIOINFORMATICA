import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Configuración de los estilos de gráficos
sns.set(style="whitegrid")

def traducir_adn(entrada_adn):
    """
    Función para traducir una secuencia de ADN a una secuencia de proteína.
    Utiliza el marco de lectura estándar (sin considerar mutaciones o marcos alternativos).
    """
    secuencia_adn = Seq(entrada_adn)
    try:
        # Traducción de la secuencia ADN a proteína
        secuencia_proteina = secuencia_adn.translate()
        return secuencia_proteina
    except:
        return None

def contar_aminoacidos(proteina):
    """
    Función para contar los aminoácidos presentes en la secuencia de proteína.
    """
    contador = Counter(proteina)
    return contador

def graficar_aminoacidos(aminoacidos_contados, secuencia_num):
    """
    Función para graficar la distribución de los aminoácidos en una proteína.
    """
    aminoacidos = list(aminoacidos_contados.keys())
    cantidades = list(aminoacidos_contados.values())
    
    plt.figure(figsize=(8, 5))
    plt.bar(aminoacidos, cantidades, color='skyblue')
    plt.title(f"Distribución de Aminoácidos en la Proteína {secuencia_num}")
    plt.xlabel("Aminoácidos")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    st.pyplot(plt)

def graficar_nucleotidos(seq1, seq2):
    """
    Función para graficar la cantidad de nucleótidos de cada secuencia de ADN.
    """
    nucleotidos_seq1 = len(seq1)
    nucleotidos_seq2 = len(seq2)
    
    # Crear el gráfico de barras
    plt.figure(figsize=(6, 4))
    plt.bar(['Secuencia 1', 'Secuencia 2'], [nucleotidos_seq1, nucleotidos_seq2], color='lightgreen')
    plt.title("Cantidad de Nucleótidos por Secuencia de ADN")
    plt.ylabel("Cantidad de Nucleótidos")
    st.pyplot(plt)

def comparar_proteinas(proteina1, proteina2):
    """
    Función para comparar dos secuencias de proteínas.
    Retorna la cantidad de proteínas que coinciden y los cambios.
    """
    coincidencias = 0
    for p1, p2 in zip(proteina1, proteina2):
        if p1 == p2:
            coincidencias += 1
    diferencias = len(proteina1) - coincidencias
    return coincidencias, diferencias

# Título de la app
st.title('Comparador de Secuencias de ADN')

# Introducción de las secuencias de ADN
seq1 = st.text_area('Introduce la primera secuencia de ADN', height=200)
seq2 = st.text_area('Introduce la segunda secuencia de ADN', height=200)

# Botón para realizar la comparación
if st.button('Comparar Secuencias'):
    if seq1 and seq2:
        # Traducción de las secuencias de ADN a proteínas
        proteina1 = traducir_adn(seq1)
        proteina2 = traducir_adn(seq2)

        if proteina1 and proteina2:
            # Mostrar las proteínas traducidas
            st.write(f'Proteína 1: {proteina1}')
            st.write(f'Proteína 2: {proteina2}')

            # Comparación de las proteínas
            coincidencias, diferencias = comparar_proteinas(proteina1, proteina2)
            
            # Mostrar los resultados de la comparación
            st.write(f'Cantidad de aminoácidos coincidentes: {coincidencias}')
            st.write(f'Diferencias en la proteína: {diferencias}')
            

        else:
            st.error("Hubo un error al traducir las secuencias de ADN.")
    else:
        st.warning("Por favor, ingresa ambas secuencias de ADN.")
