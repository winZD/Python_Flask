### Web app:

Na prvoj ruti se nalazi radarska slika trenutnog stanja neba nad Europom.

Ispod nje se nalazi google maps.

U gornjem dijelu, na lijevoj strani se nalazi padajuæa lista 10 gradova,
te pristiskom na gumb se pristupa funkciji result() koja je odgovorna za 
povlaèenje api-a.

U isto vrijeme se renderira template result.html na kojem se vidi trenutno vrijeme, te prikaz
vremena za sljedeæih nekoliko dana(za odabrani grad)

Aktiviranjem botuna "Chart" aktivitira se funkcija log() koja validira korisnièke podatke na unos.
Ukoliko su ispravni korisnik pristupa interaktivnoj mapi koja prikazuje kontinente te zemlje
odakle se oèitavaju mjerenja podataka 