<template>
  <v-container>
    <v-row justify="center">
      <h1 class="text-center">Заказы</h1>
    </v-row>

    <v-row justify="center">
      <v-col>
        <v-data-table
          :headers="headers"
          :items="orders"
          :expanded.sync="expanded"
          :single-expand="singleExpand"
          item-key="id"
          show-expand
          class="elevation-1"
          v-if="!loading"
          multi-sort
          loading-text="Загрузка списка заказов... Пожалуйста, подождите"
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
                    <p class="text-left">
                      <strong>Дата получения:</strong><br />{{
                        item.arrival_date
                      }}
                    </p>
                    <p class="text-left">
                      <strong>Кто отправлял документы:</strong><br />{{
                        item.sender
                      }}
                    </p>
                    <p class="text-left">
                      <strong>Кто получал документы:</strong><br />{{
                        item.recipient
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
          loading-text="Loading... Please wait"
        ></v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import MapTwoDots from "../MapTwoDots";
export default {
  name: "CustomerOrders",
  data() {
    return {
      loading: false,
      singleExpand: false,
      expanded: [],
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
        { text: "", value: "data-table-expand" }
      ],
      orders: [
        {
          id: 0,
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
          }
        }
      ]
    };
  },
  components: {
    MapTwoDots
  },
  async mounted() {
    this.loading = true;
    try {
      let res = await this.$http.get("/api/orders");
      if (res.data.length != null) {
        console.log(res.data);
        res.data.forEach(element => {
          if (element.courier != null) {
            element.courier = element.courier.name;
          } else {
            element.courier = "-";
          }
          if (element.arrival_date == null) {
            element.arrival_date = "-";
          }
          element.pointFrom = {};
          element.pointTo = {};
          element.pointFrom.lat = element.pointFromLat;
          element.pointFrom.lng = element.pointFromLng;
          element.pointTo.lat = element.pointToLat;
          element.pointTo.lng = element.pointToLng;

          switch (element.status) {
            case "0":
            default:
              element.status = "Поиск курьера";
              break;

            case "1":
              element.status = "Курьер движется к отправителю";
              break;

            case "2":
              element.status = "Курьер движется к получателю";
              break;

            case "3":
              element.status = "Подтверждение личности получателя";
              break;

            case "4":
              element.status = "Передача посылки получателю";
              break;

            case "5":
              element.status = "Завершено";
              break;
          }
          this.orders.push(element);
        });
      }
      this.loading = false;
    } catch (error) {
      console.log(error);
      this.loading = false;
    }
  }
};
</script>

<style lang="scss" scoped></style>
