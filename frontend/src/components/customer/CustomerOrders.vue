<template>
  <v-row justify="center">
    <v-expansion-panels inset>
      <v-expansion-panel v-for="(item, i) in 5" :key="i">
        <v-expansion-panel-header>Item</v-expansion-panel-header>
        <v-expansion-panel-content>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-row>
  <!-- <v-col cols="12">
      <v-card>
        <v-subheader>Активные заказы</v-subheader>
        <v-list two-line>
          <template v-for="n in 6">
            <v-list-item :key="n">
              <v-list-item-avatar color="grey darken-1"> </v-list-item-avatar>

              <v-list-item-content>
                <v-list-item-title>Message {{ n }}</v-list-item-title>

                <v-list-item-subtitle>
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                  Nihil repellendus distinctio similique
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-divider v-if="n !== 6" :key="`divider-${n}`" inset></v-divider>
          </template>
        </v-list>
      </v-card>
    </v-col>
    <v-col cols="12">
      <v-card>
        <v-subheader>Архив заказов</v-subheader>
        <v-list two-line>
          <template v-for="n in 6">
            <v-list-item :key="n">
              <v-list-item-avatar color="grey darken-1"> </v-list-item-avatar>

              <v-list-item-content>
                <v-list-item-title>Message {{ n }}</v-list-item-title>

                <v-list-item-subtitle>
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                  Nihil repellendus distinctio similique
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-divider v-if="n !== 6" :key="`divider-${n}`" inset></v-divider>
          </template>
        </v-list>
      </v-card>
    </v-col> -->
</template>

<script>
export default {
  name: "CustomerOrders",
  data() {
    return {
      cards: ["Today", "Yesterday"]
    };
  }
};
</script>

<style lang="scss" scoped></style>
