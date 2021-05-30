<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="4" sm="12">
        <v-card class="pb-2">
          <v-card-title
            class="headline font-weight-regular blue-grey white--text"
          >
            Откуда забрать
          </v-card-title>
          <v-autocomplete
            v-model="deliveryFrom"
            :loading="searchFromLoading"
            :items="itemsFrom"
            :search-input.sync="searchFrom"
            cache-items
            class="pt-2 mx-4"
            flat
            hide-details
            label="Саратов, ул Строителей, 5"
            no-data-text="Не удаётся найти адрес"
            solo
            clearable
            autocomplete="address"
          ></v-autocomplete>
        </v-card>
        <v-card class="mt-4 pb-2">
          <v-card-title
            class="headline font-weight-regular blue-grey white--text"
          >
            Куда доставить
          </v-card-title>
          <v-autocomplete
            v-model="deliveryTo"
            :loading="searchToLoading"
            :items="itemsTo"
            :search-input.sync="searchTo"
            cache-items
            class="pt-2 mx-4"
            flat
            no-data-text="Не удаётся найти адрес"
            hide-details
            label="Самара, ул Достоевского, 6"
            solo
            clearable
          ></v-autocomplete>
        </v-card>
        <v-radio-group v-model="delivery_way">
          <template v-slot:label>
            <div>Как доставить</div>
          </template>
          <v-radio value="onfoot">
            <template v-slot:label>
              <div>Пешком</div>
            </template>
          </v-radio>
          <v-radio value="oncar">
            <template v-slot:label>
              <div>На автомобиле</div>
            </template>
          </v-radio>
        </v-radio-group>
        <v-radio-group v-model="weight">
          <template v-slot:label>
            <div>Вес посылки</div>
          </template>
          <v-radio value="1">
            <template v-slot:label>
              <div>До 1 кг</div>
            </template>
          </v-radio>
          <v-radio value="5">
            <template v-slot:label>
              <div>До 5 кг</div>
            </template>
          </v-radio>
          <v-radio value="10">
            <template v-slot:label>
              <div>До 10 кг</div>
            </template>
          </v-radio>
          <v-radio value="15">
            <template v-slot:label>
              <div>До 15 кг</div>
            </template>
          </v-radio>
        </v-radio-group>
        <v-text-field
          v-model="documentCost"
          label="Ценность посылки"
          type="number"
          :messages="[
            `+ ${Math.round(this.documentCost * 0.1)} ₽ к стоимости посылки`,
            `Максимум 50000₽`
          ]"
          max="50000"
          min="0"
          @input="$v.documentCost.$touch()"
          @blur="$v.documentCost.$touch()"
          ><strong slot="append">₽</strong></v-text-field
        >
        <v-radio-group v-model="payment_way">
          <template v-slot:label>
            <div>Способ оплаты</div>
          </template>
          <v-radio value="card">
            <template v-slot:label>
              <div>Картой онлайн</div>
            </template>
          </v-radio>
          <v-radio value="cash">
            <template v-slot:label>
              <div>Наличными курьеру</div>
            </template>
          </v-radio>
          <v-radio value="cardbonus">
            <template v-slot:label>
              <div>Картой онлайн + бонусами Сбер Спасибо</div>
            </template>
          </v-radio>
        </v-radio-group>
      </v-col>
      <v-col cols="12" md="8" sm="12">
        <MapTwoDots :from="pointFrom" :to="pointTo"></MapTwoDots>
        <v-row>
          <v-col col="6" md="6" sm="12"
            ><v-text-field
              v-model="personFrom"
              :error-messages="personFromErrors"
              required
              @input="$v.personFrom.$touch()"
              @blur="$v.personFrom.$touch()"
              label="Кто отправляет документы"
              append-icon="mdi-account"
            ></v-text-field
          ></v-col>
          <v-col col="6" md="6" sm="12"
            ><v-text-field
              v-model="personFromPhone"
              :error-messages="personFromPhoneErrors"
              required
              @input="$v.personFromPhone.$touch()"
              @blur="$v.personFromPhone.$touch()"
              label="Номер телефона отправителя"
              append-icon="mdi-phone"
            ></v-text-field
          ></v-col>
        </v-row>
        <v-row>
          <v-col col="6" md="6" sm="12"
            ><v-text-field
              :error-messages="personToPhoneErrors"
              required
              @input="$v.personTo.$touch()"
              @blur="$v.personTo.$touch()"
              v-model="personTo"
              label="Кто получит документы"
              append-icon="mdi-account"
            ></v-text-field
          ></v-col>
          <v-col col="6" md="6" sm="12"
            ><v-text-field
              v-model="personToPhone"
              :error-messages="personToPhoneErrors"
              required
              @input="$v.personToPhone.$touch()"
              @blur="$v.personToPhone.$touch()"
              label="Номер телефона получателя"
              append-icon="mdi-phone"
            ></v-text-field
          ></v-col>
        </v-row>
        <v-row justify="center" v-if="costLoading">
          <v-progress-circular indeterminate size="64"></v-progress-circular>
        </v-row>
        <v-row class="sticky" v-else>
          <v-col cols="12">
            <h4 v-if="distance !== 0">
              Расстояние: {{ Math.round(distance * 100) / 100 }} км
            </h4>
          </v-col>
          <v-col cols="12">
            <h2 v-if="deliveryCost !== 0">Итого: {{ deliveryCost }} ₽</h2>
            <h2 v-else>
              Введите адрес отправителя и получателя, а также выберите
              подходящие параметры доставки
            </h2>
          </v-col>

          <v-btn
            class="mt-4"
            block
            @click="calculateCost()"
            :disabled="deliveryTo == '' || deliveryFrom == '' || !formIsValid"
            >Отправить заказ</v-btn
          >
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import MapTwoDots from "../MapTwoDots";
import { latLng } from "leaflet";
import { validationMixin } from "vuelidate";
import {
  required
  // maxLength
} from "vuelidate/lib/validators";

