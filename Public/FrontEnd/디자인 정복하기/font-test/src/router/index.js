import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SCDream from '../views/SCDream.vue'
import BlackHanSans from '../views/BlackHanSans'
import Mon from '../views/Mon'
import NotoSans from '../views/NotoSans'
import InkLipquid from '../views/InkLipquid'
import EnjoyStory from '../views/EnjoyStory'
import JUA from '../views/JUA'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/scdream',
    name: 'SCDream',
    component: SCDream
  },
  {
    path: '/blackhansans',
    name: 'BlackHanSans',
    component: BlackHanSans
  },
  {
    path: '/mon',
    name: 'Mon',
    component: Mon
  },
  {
    path: '/notosans',
    name: 'NotoSans',
    component: NotoSans
  },
  {
    path: '/inklipquid',
    name: 'InkLipquid',
    component: InkLipquid
  },
  {
    path: '/enjoystory',
    name: 'EnjoyStory',
    component: EnjoyStory
  },
  {
    path: '/jua',
    name: 'JUA',
    component: JUA
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
