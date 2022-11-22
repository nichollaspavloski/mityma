const menu = [
  {
    title: 'home',
    icon: 'mdi-home-outline',
    route: '/home',
    permission: true,
  },
  {
    title: 'produtor',
    icon: 'person_outline',
    route: '/registers/produtor',
    permissions: ['producer'],
  },
  {
    title: 'hortas',
    icon: 'mdi-sprout-outline',
  },
  {
    title: 'catálogo',
    icon: 'mdi-food-apple-outline',
    permissions: ['producer', 'purchaser'],
  },
  {
    title: 'banco',
    icon: 'mdi-seed-outline',
    permissions: ['producer'],
  },
];

export default menu;
