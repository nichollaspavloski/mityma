const routes = [
  {
    path: '/',
    component: () => import('layouts/main_layout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: '/home', component: () => import('pages/IndexPage.vue') },
      { path: '/registers/producer', component: () => import('pages/registers/producer.vue') },
      { path: '/registers/greens', component: () => import('pages/registers/cultivated_greens.vue') },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
  {
    path: '/login',
    meta: { growable: true },
    component: () => import('pages/login.vue'),
  },
];

export default routes;
