<template>
  <v-app id="inspire">
    <v-app-bar app color="primary" dark
      ><v-app-bar-nav-icon dark @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-white">DocDelivery</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn class="blue darken" to="/courier"
        ><v-icon left dark>mdi-plus</v-icon>ПРИНЯТЬ ЗАКАЗ</v-btn
      >
    </v-app-bar>
    <v-system-bar v-if="isNotification" app color="secondary" dark>
      Появился свободный заказ #321213
      <v-spacer></v-spacer>

      <v-icon @click="isNotification = false" color="red"
        >mdi-close-circle</v-icon
      >
    </v-system-bar>

    <v-navigation-drawer v-model="drawer" app>
      <v-sheet color="white lighten-2" class="pa-4">
        <v-avatar class="mb-4" color="grey darken-1" size="64"></v-avatar>
        <div>Никита Глазков, <strong>курьер</strong></div>
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
  name: "Courier",
  data: () => ({
    drawer: null,
    links: [
      // ["mdi-home", "Главная", "/courier"],
      ["mdi-bike-fast", "Активные заказы", "/courier"],
      ["mdi-folder-clock", "Архив заказов", "/courier/archieve-orders"],
      ["mdi-cash", "Зарплата", "/courier/salary"],
      ["mdi-alert-octagon", "Выйти", "/auth"]
    ],
    isNotification: true
  })
};
</script>

<style lang="scss" scoped></style>
