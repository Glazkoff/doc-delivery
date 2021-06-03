<template>
  <v-container>
    <v-row justify="center">
      <h1 class="text-center mb-4">Заказы</h1>
    </v-row>
    <router-link to="/courier/order/1">Заказ</router-link>
    <v-row justify="center">
      <v-col>
        <v-data-table
          :headers="headers"
          :items="orders"
          item-key="name"
          class="elevation-1"
          v-if="!loading"
          multi-sort
          :footer-props="{
            'items-per-page-text': 'Заказов на странице',
            pageText: '{0}-{1} из {2}'
          }"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title>Активные заказы</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
          </template>
          <!-- eslint-disable-next-line -->
          <template v-slot:item.actions="{ item }">
            <div class="mt-2">
              <div v-if="item.actions.length !== 0">
                <div :key="button.text" v-for="button in item.actions">
                  <v-btn :color="button.color" class="mb-2" :to="button.to">{{
                    button.text
                  }}</v-btn>
                </div>
              </div>
            </div>
          </template>
        </v-data-table>
        <v-data-table
          v-else
          item-key="id"
          class="elevation-1"
          loading
          loading-text="Идёт загрузка... Пожалуйста, подождите"
        ></v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "CourierActiveOrders",
  data() {
    return {
      loading: false,
      headers: [
        {
          text: "Код доставки",
          align: "start",
          sortable: false,
          value: "id"
        },
        { text: "Дата отправки", value: "departure_date" },
        { text: "Дата получения", value: "arrival_date" },
        { text: "Курьер", value: "courier" },
        { text: "Статус", value: "status" },
        { text: "Действия", value: "actions", sortable: false }
      ],
      orders: [
        {
          id: 1,
          departure_date: "25.03.2020",
          arrival_date: "25.03.2020",
          courier: "Иванов С.А.",
          status: "Передан курьеру",
          address_from: "г Астрахань, ул Победы, д 54",
          address_to: "г Волгоград, ул Строителей, д 12",
          sender: "Иванов Фёдор Павлович",
          recipient: "Фёдоров Павел Иванович",
          pointFrom: {
            lat: 46.355551,
            lng: 48.057676
          },
          pointTo: {
            lat: 48.606571,
            lng: 44.3626
          },
          actions: [
            {
              color: "success",
              text: "Начать исполнение",
              to: "/courier/order/1"
            }
          ]
        }
      ]
    };
  }
};
</script>

<style lang="scss" scoped></style>
