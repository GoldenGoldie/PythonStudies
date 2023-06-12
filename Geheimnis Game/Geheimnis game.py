
geheimnis = 1337
versuch = 0
zaehler = 0

while versuch != geheimnis:
    versuch = int(input("Raten Sie: "))

    if versuch < geheimnis:
        print("Zu klein")

    if versuch > geheimnis:
        print("zu groß")

    zaehler=zaehler + 1

    if versuch == geheimnis:
        print("super, du hast es in",zaehler,"Versuchen geschafft gut Arbeit")