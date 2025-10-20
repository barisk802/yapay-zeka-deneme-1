import streamlit as st

st.title("💬 Ne yapaay zeka :D")

# Sohbet geçmişini tut
if "sohbet" not in st.session_state:
    st.session_state.sohbet = []

# Kullanıcıdan mesaj al
soru = st.text_input("Sen :")

# Eğer kullanıcı mesaj yazdıysa
if soru:
    cevap = ""

    if "merhaba" in soru.lower() or "selam" in soru.lower() or "naber" in soru.lower():
        cevap = "Selam nasılsın?"
    elif "nasılsın" in soru.lower():
        cevap = "Ben bir yapay zekayım, duygularım yok. Sen nasılsın?"
    elif "adın ne" in soru.lower():
        cevap = "Benim adım yok, Barış’a ait bir yapay zekayım. Senin adın ne?"
    elif "cemre" in soru.lower():
        cevap = "Hmm... Barış senden bahsetti. Sana çok aşık ve çok güzel olduğundan bahsetti 💕"
    elif "metehan" in soru.lower():
        cevap = "Hmm... Barış senden bahsetmişti. Travmalarını anlatmak ister misin? 😅"
    elif "batu" in soru.lower():
        cevap = "Tahminimce sen Fenerbahçelisin 💛💙 En büyük FENER!"
    elif "süperlig puan durumu" in soru.lower():
        cevap = "[🏆 Süper Lig Puan Durumu](https://www.tff.org/default.aspx?pageID=198)"
    elif "hava durumu" in soru.lower():
        cevap = "[☀️ İzmir Hava Durumu](https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Izmir)"
    elif "görüşürüz" in soru.lower() or "çık" in soru.lower():
        cevap = "Görüşürüz! Kendine iyi bak 👋"
    else:
        cevap = "Üzgünüm, seni anlayamadım. Henüz bunları yapamıyorum 😅"

    # Sohbete hem kullanıcı hem bot mesajını ekle
    st.session_state.sohbet.append(("Sen", soru))
    st.session_state.sohbet.append(("Bot", cevap))

    # Input’u temizlemek için sayfayı yenile
    st.experimental_rerun()

# Sohbet geçmişini göster
for kim, mesaj in st.session_state.sohbet:
    if kim == "Sen":
        st.markdown(f"🧍‍♂️ **{kim}:** {mesaj}")
    else:
        st.markdown(f"🤖 **{kim}:** {mesaj}")

