# Kierunkowskaz

Nasza aplikacja zada użytkownikowi kilka pytań na temat jego
preferencji w temacie nauki, życia i kilku innych cech i na
podstawie odpowiedzi zaproponuje 5 najlepiej dopasowanych 
kierunków studiów.

## Jak to się dzieje?
Żeby uzyskać powyżej przedstawiony efekt korzystamy z **twierdzenia
Bayesa**. Wiedząc że 90% studentów matematyki lubi przedmioty ścisłe
możemy policzyć prawdopodobieństwo tego że ktoś będzie stduiował
informatykę lubiąc przedmioty ścisłe korzystając ze wzoru:<br />
![wzor](./images/stary.png) <br />
Gdzie:
P(A|B) - Prawdopodobieństwo tego że ktoś będzie stduiował
informatykę lubiąc przedmioty ścisłe <br />
P(B|A) - Prawdopodobieństwo tego że ktoś lubi przedmioty ścisłe
studiując informatykę <br />
P(A) - Prawdopodobieństwo że dany kierunek studiów to 
informatyka <br />
P(B|A') - Prawdopodobieństwo tego że ktoś lubi przedmioty ścisłe
nie studiując informatyki <br />
P(A') - Prawdopodobieństwo że dany kierunek studiów to nie jest
informatyka <br />

## Jak dobieramy pytania
[Entropia :))](https://pl.wikipedia.org/wiki/Entropia_(teoria_informacji))
<br />
(Szukamy pytania które da największy spadek entropi.)
