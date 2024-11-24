import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from Bio.Seq import Seq
from Bio.SeqUtils import molecular_weight
from collections import Counter

st.title("Diferencia proteica entre dos genes")

# Diccionario de codones de ARN a aminoácidos
codon_to_amino_acid = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L',
    'CUA': 'L', 'CUG': 'L', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'UCU': 'S', 'UCC': 'S',
    'UCA': 'S', 'UCG': 'S', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A',
    'GCA': 'A', 'GCG': 'A', 'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W', 'CGU': 'R', 'CGC': 'R',
    'CGA': 'R', 'CGG': 'R', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

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

# Interfaz de usuario en Streamlit
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
            
            # Mostrar el peso molecular de las proteínas
            peso_molecular_1 = molecular_weight(proteina1)
            peso_molecular_2 = molecular_weight(proteina2)
            st.write(f'Peso molecular de la Proteína 1: {peso_molecular_1} Da')
            st.write(f'Peso molecular de la Proteína 2: {peso_molecular_2} Da')

        else:
            st.error("Hubo un error al traducir las secuencias de ADN.")
    else:
        st.warning("Por favor, ingresa ambas secuencias de ADN.")
