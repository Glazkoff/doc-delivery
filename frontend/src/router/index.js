import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Customer from "../views/Customer.vue";
import Courier from "../views/Courier.vue";
import Auth from "../views/Auth.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    children: [
      {
        path: "auth",
        name: "Auth",
        component: Auth
      },
      {
        path: "customer",
        name: "Customer",
        component: Customer,
        children: [
          // TODO: add components
          {
            path: ""
            // name: "Auth",
            // component: Auth
          },
          {
            path: "orders"
            // name: "Auth",
            // component: Auth
          },
          {
            path: "order_delivery"
            // name: "Auth",
            // component: Auth
          }
        ]
      },
      {
        path: "courier",
        name: "Courier",
        component: Courier
      }
    ]
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
