
import pandas as pd
import gradio as gr

# Load dataset ICD
icd10 = pd.read_csv("icd10_2010.csv")
icd9 = pd.read_csv("icd9_2010.csv")

def cari_kode_icd(pertanyaan):
    hasil_icd10 = icd10[icd10['Nama Penyakit'].str.contains(pertanyaan, case=False, na=False)]
    hasil_icd9 = icd9[icd9['Nama Penyakit'].str.contains(pertanyaan, case=False, na=False)]

    if not hasil_icd10.empty:
        return "📘 ICD-10:\n" + hasil_icd10[['Kode', 'Nama Penyakit']].to_string(index=False)
    elif not hasil_icd9.empty:
        return "📗 ICD-9:\n" + hasil_icd9[['Kode', 'Nama Penyakit']].to_string(index=False)
    else:
        return "❌ Maaf, kode penyakit tidak ditemukan dalam database ICD 2010."

gr.Interface(fn=cari_kode_icd,
             inputs="text",
             outputs="text",
             title="Chat ICD AI",
             description="Tanyakan kode diagnosa dari ICD-10 2010 dan ICD-9 2010. Contoh: 'cacar', 'tifoid', 'kolera'"
).launch()
