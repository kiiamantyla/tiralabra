# Käyttöohje

## Asennus ja käynnistys
Kun olen kloonannut repositorion omalle koneellesi, käynnistä poetry projektin juurihakemistossa komennolla

```bash
poetry shell
```

Tämä vaatii, että koneella on asennettuna poetry. Tämän jälkeen luo virtuaaliympäristö ja lataa projektin riippuvuudet komennolla

```bash
poetry install
```

Sovelluksen voi nyt käynnistää komennolla

```bash
poetry run invoke start
```

Sovelluksen käyttöliittymä aukeaa terminaalin antamaan osoitteeseen, josta klikkaamalla aukeaa aloitusnäkymä. Lokaalista pyörivän sovelluksen voi sulkea terminaalista näppäilemällä Ctrl+C.

## Testit
Jos haluat ajaa sovellukselle yksikkötestejä, sen voi tehdä komennolla

```bash
poetry run invoke test
```

Testikattavuusraportin voi muodostaa komennolla

```bash
poetry run invoke coverage
```