function distance(lat1, lon1, lat2, lon2, unit) {
  if (lat1 == lat2 && lon1 == lon2) {
    return 0;
  } else {
    var radlat1 = (Math.PI * lat1) / 180;
    var radlat2 = (Math.PI * lat2) / 180;
    var theta = lon1 - lon2;
    var radtheta = (Math.PI * theta) / 180;
    var dist =
      Math.sin(radlat1) * Math.sin(radlat2) +
      Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
    if (dist > 1) {
      dist = 1;
    }
    dist = Math.acos(dist);
    dist = (dist * 180) / Math.PI;
    dist = dist * 60 * 1.1515;
    if (unit == "K") {
      dist = dist * 1.609344;
    }
    if (unit == "N") {
      dist = dist * 0.8684;
    }
    return dist;
  }
}

const token = "636455d0a05f8d1524f174d40703080dc0ee0879";
export default {
  name: "CustomerOrderDelivery",
  components: {
    MapTwoDots
  },
  data() {
    return {
      deliveryCost: 0,
      distance: 0,
      deliveryTo: "",
      deliveryFrom: "",
      itemsFrom: [],
      itemsTo: [],
      pointFrom: null,
      pointTo: null,
      searchToLoading: false,
      searchFromLoading: false,
      searchTo: null,
      searchFrom: null,
      delivery_way: "onfoot",
      weight: "1",
      payment_way: "card",
      documentCost: 0,
      personFrom: "",
      personFromPhone: "",
      personTo: "",
      personToPhone: "",
      costLoading: false
    };
  },
  mixins: [validationMixin],
  validations: {
    personTo: { required },
    personToPhone: { required },
    personFrom: { required },
    personFromPhone: { required }
  },
  computed: {
    formIsValid() {
      let a =
        this.$v.personTo.$invalid ||
        this.$v.personToPhone.$invalid ||
        this.$v.personFrom.$invalid ||
        this.$v.personFromPhone.$invalid;
      console.log("personTo", this.$v.personTo.$invalid);
      console.log("personToPhone", this.$v.personToPhone.$invalid);
      console.log("personFrom", this.$v.personFrom.$invalid);
      console.log("personFromPhone", this.$v.personFromPhone.$invalid);

      console.log(!a);
      return !a;
    },
    personToErrors() {
      const errors = [];
      if (!this.$v.personTo.$dirty) return errors;
      !this.$v.personTo.required && errors.push("Поле обязательно!");
      return errors;
    },
    personToPhoneErrors() {
      const errors = [];
      if (!this.$v.personToPhone.$dirty) return errors;
      !this.$v.personToPhone.required && errors.push("Поле обязательно!");
      return errors;
    },
    personFromErrors() {
      const errors = [];
      if (!this.$v.personFrom.$dirty) return errors;
      !this.$v.personFrom.required && errors.push("Поле обязательно!");
      return errors;
    },
    personFromPhoneErrors() {
      const errors = [];
      if (!this.$v.personFromPhone.$dirty) return errors;
      !this.$v.personFromPhone.required && errors.push("Поле обязательно!");
      return errors;
    }
  },
  watch: {
    async searchTo(val) {
      try {
        var url =
          "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address";

        var options = {
          method: "POST",
          mode: "cors",
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
            Authorization: "Token " + token
          },
          body: JSON.stringify({ query: val })
        };

        fetch(url, options)
          .then(response => response.json())
          .then(result => {
            this.itemsTo = [];
            result.suggestions.forEach(element => {
              this.itemsTo.push(element.value);
            });
          })
          .catch(error => console.log("error", error));
      } catch (e) {
        console.log(e);
      }
    },
    async searchFrom(val) {
      try {
        var url =
          "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address";

        var options = {
          method: "POST",
          mode: "cors",
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
            Authorization: "Token " + token
          },
          body: JSON.stringify({ query: val })
        };

        fetch(url, options)
          .then(response => response.json())
          .then(result => {
            this.itemsFrom = [];
            result.suggestions.forEach(element => {
              this.itemsFrom.push(element.value);
            });
          })
          .catch(error => console.log("error", error));
      } catch (e) {
        console.log(e);
      }
    },
    deliveryTo: function () {
      if (this.deliveryTo !== "" && this.deliveryFrom !== "") {
        this.calculateCost();
      } else {
        this.deliveryCost = 0;
      }
    },
    deliveryFrom: function () {
      if (this.deliveryTo !== "" && this.deliveryFrom !== "") {
        this.calculateCost();
      } else {
        this.deliveryCost = 0;
      }
    },
    weight: function () {
      if (this.deliveryTo !== "" && this.deliveryFrom !== "") {
        this.calculateCost();
      } else {
        this.deliveryCost = 0;
      }
    },
    delivery_way: function () {
      if (this.deliveryTo !== "" && this.deliveryFrom !== "") {
        this.calculateCost();
      } else {
        this.deliveryCost = 0;
      }
    },
    documentCost: function () {
      if (this.deliveryTo !== "" && this.deliveryFrom !== "") {
        this.calculateCost();
      } else {
        this.deliveryCost = 0;
      }
    }
  },
  methods: {
    async collectCoordinates(query) {
      const yaToken = "8bde1945-9e21-4512-85b2-ad2ea38283d0";
      var url = `https://geocode-maps.yandex.ru/1.x?geocode=${encodeURI(
        query
      )}&format=json&apikey=${yaToken}`;

      var options = {
        method: "GET",
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json"
        }
      };
      let response = await fetch(url, options);
      let result = await response.json();
      return result.response.GeoObjectCollection.featureMember[0].GeoObject
        .Point.pos;
    },
    async calculateCost() {
      this.costLoading = true;
      let coordFrom = await this.collectCoordinates(this.deliveryFrom);
      console.log("coordFrom", coordFrom);
      let coordTo = await this.collectCoordinates(this.deliveryTo);
      console.log("coordTo", coordTo);
      let xTo = coordTo.split(" ")[0];
      let yTo = coordTo.split(" ")[1];
      this.pointTo = latLng(yTo, xTo);
      console.log(this.pointTo);

      let xFrom = coordFrom.split(" ")[0];
      let yFrom = coordFrom.split(" ")[1];
      this.pointFrom = latLng(yFrom, xFrom);
      console.log(this.pointFrom);

      this.distance = distance(xFrom, yFrom, xTo, yTo, "K");
      console.log("Distance: ", this.distance);

      let costPerKm = 25;
      let onFootCoef = 1.2;
      let onCarCoef = 1.3;

      let coefFor1kg = 1.01;
      let coefFor5kg = 1.05;
      let coefFor10kg = 1.1;
      let coefFor15kg = 1.15;

      let deliveryCost = this.distance * costPerKm;

      switch (this.delivery_way) {
        case "onfoot":
        default:
          deliveryCost *= onFootCoef;
          break;
        case "oncar":
          deliveryCost *= onCarCoef;
          break;
      }
      switch (this.weight) {
        case "1":
        default:
          deliveryCost *= coefFor1kg;
          break;
        case "5":
          deliveryCost *= coefFor5kg;
          break;
        case "10":
          deliveryCost *= coefFor10kg;
          break;
        case "15":
          deliveryCost *= coefFor15kg;
          break;
      }
      deliveryCost += Math.round(this.documentCost * 0.1);
      this.deliveryCost = Math.round(deliveryCost * 100) / 100;
      this.costLoading = false;
    }
  }
};
</script>

<style lang="scss" scoped>
.sticky {
  position: sticky;
  right: 0;
  bottom: 0;
  z-index: 1000;
  background-color: white;
  padding-bottom: 1rem;
}
</style>
