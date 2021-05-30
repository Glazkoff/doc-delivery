<template>
  <v-app id="inspire">
    <v-app-bar app color="primary" dark
      ><v-app-bar-nav-icon dark @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-white">DocDelivery</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn class="accent" to="/customer/order-delivery"
        ><v-icon left dark>mdi-plus</v-icon>СДЕЛАТЬ ЗАКАЗ</v-btn
      >
    </v-app-bar>
    <v-system-bar v-if="isNotification" app color="secondary" dark>
      У заказа #321213 изменился статус на "Доставлено"
      <v-spacer></v-spacer>

      <v-icon @click="isNotification = false">mdi-close-circle</v-icon>
    </v-system-bar>

    <v-navigation-drawer v-model="drawer" app>
      <v-sheet color="white lighten-2" class="pa-4">
        <v-avatar class="mb-4" color="grey darken-1" size="64"></v-avatar>
        <div>Никита Глазков, <strong>клиент</strong></div>
        <div>john@vuetifyjs.com</div>
      </v-sheet>

      <v-divider></v-divider>

      <v-list>
        <v-list-item
          v-for="[icon, text, to] in links"
          :exact="true"
          :key="icon"
          :to="to"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <v-container class="py-8 px-6" fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
    <v-footer>
      <v-card-text class="py-2 text-center">
        {{ new Date().getFullYear() }} —
        <strong>Глазков Никита, 181-321</strong>
      </v-card-text></v-footer
    >
  </v-app>
</template>

<script>
export default {
  name: "Customer",
  data: () => ({
    drawer: null,
    links: [
      ["mdi-home", "Главная", "/customer"],
      ["mdi-bike-fast", "Заказать доставку", "/customer/order-delivery"],
      ["mdi-clipboard-list", "Мои доставки", "/customer/orders"],
      ["mdi-alert-octagon", "Выйти", "/auth"]
    ],
    isNotification: true
  })
};
</script>

<style lang="scss" scoped></style>
