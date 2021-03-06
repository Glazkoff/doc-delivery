import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "@/plugins/vuetify";
import { LMap, LTileLayer, LMarker, LTooltip, LPolyline } from "vue2-leaflet";
import "leaflet/dist/leaflet.css";
import Vue2LeafletLocatecontrol from "vue2-leaflet-locatecontrol";
import Vuelidate from "vuelidate";
import { Icon } from "leaflet";
import axios from "axios";
import VueAxios from "vue-axios";
import VueCookies from "vue-cookies";

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png")
});

Vue.config.productionTip = false;

Vue.use(Vuelidate);

Vue.component("l-map", LMap);
Vue.component("l-tooltip", LTooltip);
Vue.component("l-polyline", LPolyline);
Vue.component("l-tile-layer", LTileLayer);
Vue.component("l-marker", LMarker);
Vue.component("v-locatecontrol", Vue2LeafletLocatecontrol);

Vue.use(VueAxios, axios);
Vue.use(VueCookies);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
