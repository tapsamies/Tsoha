# Keskustelusovellus
Tämän projektin tavoitteena on luoda nimensä mukaisesti keskustelusovellus, joka noudattaa kurssin esimerkkiaiheen määritelmää keskustelusovelluksesta.

## Tehdyt toiminnallisuudet
- Mahdollista luoda käyttäjä, joka kirjautuu ulos/sisään
- Ylläpitäjä voi tehdä uusia alueita

## Tekemättömät toiminnallisuudet
- Käyttäjä näkee aihealueet ja viimeisimmän viestin jokaisesta aihealueesta
- Käyttäjä voi luoda aihealueiden sisälle uusia ketjuja
- Käyttäjä voi vastata olemassa olevaan ketjuun ja muokata omia viestejään
- Käyttäjä voi lainata muiden viestejä
- Käyttäjä voi poistaa oman ketjunsa
- Käyttäjä voi etsiä viestit/ ketjut hakusanojen perusteella
- Ylläpitäjä voi poistaa keskustelualueita
- Ylläpitäjä voi lukita ja poistaa ketjuja sekä käyttäjiä
- Ylläpitäjä voi tehdä rajattuja alueita ja määrittää pääsyoikeuksia käyttäjille

### Sovelluksen käyttö
- Sovellus on käytettävissä [fly.io:n puolella](https://tsoha-keskustelusovellus.fly.dev/), mutta voit ajaa sitä myös paikallisesti.
- Ylläpidon toiminnallisuutta voi testata tunnuksella "admin", jonka salasana on sama kuin käyttäjätunnus. 

### Paikallinen käyttö
- Käyttöä varten PostgreSQL tulee olla asennettuna, [linkki asennussivulle](https://www.postgresql.org/download/)
- Suorita seuraavat komennot sovelluksen käyttämistä varten kloonattuasi repon omalle (linux) tietokoneellesi:
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- psql < schema.sql
- flask run
- voit testata sovellusta selaimella osoitteessa 127.0.0.1:5000
- voit sulkea flaskin terminaalissa painamalla ctrl+c 
- voit sulkea python virtuaaliympäristön komennolla deactivate
