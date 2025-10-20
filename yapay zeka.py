import streamlit as st
import webbrowser

st.title("🤖 Ne yapaaiiy zeka :D")

# Kullanıcı girişi alanı
soru = st.text_input("Sen :").lower()

if soru:
    if "merhaba" in soru or "selam" in soru or "naber" in soru:
        st.write("**Bot :** Selam nasılsın")
    elif "nasılsın" in soru:
        st.write("**Bot :** Ben bir yapay zekayım, duygularım yok. Sen nasılsın?")
    elif "adın ne" in soru:
        st.write("**Bot :** Benim adım yok, ben Barış’a ait bir yapay zekayım. Senin adın ne?")
    elif "cemre" in soru:
        st.write("**Bot :** Hmm... Barış senden bahsetti. Sana çok aşık ve çok güzel olduğundan bahsetti 💕")
    elif "metehan" in soru:
        st.write("**Bot :** Hmm... Barış senden bahsetmişti, travmalarını anlatmak ister misin? İstersen sana şarkı açabilirim 🎵")
        st.link_button("🎶 Şarkıyı Aç", "https://www.youtube.com/watch?v=LU5FrAKJmYQ&list=RDLU5FrAKJmYQ&start_radio=1")
    elif "batu" in soru:
        st.write("**Bot :** Hmm... Tahminimce sen Fenerbahçelisin 💛💙 En büyük FENER!")
    elif "ayberk" in soru:
        st.write("**Bot :** Selam Ayberk tanıştığıma memnun oldum götoş")
    elif "süperlig puan durumu" in soru:
        st.write("**Bot :** Linke tıklayarak gidebilirsin ⚽️")
        st.link_button("🏆 Süper Lig Puan Durumu", "https://www.tff.org/default.aspx?pageID=198")
    elif "hava durumu" in soru:
        st.write("**Bot :** Linke tıklayarak gidebilirsin 🌦️ (şimdilik sadece İzmir için 😅)")
        st.link_button("☀️ İzmir Hava Durumu", "https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Izmir")
    elif "görüşürüz" in soru or "çık" in soru:
        st.write("**Bot :** Görüşürüz! Kendine iyi bak 👋")
    else:
        st.write("**Bot :** Üzgünüm, seni anlayamadım. Henüz bunları yapamıyorum. Gelişim aşamasındayım 😅")

