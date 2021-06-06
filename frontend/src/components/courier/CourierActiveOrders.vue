<template>
  <v-container>
    <v-row justify="center">
      <h1 class="text-center mb-4">Текущие заказы</h1>
    </v-row>
    <v-row justify="center">
      <v-col>
        <v-data-table
          :headers="headers"
          :items="orders"
          item-key="name"
          class="elevation-1"
          v-if="!loading"
          multi-sort
          no-data-text="Пока здесь нет заказов"
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
    <v-row justify="center">
      <v-col>
        <v-data-table
          :headers="headers"
          :items="freeOrders"
          item-key="name"
          class="elevation-1"
          v-if="!loading"
          show-expand
          multi-sort
          no-data-text="Пока здесь нет заказов"
          :footer-props="{
            'items-per-page-text': 'Заказов на странице',
            pageText: '{0}-{1} из {2}'
          }"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title>Свободные заказы</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
          </template>
          <!-- eslint-disable-next-line -->
          <template v-slot:item.actions="{ item }">
            <div class="mt-2">
              <div v-if="item.actions.length !== 0">
                <div :key="button.text" v-for="(button, index) in item.actions">
                  <v-btn
                    :color="button.color"
                    :dark="button.dark"
                    class="mb-2"
                    @click="getAnOrder(index)"
                    >{{ button.text }}</v-btn
                  >
                </div>
              </div>
            </div>
          </template>
          <template v-slot:expanded-item="{ headers, item }">
            <td :colspan="headers.length">
              <v-row>
                <v-col cols="4" md="4" sm="12"
                  ><div class="pt-4 pb-4">
                    <h4 class="mb-4">Подробно о заказе №{{ item.id }}</h4>
                    <p class="text-left">
                      <strong>От:</strong><br />{{ item.address_from }}
                    </p>
                    <p class="text-left">
                      <strong>До:</strong><br />{{ item.address_to }}
                    </p>
                    <p class="text-left">
                      <strong>Дата отправки:</strong><br />{{
                        item.departure_date
                      }}
                    </p>
                  </div></v-col
                >
                <v-col cols="8" md="8" sm="12" align-self="center">
                  <MapTwoDots
                    class="mt-4 mb-4"
                    :from="item.pointFrom"
                    :to="item.pointTo"
                  ></MapTwoDots>
                </v-col>
              </v-row>
            </td>
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
import MapTwoDots from "../MapTwoDots.vue";
export default {
  name: "CourierActiveOrders",
  components: {
    MapTwoDots
  },
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
        { text: "Действия", value: "actions", sortable: false },
        { text: "", value: "data-table-expand" }
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
              color: "primary",
              text: "Начать исполнение",
              to: "/courier/order/1"
            }
          ]
        }
      ],
      freeOrders: [
        {
          id: 2,
          departure_date: "25.03.2020",
          arrival_date: "-",
          courier: "-",
          status: "Идёт поиск курьера",
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
              color: "black",
              dark: true,
              text: "Взять заказ на себя",
              to: "/courier/order/1"
            }
          ]
        }
      ]
    };
  },
  methods: {
    getAnOrder(index) {
      this.freeOrders[index].courier = "Иванов С.А.";
      this.freeOrders[index].status = "Заказ принят курьером";
      this.freeOrders[index].actions = [
        {
          color: "primary",
          text: "Начать исполнение",
          to: `/courier/order/${this.freeOrders[index].id}`
        }
      ];
      this.orders.push(this.freeOrders[index]);
      this.freeOrders.splice(index, 1);
    }
  }
};
</script>

<style lang="scss" scoped></style>
