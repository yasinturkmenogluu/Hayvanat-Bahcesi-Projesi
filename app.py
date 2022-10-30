import random
import math

c = 0 # hayvanlarin_uremesi fonksiyonunda yeni doğan erkek ve dişi hayvanlardan üreme olmaması için kullanılmaktadır.

# Başlangıçtaki hayvan sayısı
hayvan_sayisi = 78

# Hayvanların tanımlanması (cins, cinsiyet, konum [x,y])
# ke: erkek koyunlar, kd: dişi koyunlar, 123... : hayvan sırası
koyunlar = {"ID": {"ke1":[0,250], "ke2":[0,252], "ke3":[0,254], "ke4":[0,256], "ke5":[0,258], "ke6":[0,260], "ke7":[0,262], "ke8":[0,264], "ke9":[0,266], "ke10":[0,268], "ke11":[0,270], "ke12":[0,272], "ke13":[0,274], "ke14":[0,276], "ke15":[0,278],
                   "kd1":[0,251], "kd2":[0,253], "kd3":[0,255], "kd4":[0,257], "kd5":[0,259], "kd6":[0,261], "kd7":[0,263], "kd8":[0,265], "kd9":[0,267], "kd10":[0,269], "kd11":[0,271], "kd12":[0,273], "kd13":[0,275], "kd14":[0,277], "kd15":[0,279]}}

# ie: erkek inekler, id: dişi inekler
inekler = {"ID":{"ie1": [0,500], "ie2": [2,500], "ie3": [4,500], "ie4": [6,500], "ie5": [8,500],
                 "id1": [1,500], "id2": [3,500], "id3": [5,500], "id4": [7,500], "id5": [9,500]}}

# kue: erkek kurtlar, kud: dişi kurtlar
kurtlar = {"ID":{"kue1":[500,0],"kue2":[498,0],"kue3":[496,0], "kue4":[494,0], "kue5":[492,0],
           "kud1":[0,0],"kud2":[2,0],"kud3":[4,0], "kud4":[6,0], "kud5":[8,0]}}

# ae: erkek aslanlar, ad: dişi aslanlar
aslanlar = {"ID":{"ae1": [499,0], "ae2": [497,0], "ae3": [495,0], "ae4": [493,0],
                  "ad1": [1,0], "ad2": [3,0], "ad3": [5,0], "ad4": [7,0]}}

# h: horozlar, t: tavuklar
horozlar_ve_tavuklar = {"ID":{"h1":[500,250], "h2": [500,252], "h3": [500,254], "h4": [500,256], "h5": [500,258], "h6": [500,260], "h7": [500,262], "h8": [500,264], "h9": [500,266], "h10": [500,268],
                              "t1":[500,251], "t2": [500,253], "t3": [500,255], "t4": [500,257], "t5": [500,259], "t6": [500,261], "t7": [500,263], "t8": [500,265], "t9": [500,267], "t10": [500,269]}}
# avcı
avci = {"ID": {"av": [250,0]}}

# Canlılara Random olarak gönderilir.
# konumlar: [x,y] şeklindedir
# sağ: x ekseninde artış, sol: x ekseninde azalış, ileri: y ekseninde artış, geri: y ekseninde azalış,
yonler = ["ileri","geri","sag","sol"] # Random seçilecektir.


# ******************************************HAYVANLARIN ÖLMESİ**********************************************************

def canilarin_avlanmasi(avlayan, avlanan, birim):
    # avlayan: avcı, avlanan av, birim: bir adımdaki avlanma için tanımlanan birim
    global hayvan_sayisi

    for h1, h2 in zip(avlayan["ID"], avlayan["ID"].values()):
        for k1, k2 in zip(list(avlanan["ID"]), list(avlanan["ID"].values())):

            if (abs((h2[0] - k2[0]) ** 2 + (h2[1] - k2[1]) ** 2) <= birim):
                avlanan["ID"].pop(k1)

                # print("Bir koyun {} tarafından öldürüldü.".format(avlayan))
                hayvan_sayisi -= 1


