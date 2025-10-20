import webbrowser

print("""
Ne yapaay zeka :D
""")

while True:
    soru = input("Sen :").lower()

    if "Merhaba" or "selam" or "naber" in soru:
        print("Bot : Selam nasılsın")
    elif "nasılsın" in soru:
        print("Bot : Ben bir yapay zekayım duygularım yok sen nasılsın")
    elif "adın ne" in soru:
        print("Bot : Benim adım yok, ben Barış'a ait bir yapay zekayım senin adın ne")
    elif "Cemre" in soru:
        print("Bot : hmm Barış senden bahsetti sana çok aşık ve çok güzel olduğundan bahsetti")
    elif "Metehan" in soru:
        print("Bot : hmm.. barış senden bahsetmişti travmalarını anlatmak ister misin? İstersen sana şarkı açabilirim")
        webbrowser.open("https://www.youtube.com/watch?v=LU5FrAKJmYQ&list=RDLU5FrAKJmYQ&start_radio=1")
    elif "Batu" in soru :
        print("Bot : hmm.. Tahminimce sen Fenerbahçelisin en büyük FENER💛💙")
    elif "Süperlig puan durumu" in soru:
        print("Bot : Linke tıklayarak gidebilirsin..")
        webbrowser.open("https://www.tff.org/default.aspx?pageID=198")
    elif "hava durumu" in soru:
        print("Bot : Linke tıklayarak gidebilirsin..(ama sadece İzmir için yönlendirebiliyorum şimdilik :))")
        webbrowser.open("https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Izmir")
    elif "görüşürüz" in soru or "çık" in soru:
        print("Bot: Görüşürüz! Kendine iyi bak 👋")
        break
    else:
        print("Bot : üzgünüm seni anlayamadım henüz bunları yapamıyorum lütfen daha sonra dene gelişim aşamasındayım.")