<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated height-hint="80">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="mdi-home-outline"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          MITYMA
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <q-item-label header>
          menu
        </q-item-label>

        <MenuItem
          v-for="link in menus"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
/* eslint-disable global-require */
import { defineComponent } from 'vue';
import MenuItem from 'components/menu_item.vue';
import menu from '../api/menu.js';

export default defineComponent({
  name: 'MainLayout',

  components: { MenuItem },

  data() {
    return {
      menus: menu,
      leftDrawerOpen: true,
    };
  },

  methods: {
    toggleLeftDrawer() {
      this.leftDrawerOpen = !this.leftDrawerOpen;
    },
  },
});
</script>