def hayvanlarin_uremesi(hayvanlar, index, sd1, sd2, id1, id2):
    # hayvanlar: üreme yapacak tüm hayvanlar, index: cinslere göre ID tanımlarındaki cinsiyet belirten harfi (e veya d) elde etmek için kullanılır.
    # sd1, sd2: bir cinsin en sonundaki hayvanın ID'si (dişi, erkek)
    global hayvan_sayisi,c

    for e, ek in zip(list(hayvanlar["ID"]), list(hayvanlar["ID"].values())):
        for d, dk in zip(list(hayvanlar["ID"]), list(hayvanlar["ID"].values())):

            if ((e[index] == "e") & (d[index] == "d") or (e[index] == "d") & (d[index] == "e")):

                if (abs((ek[0] - dk[0]) ** 2 + (ek[1] - dk[1]) ** 2) <= 9):
                    #print("yeni bir kurt doğdu")
                    yeni_hayvan = random.choice([id1 + "{}".format(math.ceil(len(hayvanlar["ID"].values()) / 2 + 1)),
                                                 id2 + "{}".format(math.ceil(len(hayvanlar["ID"].values()) / 2 + 1))])

                    hayvanlar["ID"][yeni_hayvan] = [random.randint(0, 500), random.randint(0, 500)]
                    hayvan_sayisi += 1

            if (e == sd1) & (d == sd2):
                c = 1
                break
        if c == 1:
            c = 0
            break


# canlıların konumları güncellenmektedir.
def konum_guncelle(canlilar, adim):
    # canlılar: tüm canlılar, adim: hayvanların her bir adımda kat ettiği birim
    for ki, kk in zip(list(canlilar["ID"]), list(canlilar["ID"].values())):
        yon = random.choice(yonler)

        if (yon == "ileri") & ((kk[1] + adim) <= 500):
            canlilar["ID"][ki] = [kk[0], kk[1] + adim]

        elif (yon == "geri") & (kk[1] <= 500):
            canlilar["ID"][ki] = [kk[0], kk[1] - adim]

        elif (yon == "sag") & (kk[0] + adim):
            canlilar["ID"][ki] = [kk[0] + adim, kk[1]]
        # sol
        else:
            if kk[0] <= 500:
                canlilar["ID"][ki] = [kk[0] - adim, kk[1]]



count=0 # 1000 iterasyon (adım) için kullanılır.
while (count<1000):
    # Kurtlar
    canilarin_avlanmasi(kurtlar, koyunlar, 16)
    canilarin_avlanmasi(kurtlar, horozlar_ve_tavuklar, 16)

    # Aslanlar
    canilarin_avlanmasi(aslanlar, koyunlar, 25)
    canilarin_avlanmasi(aslanlar, inekler, 25)

    # Avcı
    canilarin_avlanmasi(avci, aslanlar, 64)
    canilarin_avlanmasi(avci, kurtlar, 64)
    canilarin_avlanmasi(avci, koyunlar, 64)
    canilarin_avlanmasi(avci, inekler, 64)
    canilarin_avlanmasi(avci, horozlar_ve_tavuklar, 64)

    #------------------------------------------HAYVANLARIN ÜREMESİ---------------------------------------------------------
    hayvanlarin_uremesi(aslanlar, 1, "ae4","ad4","ae","ad")
    hayvanlarin_uremesi(koyunlar, 1, "ke15","kd15","ke","kd")
    hayvanlarin_uremesi(inekler, 1, "ie5","id5","ie","id")
    hayvanlarin_uremesi(horozlar_ve_tavuklar, 0, "h10","t10","h","t")
    hayvanlarin_uremesi(kurtlar, 2, "kue5","kud5","kue","kud")

    #------------------------------------------KONUM GÜNCELLEME---------------------------------------------------------
    konum_guncelle(koyunlar, 2)
    konum_guncelle(kurtlar, 3)
    konum_guncelle(inekler, 2)
    konum_guncelle(horozlar_ve_tavuklar, 1)
    konum_guncelle(aslanlar, 4)
    konum_guncelle(avci, 1)

    count+=1

print("Kalan hayvan sayısı:", hayvan_sayisi)
