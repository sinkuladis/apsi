<template>
        <div class="main-body">
            <h1> Jak działamy?</h1>

            <section>
            <h1> Sprzedaj - docieraj do nabywców w całej Polsce:</h1>
            <ol>
              <li> <bold>  Zrób zdjęcia tego, co sprzedajesz </bold>  - przeczytaj, jak pisać ogłoszenia, przekonaj się,
dlaczego warto dodać zdjęcia i dowiedz się, jak sprzedawać szybciej.  </li>
              <li> <bold> Dodaj ogłoszenie </bold> - dodaj dokładny opis oraz zdjęcia i poczekaj na kontakt od
                  kupujących.</li>
                <li> <bold> Odpowiadaj kupującym </bold> - reaguj na pytania, udzielaj dokładnych informacji i
                    dogaduj szczegóły zakupu.</li>
                <li> <bold> Sprzedaj i przekaż zakup </bold> - skorzystaj z przesyłki  lub umów się na odbiór
                    osobisty w bezpiecznym miejscu publicznym. </li>
                <li> <bold> Przekaż procent na walkę z COVID-19 </bold>  </li>
            </ol>
            </section>

            <section>
            <h1> Kup - znajduj najlepsze okazje blisko Ciebie:</h1>

            <ol>
              <li> <bold> Poszukaj </bold> - skorzystaj z wyszukiwania na stronie głównej lub sprawdź nasze kategorie, aby przeglądać ogłoszenia, które Cię interesują. </li>
              <li> <bold> Wybierz  </bold> - przyjrzyj się zdjęciu w ogłoszeniu, uważnie przeczytaj opis i zajrzyj na profil sprzedającego.</li>
              <li> <bold> Skontaktuj się </bold> - wyślij sprzedającemu wiadomość. Dowiedz się więcej o ofercie, negocjuj cenę lub po prostu umów się na zakup.</li>
              <li> <bold> Kup i odbierz </bold> - skorzystaj z bezpiecznej przesyłki lub umów się na odbiór osobisty w bezpiecznym miejscu publicznym. </li>
            </ol>
            </section>


        </div>
</template>

<script>
    export default {
        name: "About"
    }
</script>

<style scoped lang="scss">
    .main-body {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding-bottom: 10rem;
    }


    .options {
      display: flex;
      justify-content: center;

      button {
        margin: 5px;
      }
    }
</style>