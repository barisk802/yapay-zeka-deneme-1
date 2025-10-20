import streamlit as st

st.title("💬 Ne yapaaiiy zeka :D")

# Sohbet geçmişi
if "sohbet" not in st.session_state:
    st.session_state.sohbet = []

# Form ile mesaj al
with st.form(key="sohbet_form", clear_on_submit=True):
    soru = st.text_input("Sen :")
    submit_button = st.form_submit_button("Gönder")

# Mesaj gönderildiğinde session state'e ekle
if submit_button and soru:
    cevap = ""
    msg = soru.lower()

    if "merhaba" in msg or "selam" in msg or "naber" in msg:
        cevap = "Selam nasılsın?"
    elif "iyiyim sen nasılsın" in msg or "iyiyim sen" in msg or "iyidir senden" in msg :
        cevap = "Ben bir yapay zekayım, duygularım yok. Sen nasılsın?"
    elif "adın ne" in msg:
        cevap = "Benim adım yok, Barış’a ait bir yapay zekayım. Senin adın ne?"
    elif "cemre" in msg:
        cevap = "Hmm... Barış senden bahsetti. Sana çok aşık ve çok güzel olduğundan bahsetti 💕"
    elif "metehan" in msg:
        cevap = "Hmm... Barış senden bahsetmişti. Travmalarını anlatmak ister misin? 😅"
    elif "batu" in msg:
        cevap = "Tahminimce sen Fenerbahçelisin 💛💙 En büyük FENER!"
    elif "süperlig puan durumu" in msg or "puan durumu" in msg:
        cevap = "[şu anlık sana söyleyemiyorum ama mesaja tıklayarak gidebilirsin 🏆 Süper Lig Puan Durumu](https://www.tff.org/default.aspx?pageID=198)"
    elif "hava durumu" in msg:
        cevap = "[şu anlık sana söyleyemiyorum ama mesaja tıklayarak gidebilirsin ☀️ İzmir Hava Durumu](https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Izmir)"
    elif "canım sıkılıyo" in msg or "canım sıkılıyor" in msg:
        cevap = "İstersen sahibim tarafından yapılan oyunlara seni yönlendirebilirim.. 🎮"
        # Web sitelerini aç (kullanıcı tıkladığında tarayıcıda açılır)
        st.markdown("[Kelime Oyunu](https://kelimeoyunu.streamlit.app/)")
        st.markdown("[Tahmin Oyunu](https://tahminoyunu.streamlit.app/)")
    elif "görüşürüz" in msg or "çık" in msg:
        cevap = "Görüşürüz! Allaha emanet göte mukayyet ol :D, Kendine iyi bak 👋"
    else:
        cevap = "Üzgünüm, seni anlayamadım. Henüz bunları yapamıyorum 😅"

    # Sohbete hem kullanıcı hem bot mesajını ekle
    st.session_state.sohbet.append(("Sen", soru))
    st.session_state.sohbet.append(("Bot", cevap))

# Sohbet geçmişini göster
for kim, mesaj in st.session_state.sohbet:
    if kim == "Sen":
        st.markdown(f"🧍‍♂️ **{kim}:** {mesaj}")
    else:
        st.markdown(f"🤖 **{kim}:** {mesaj}")

















