import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TV from '../components/TV.vue'
import TVScreen from "@/components/TVScreen";
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    redirect: '/tv/1'
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/tv',
    name: 'tv',
    component: TV,
    redirect: '/tv/1',
    children: [
        {
          path: ':page',
          name: 'tvscreen',
          component: TVScreen,
          props: route=> ({ id: parseInt(route.params.page) }),
          children: [
          {
         path: ':subpage',
        name: 'tvscreen.subpage',
        component: TVScreen,
        props: route=> ({id2: parseInt(route.params.subpage)})
      }
    ]
  }
    ]
  },
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
