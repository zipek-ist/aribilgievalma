import streamlit as st


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.mgc.com.tr/wp-content/uploads/2022/06/gayrimenkul-yatirim-fonu-kurmanin-avantajlari-nelerdir-tr-mgc-legal.jpeg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()



st.markdown(f'<h1 style="color:red;font-size:48px;">{"KOMŞU ALMA EV AL PROJESİ"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:black;font-size:22px;">{"Bu hesaplama aracı enflasyonist olmayan bir dünya düzeninde, ev harici hiçbirşeye para harcamazsanız belirttiğiniz dönem sonunda elinizde avucunuzda ne olacak göstermek için tasarlanmıştır."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:black;font-size:22px;">{"Aşağıdaki formda istediğiniz gibi oynayıp fantazi dünyanızı genişletebilirsiniz."}</h1>', unsafe_allow_html=True)

col1,col2,col3,col4,col5=st.columns(5)
with col1:
    evfiyat=st.number_input("Almak istediğiniz evin fiyatı ne?")
with col2:
    pesinatyuzdesi=st.number_input("Gereken peşinat yüzdesi nedir?")
with col3:
    mevcutpesinat=st.number_input("Elinizde peşinat var mı?")
with col4:
    aylikbirikim=st.number_input("Her ay ne kadar biriktiyorsunuz?")
with col5:
    evkira=st.number_input("Evin kira getirisi nedir?")

col1,col2=st.columns(2)
with col1:
    mevcutyas=st.number_input("Maceranın başladığı yaş nedir?")
with col2:
    emeklilik=st.number_input("Bu eziyet kaç yaşında bitecek?")


period=(emeklilik-mevcutyas)*12
gerekenpesinat=(evfiyat*pesinatyuzdesi)/100
evsayisi=0
kreditaksit=(evfiyat-gerekenpesinat)/180



i=0
while i<period:
    mevcutpesinat+=aylikbirikim
    if mevcutpesinat>=gerekenpesinat:
        evsayisi += 1
        mevcutpesinat-=gerekenpesinat
        aylikbirikim += evkira-kreditaksit
    i += 1
st.subheader(f"Belirttiğiniz dönem sonunda {evsayisi} adet eviniz olacak ve her ay {evsayisi*evkira} gelir elde edeceksiniz...")




