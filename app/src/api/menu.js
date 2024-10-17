const menu = [
  {
    title: 'home',
    icon: 'mdi-home-outline',
    route: '/home',
    permission: true,
    permissions: [],
  },
  {
    title: 'produtor',
    icon: 'person_outline',
    route: '/registers/producer',
    permissions: ['producer'],
  },
  {
    title: 'hortas',
    icon: 'mdi-sprout-outline',
    permissions: [],
  },
  {
    title: 'catálogo',
    icon: 'mdi-food-apple-outline',
    route: '/registers/greens',
    permissions: ['producer', 'purchaser'],
  },
  {
    title: 'banco',
    icon: 'mdi-seed-outline',
    permissions: ['producer'],
  },
];

export default menu;
