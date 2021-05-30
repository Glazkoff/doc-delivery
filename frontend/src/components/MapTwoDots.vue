<template>
  <div @click="tryThing()">
    <l-map
      ref="map"
      :crs="layer.crs"
      :zoom="zoom"
      :center="to != null ? to : center"
      style="height: 300px; width: 100%"
    >
      <l-tile-layer
        :url="layer.url"
        :subdomains="layer.subdomains"
        :attribution="layer.attribution"
      />

      <l-marker :lat-lng="from" v-if="from != null">
        <l-tooltip :options="{ permanent: true, interactive: true }">
          Откуда заберём документы
        </l-tooltip>
      </l-marker>
      <l-marker :lat-lng="to" v-if="to != null">
        <l-tooltip :options="{ permanent: true, interactive: true }">
          Куда доставим документы
        </l-tooltip>
      </l-marker>
      <l-polyline
        v-if="from != null && to != null"
        :lat-lngs="[to, from]"
        :color="'#27A440'"
      />
    </l-map>
  </div>
</template>

<script>
import { CRS, latLng } from "leaflet";
import { LMap, LTileLayer } from "vue2-leaflet";

export default {
  name: "MapTwoDots",
  components: {
    LMap,
    LTileLayer
  },
  data() {
    return {
      zoom: 10,
      center: latLng(55.751999, 37.617734),
      layerIndex: 0,
      layers: [
        {
          url: "https://vec01.maps.yandex.net/tiles?l=map&x={x}&y={y}&z={z}",
          subdomains: "1,2,3,4",
          attribution: '&copy; <a href="http://yandex.ru/copyright">Yandex</a>',
          crs: CRS.EPSG3395
        }
      ]
    };
  },
  computed: {
    layer() {
      return this.layers[this.layerIndex];
    }
  },
  methods: {
    tryThing() {
      // console.log(L);
      // var mymap = L.map("mapid").setView([50.27264, 7.26469], 13);
      // console.log(mymap);
      // L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png").addTo(mymap);
      // var control = L.Routing.control({
      //   waypoints: [
      //     L.latLng(38.7436056, -9.2304153),
      //     L.latLng(38.5334477, -0.1312811)
      //   ],
      //   router: new L.Routing.osrmv1({
      //     language: "en",
      //     profile: "car"
      //   }),
      //   geocoder: L.Control.Geocoder.nominatim({})
      // }).addTo(mymap);
    }
  },
  props: ["from", "to"]
};
</script>

<style lang="scss" scoped>
@import "~leaflet/dist/leaflet.css";
@import "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css";
</style>
