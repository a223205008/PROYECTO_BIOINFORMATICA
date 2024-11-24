import streamlit as st
from Bio.Seq import Seq
from collections import Counter

# Diccionario de codones a aminoácidos
codones_a_aminoacidos = {
    'ATA': 'Ile', 'ATC': 'Ile', 'ATT': 'Ile', 'ATG': 'Met', 
    'ACA': 'Thr', 'ACC': 'Thr', 'ACG': 'Thr', 'ACT': 'Thr', 
    'AAC': 'Asn', 'AAT': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys', 
    'AGC': 'Ser', 'AGT': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg', 
    'CTA': 'Leu', 'CTC': 'Leu', 'CTG': 'Leu', 'CTT': 'Leu', 
    'CCA': 'Pro', 'CCC': 'Pro', 'CCG': 'Pro', 'CCT': 'Pro', 
    'CAC': 'His', 'CAT': 'His', 'CAA': 'Gln', 'CAG': 'Gln', 
    'CGA': 'Arg', 'CGC': 'Arg', 'CGG': 'Arg', 'CGT': 'Arg', 
    'GTA': 'Val', 'GTC': 'Val', 'GTG': 'Val', 'GTT': 'Val', 
    'GCA': 'Ala', 'GCC': 'Ala', 'GCG': 'Ala', 'GCT': 'Ala', 
    'GAC': 'Asp', 'GAT': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu', 
    'GGA': 'Gly', 'GGC': 'Gly', 'GGG': 'Gly', 'GGT': 'Gly', 
    'TCA': 'Ser', 'TCC': 'Ser', 'TCG': 'Ser', 'TCT': 'Ser', 
    'TTC': 'Phe', 'TTT': 'Phe', 'TTA': 'Leu', 'TTG': 'Leu', 
    'TAC': 'Tyr', 'TAT': 'Tyr', 'TAA': 'Stop', 'TAG': 'Stop', 
    'TGC': 'Cys', 'TGT': 'Cys', 'TGA': 'Stop', 'TGG': 'Trp', 
    'CTA': 'Leu', 'CTC': 'Leu', 'CTG': 'Leu', 'CTT': 'Leu'
}

# Función para traducir una secuencia de ADN a una proteína
def traducir_a_proteina(seq):
    # Asegúrate de que la secuencia sea válida
    seq = seq.upper()  # Convertir a mayúsculas
    # Crear un objeto Seq de Biopython y traducir
    secuencia_obj = Seq(seq)
    proteina = secuencia_obj.translate(to_stop=True)
    return str(proteina)

# Función para contar aminoácidos en la proteína
def contar_aminoacidos(proteina):
    return dict(Counter(proteina))

# Crear la interfaz con Streamlit
st.title('Comparador de Secuencias de ADN y Análisis de Proteínas')

# Descripción de la app
st.write("Introduce dos secuencias de ADN para compararlas")

# Áreas de texto para ingresar las secuencias
seq1 = st.text_area('Introduce la primera secuencia de ADN', height=200)
seq2 = st.text_area('Introduce la segunda secuencia de ADN', height=200)

# Botón para realizar la comparación
if st.button('Comparar Secuencias'):
    if seq1 and seq2:
        proteina1 = traducir_a_proteina(seq1)
        proteina2 = traducir_a_proteina(seq2)

        # Mostrar las proteínas traducidas
        st.write(f'Proteína 1: {proteina1}')
        st.write(f'Proteína 2: {proteina2}')
        
        # Comparación simple de proteínas
        if proteina1 == proteina2:
            st.write("Las proteínas son idénticas.")
        else:
            st.write("Las proteínas son diferentes.")

        # Contar los aminoácidos en ambas proteínas
        aminoacidos_contados_1 = contar_aminoacidos(proteina1)
        aminoacidos_contados_2 = contar_aminoacidos(proteina2)

        # Mostrar los contadores de aminoácidos
        st.write("Conteo de aminoácidos en Proteína 1:")
        st.write(aminoacidos_contados_1)
        st.write("Conteo de aminoácidos en Proteína 2:")
        st.write(aminoacidos_contados_2)

