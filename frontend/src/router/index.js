import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Customer from "../views/Customer.vue";
import Courier from "../views/Courier.vue";
import Auth from "../views/Auth.vue";
import CustomerMain from "../components/customer/CustomerMain.vue";
import CustomerOrders from "../components/customer/CustomerOrders.vue";
import CustomerOrderDelivery from "../components/customer/CustomerOrderDelivery.vue";
import CourierActiveOrders from "../components/courier/CourierActiveOrders.vue";
import CourierArchieveOrders from "../components/courier/CourierArchieveOrders.vue";
import CourierSalary from "../components/courier/CourierSalary.vue";
import CourierSpecificOrder from "../components/courier/CourierSpecificOrder.vue";

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
        path: "",
        // name: "Customer",
        component: Customer,
        children: [
          {
            path: "/",
            name: "CustomerMain",
            component: CustomerMain
          },
          {
            path: "orders",
            name: "CustomerOrders",
            component: CustomerOrders
          },
          {
            path: "order-delivery",
            name: "CustomerOrderDelivery",
            component: CustomerOrderDelivery
          }
        ]
      },
      {
        path: "courier",
        component: Courier,
        children: [
          {
            path: "/",
            name: "CourierActiveOrders",
            component: CourierActiveOrders
          },
          {
            path: "order/:id",
            name: "CourierSpecificOrder",
            component: CourierSpecificOrder
          },
          {
            path: "archieve-orders",
            name: "CourierArchieveOrders",
            component: CourierArchieveOrders
          },
          {
            path: "salary",
            name: "CourierSalary",
            component: CourierSalary
          }
        ]
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
