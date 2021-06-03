<template>
  <v-container>
    <v-row justify="center">
      <h1 class="text-center mb-4">Ваша зарплата</h1>
    </v-row>
    <v-row>
      <v-col offset-md="1" md="5" xs="12">
        <v-card outlined class="pt-4 pb-4">
          <p>За текущий месяц вы заработали</p>
          <h2 class="display-2">46,560 ₽</h2>
        </v-card>
        <v-card outlined class="pt-4 pb-4 mt-5">
          <p>За текущий месяц выполнено</p>
          <h2 class="display-2">15 заказов</h2>
        </v-card>
        <v-card outlined class="pt-4 pb-4 mt-5">
          <p>За всё время выполнено заказов</p>
          <h2 class="display-1 text--secondary">89 заказов</h2>
        </v-card>
      </v-col>
      <v-col md="5" xs="12">
        <v-card outlined class="pt-4 pb-4">
          <p>Пешком пройдено</p>
          <h2 class="display-1 text--secondary">78 км</h2>
        </v-card>
        <v-card outlined class="pt-4 pb-4 mt-5">
          <p>Заработано пешком</p>
          <h2 class="display-1 text--secondary">8,345 ₽</h2>
        </v-card>
        <v-card outlined class="pt-4 pb-4 mt-5">
          <p>Пройдено на автомобиле</p>
          <h2 class="display-1 text--secondary">878 км</h2>
        </v-card>
        <v-card outlined class="pt-4 pb-4 mt-5">
          <p>Заработано на автомобиле</p>
          <h2 class="display-1 text--secondary">18,675 ₽</h2>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "CourierSalary"
};
</script>

<style lang="scss" scoped></style>
