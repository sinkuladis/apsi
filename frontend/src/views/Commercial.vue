<template>
    <div class="main-body">
            <h1> U nas łatwo uruchomisz reklamę</h1>
        <section>
            <h1> Czemu warto nas wybrać?</h1>
            <ol>
                <li> reklamy zaczynają się już od 500 zł</li>
                <li> czas kampanii można ustawić nawet na 3 miesiące</li>
                <li> Umożliwiamy podgląd statystyk na koncie klienta</li>
            </ol>

            <h1> Jakie formy reklamy umożliwiamy?</h1>
            <ol>
                <li> top ogłoszenia</li>
                <li> reklama banerowa </li>
            </ol>
        </section>
    </div>
    
</template>

<script>
    export default {
        name: "Commercial"
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