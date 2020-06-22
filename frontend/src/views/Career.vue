<template>
    <div class="main-body">
        <h1> Kariera w Olx<bold>ample</bold></h1>
        <h2 style="text-align:left">
            Obecnie rekrutujemy na stanowiska:
        </h2>
            <ul>
              <li> <a href="/data_analyst.pdf">Data Analyst</a> </li>
              <li> <a href="/data_engineer.pdf"> Data Engineer</a> </li>
              <li> <a href="/software_engineer.pdf">Software Engineer</a> </li>
            </ul>
        <section>
        <h2 style="text-align:left">
            Dlaczego my?
        </h2>
        <ul>
          <li>nieprzeciętni współpracownicy </li>
          <li>realny wpływ na </li>
          <li>nowoczesne technologie</li>
          <li>ciekawe projekty</li>
          <li>rozwój osobisty</li>
        </ul>
        </section>

        <section>
        <h2 style="text-align:left">
            Benefity?
        </h2>
        <ul>
          <li>Atrakcyjne przestrzenie biurowe </li>
          <li>MindUp </li>
          <li>Prywatna opieka medyczna</li>
          <li>Karta sportowa</li>
          <li>Ubezpieczenie na życie</li>
        </ul>
        </section>

        <section>
        <h2 style="text-align: left"> Jeśli jesteś zainteresowany pracą u nas:</h2>
        <ol>
          <li> Prześlij CV i list motywacyjny na adres: olxample@olxample.pl </li>
          <li> Rozwiąż zadanie</li>
          <li> Przyjdź na spotkanie</li>
          <li> Zacznij pracę</li>
        </ol>
        </section>

    </div>
</template>

<script>
    export default {
        name: "Career"
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

    .section {
        margin: 10px;
    }
    .options {
      display: flex;
      justify-content: center;

      button {
        margin: 5px;
      }
    }
</style>