import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder

# membaca model
model_heart = pickle.load(open('heartFailure-randomForest.sav','rb'))

# judul
st.title("Prediksi Gagal Jantung")

Age = st.text_input('Berapa usia Anda?')
Sex_pilihan = ['Laki - Laki', 'Perempuan']
Sex = st.selectbox('Jenis kelamin Anda', Sex_pilihan)
if Sex == 'Laki - Laki':
    Sex = 'M'
elif Sex == 'Perempuan' :
    Sex = 'F'


Chest_pilihan = ['Angina Khas', 'Angina Atipikal', 'Nyeri Non-Anginal', 'Asimtomatik']
ChestPainType = st.selectbox("Apa jenis sakit dada yang Anda alami?", Chest_pilihan)
if ChestPainType == 'Angina Khas':
    ChestPainType = 'TA'
elif ChestPainType == 'Angina Atipikal':
    ChestPainType = "ATA"
elif ChestPainType == 'Nyeri Non-Anginal':
    ChestPainType = 'NAP'
elif ChestPainType == 'Asimtomatik':
    ChestPainType = 'ASY'

RestingBP = st.text_input('Berapa tekanan darah Anda?')
Cholesterol = st.text_input('Berapa kolesterol Anda?')
FastingBS_pilihan = ['Ya', 'Tidak']
FastingBS = st.selectbox('Apakah gula darah Anda setelah puasa di atas 120 mg/dl?', FastingBS_pilihan)
if FastingBS == 'Ya':
    FastingBS = 1
else:
    FastingBS = 0
MaxHR = st.text_input('Berapa denyut jantung maksimal? (Input angka 60 - 202 detik)')

# with col3 :
    

# encode
input_data = (Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,MaxHR)
arr1 = np.array(input_data)
arr1 = arr1.reshape(1,-1)

# Indeks-indeks yang ingin dilakukan encoding
indeks_encode = [1, 2]

# Melakukan encoding pada indeks-indeks yang dipilih
for indeks in indeks_encode:
    label_encoder = LabelEncoder()
    arr1[:, indeks] = label_encoder.fit_transform(arr1[:, indeks])

# prediksi
diagnosis = ''

# tombol prediksi
if st.button('Mulai Tes'):
    HeartDisease_prediksi = model_heart.predict(arr1)

    if(HeartDisease_prediksi == 1):
        diagnosis = 'Anda terindikasi gagal jantung, segera periksa ke fasilitas kesehatan terdekat'
        st.error(diagnosis)

    elif(HeartDisease_prediksi == 0):
        diagnosis = 'Anda tidak terindikasi gagal jantung'
        st.success(diagnosis)

    

