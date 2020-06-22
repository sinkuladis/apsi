<template>
    <div class="main-body">
        <h1> Kontakt </h1>
        Jeśli masz jakieś pytania lub potrzebujesz pomocy napisz do nas: pomoc@olxample.pl
    </div>
    
</template>

<script>
    export default {
        name: "Help"
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