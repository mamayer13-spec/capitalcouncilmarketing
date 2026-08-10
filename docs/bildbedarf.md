# Welche Bilder gebraucht werden

Stand: 2026-08-10

## Regeln für alle Bilder

**Quelle:** [Unsplash](https://unsplash.com) oder [Pexels](https://pexels.com). Beide
Lizenzen erlauben die kommerzielle Nutzung ohne Namensnennung. Keine Bilder aus der
Google-Bildersuche — die sind fast immer urheberrechtlich geschützt.

**Ablage:** in `assets/img/`, exakt unter dem unten genannten Dateinamen.

**Format:** JPG. Mindestbreite wie angegeben. Danach verkleinern:

    sips -Z 2000 assets/img/DATEINAME.jpg --out assets/img/DATEINAME.jpg

Ziel sind unter 400 KB je Datei.

**Was nicht geht:**

- Händeschütteln, Daumen hoch, Erfolgsposen
- Konferenzräume, in denen jemand auf ein Diagramm zeigt
- Fremde Markenlogos im Bild, erkennbare LinkedIn-Oberflächen
- Strand, Pool, Luxusautos, Villen — die Seite grenzt sich im Text ausdrücklich davon ab
- Offensichtliche Katalogware: künstliches Lächeln, unnatürliche Gruppenaufstellungen

**Worauf es ankommt:** ruhige, konkrete Situationen bei Tageslicht. Lieber ein Bild, das
banal wirkt, aber echt — als eines, das inszeniert aussieht. Alle Bilder bekommen über
die Seite denselben leichten Blaustich, damit sie wie eine Serie wirken. Du musst also
nicht auf einheitliche Farbstimmung achten, nur auf einheitliche Helligkeit: durchgehend
hell, keine dunklen Aufnahmen.

---

## 1. Kontakt — wird gebraucht

| | |
|---|---|
| Dateiname | `gespraech.jpg` |
| Seitenverhältnis | 4:3 quer |
| Mindestbreite | 1600 px |
| Platz auf der Seite | Kontaktabschnitt, rechte Spalte neben „Erstgespräch vereinbaren" |

**Motiv:** Zwei Personen im Gespräch an einem Tisch. Kein Verkaufsgespräch, eher ein
ruhiges Arbeitsgespräch zu zweit. Laptop oder Notizblock dürfen vorkommen.

**Suchbegriffe:** `two people meeting table daylight`, `business conversation desk`,
`consultation two people`

**Warum diese Stelle:** Es ist die einzige Bildfläche, die aktuell leer ist. Sie zeigt
derzeit einen blauen Farbverlauf — das sieht bewusst gestaltet aus und ist kein Notstand,
aber ein echtes Bild direkt neben dem Buchungsknopf wirkt einladender.

---

## 2. Methode — empfohlen

| | |
|---|---|
| Dateiname | `arbeit.jpg` |
| Seitenverhältnis | 16:7 quer, sehr breit |
| Mindestbreite | 2000 px |
| Platz auf der Seite | Methodenabschnitt, als breites Band unter den fünf Phasen |

**Motiv:** Eine Person konzentriert am Laptop bei Tageslicht. Von der Seite oder über die
Schulter, nicht frontal in die Kamera. Der Bildschirm darf unscharf sein.

**Suchbegriffe:** `person laptop focused daylight`, `working desk window light`,
`writing laptop side view`

**Warum diese Stelle:** Der Methodenabschnitt ist der längste der Seite — fünf Karten
plus Werkzeugraster. Ein breites Bild dazwischen gibt dem Auge eine Pause. Ich baue die
Fläche erst ein, wenn das Bild da ist.

---

## 3. Hero — optional

| | |
|---|---|
| Dateiname | `hero.jpg` |
| Seitenverhältnis | 3:2 quer |
| Mindestbreite | 2400 px |
| Platz auf der Seite | Startbereich, rechts neben der Überschrift |

**Motiv:** Ruhiger Arbeitsplatz bei Tageslicht, keine Person im Fokus. Oder klare, helle
Architektur: Glasfassade, Treppenhaus, Bürogebäude von außen.

**Suchbegriffe:** `office daylight desk minimal`, `modern architecture glass daylight`,
`quiet workspace morning`

**Warum optional:** Dort sitzt derzeit der pulsierende Punkt-Ring. Der funktioniert gut
und ist eigenständiger als ein Stockfoto. Ein Bild würde den Ring ersetzen, nicht
ergänzen — beides nebeneinander wird zu unruhig. Nur nehmen, wenn dir ein Foto dort
lieber ist als das Zeichen.

---

## 4. Porträt — später ersetzen

Aktuell liegt `claudio.png` im Über-uns-Abschnitt, das Strandbild aus dem
`capital-architecture`-Repo. Es ist eingebaut, weil du es so wolltest.

Zwei Punkte, die dagegen sprechen und die du bei Gelegenheit abwägen solltest:

1. Direkt daneben steht der Satz „Keine Erfolgsversprechen, **keine gemieteten Kulissen**."
   Bild und Aussage widersprechen sich für jeden, der beides gleichzeitig sieht.
2. Palme und Strand sind im Coaching-Umfeld das Erkennungszeichen, an dem Zahlungsanbieter
   und Banken genauer hinsehen. Die Seite wird der Bank vorgelegt.

**Was besser wäre:** ein sachliches Porträt — Oberkörper, ruhiger Hintergrund, normale
Arbeitskleidung, Tageslicht. Mit dem Handy in zehn Minuten gemacht. Dateiname bleibt
`claudio.png` oder wird `claudio.jpg`, dann sage mir Bescheid.

Ein Stockfoto kommt hier **nicht** infrage: ein fremdes Gesicht unter einem echten Namen
wäre eine Falschdarstellung.

---

## Zusammengefasst

| Priorität | Datei | Verhältnis | Mindestbreite |
|---|---|---|---|
| **wird gebraucht** | `gespraech.jpg` | 4:3 | 1600 px |
| empfohlen | `arbeit.jpg` | 16:7 | 2000 px |
| optional | `hero.jpg` | 3:2 | 2400 px |
| bei Gelegenheit | echtes Porträt statt `claudio.png` | 4:5 | 1200 px |

Leg die Dateien einfach in `assets/img/` ab und sag Bescheid — ich binde sie ein,
verkleinere sie und prüfe, wie sie mit dem Blaustich zusammenwirken.
