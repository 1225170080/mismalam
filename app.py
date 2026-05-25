import streamlit as st

st.set_page_config(page_title="Aplikasi Pertamaku", page_icon="+")

st.title("Aplikasi streamlite pertamaku!")
st.write("Halo dunia! Jika kamu bisa melihat halaman ini, berarti kamu sudah **BERHASIL** meng-upload dan mendeploy aplikasi streamlit dari Github.")

st.divider()

nama= st.text_input("Siapa namamu?")

if st.button("Klik saya!"):
    if nama:
        st.success(f"Hallo,{nama}! Selamat belajar streamlit. Kamu hebat!")
        st.ballons()
    else:
        st.warning("Isi namamu dulu dikotak atas ya!")
        