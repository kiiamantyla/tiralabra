# 2048-pelin tekoäly
Tämä on Helsingin yliopiston Algoritmit ja tekoäly -kurssilla tehtävä 2048-pelin tekoäly.

## Dokumentaatio
[Määrittelydokumentti](./docs/maarittelydokumentti.md)

[Testausraportti](./docs/testausraportti.md)

[Käyttöohje](./docs/kayttoohje.md)

## Viikkoraportit
[Viikko 1](./docs/viikkoraportit/viikkoraportti1.md)

[Viikko 2](./docs/viikkoraportit/viikkoraportti2.md)

[Viikko 3](./docs/viikkoraportit/viikkoraportti3.md)

[Viikko 4](./docs/viikkoraportit/viikkoraportti4.md)


# Asennus ja käynnitysohje
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

Sovelluksen käyttöliittymä aukeaa terminaalin antamaan osoitteeseen, josta klikkaamalla aukeaa aloitusnökymä. Lokaalista pyörivän sovelluksen voi sulkea terminaalista Ctrl+C.
