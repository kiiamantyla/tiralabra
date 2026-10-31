# Määrittelydokumentti
Tämä dokumentti määrittelee Helsingin yliopiston Aineopintojen harjoitustyö: Algoritmit ja tekoäly - kurssilla tehtävän harjoitustyön. Suoritan kurssin Tietojenkäsittelytieteen kandiohjelmassa (TKT).

# Ohjelmointikieli ja projektin kieli
Harjoitustyö toteutetaan Pythonilla.
Vertaisarvioinnissa arvostelen mieluusti pythonilla toteutettuja töitä.
Projektin dokumentaatio kirjoitetaan suomeksi. Itse koodi ja muuttujien nimet ovat englanniksi, mutta koodissa olevat kommentit suomeksi.

# Aihe ja toteutus
Toteutan harjoitustyössä 2048-peliin tekoälyn, joka osaa pelata peliä itsenäisesti ja tehdä optimaalisia siirtoja. Hyödynnän tämän tekemiseen expectiminimax-algoritmia ja heuristista arviointifunktiota.
Tekoäly saa syötteekseen nykyisen pelilaudan tilan (4x4 matriisi), jonka perusteella se muodostaa pelipuun ja laskee parhaan siirron, jonka se palauttaa.
Expectiminimax-algoritmi vie lähteiden mukaan o(b^d), jossa b on haarautumistekijä ja d hakupuun syvyys.


# Lähteet
Harjoitustyössä käytän seuraavia lähteitä:
- [Expectiminimax (Wikipedia)](https://en.wikipedia.org/wiki/Expectiminimax)
- [Minimax (Wikipedia)](https://en.wikipedia.org/wiki/Minimax)
- [Alpha-beta pruning (Wikipedia)](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
- [Yun Nie, Wneqi Hou ja Yichen An artikkeli](https://cs229.stanford.edu/proj2016/report/NieHouAn-AIPlays2048-report.pdf)
