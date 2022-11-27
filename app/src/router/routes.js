const routes = [
  {
    path: '/',
    component: () => import('layouts/main_layout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: '/registers/producer', component: () => import('src/components/registers/producer.vue') },
      { path: '/home', component: () => import('pages/IndexPage.vue') },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
