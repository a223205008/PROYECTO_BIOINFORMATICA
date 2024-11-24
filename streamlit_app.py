import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
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

def dna_to_rna(dna_sequence):
    """Convierte una secuencia de ADN a ARN reemplazando la T por U."""
    return dna_sequence.replace('T', 'U')

def rna_to_protein(rna_sequence):
    """Convierte una secuencia de ARN a proteína (secuencia de aminoácidos)."""
    protein = []
    for i in range(0, len(rna_sequence), 3):  # Leer de 3 en 3 nucleótidos (codones)
        codon = rna_sequence[i:i+3]
        if len(codon) == 3:
            amino_acid = codon_to_amino_acid.get(codon, 'X')  # X para codón desconocido
            if amino_acid == '*':
                break  # Parada de la traducción
            protein.append(amino_acid)
    return ''.join(protein)

# Interfaz de usuario en Streamlit
st.title('Análisis de Secuencia de ADN')

# Entrada del usuario: secuencia de ADN
dna_input = st.text_area('Introduce la primera secuencia de ADN:', '')
dna_input = st.text_area('Introduce la segunda secuencia de ADN:', '')

# Botón para procesar
if st.button('Analizar'):
    if dna_input:
        # Validar secuencia de ADN
        if all(base in 'ATGC' for base in dna_input):
            rna_sequence = dna_to_rna(dna_input)
            protein_sequence = rna_to_protein(rna_sequence)
            
            # Mostrar los resultados
            st.write('Secuencia de ARN: ', rna_sequence)
            st.write('Secuencia de proteína (aminoácidos): ', protein_sequence)
            
            # Contar las proteínas (aminoácidos)
            protein_count = {aa: protein_sequence.count(aa) for aa in set(protein_sequence)}
            st.write('Cantidad de cada tipo de proteína (aminoácido):', protein_count)
        else:
            st.error('La secuencia de ADN contiene caracteres no válidos. Debe contener solo A, T, G, C.')
