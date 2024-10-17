<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated style="height: 5rem">
      <q-toolbar style="height: 100%">
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
        <q-space />
        <q-btn round size="sm" color="white">
          <q-avatar icon="person_outline" text-color="primary">
            <q-menu anchor="bottom middle" self="top middle">
              <q-list dense style="min-width: 30px">
                <q-item
                  clickable
                  v-close-popup
                  v-for="user in users"
                  :key="user.id"
                  @click="setUser(user)"
                >
                  <q-item-section>{{ user.user }}</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-avatar>
        </q-btn>
        <span class="text-h6 q-ml-sm"> {{ !getUser ? 'no user' : getUser }} </span>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list v-if="menus.length > 0">
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
import { useUserStore } from 'stores/user';
import menu from '../api/menu.js';

export default defineComponent({
  name: 'MainLayout',

  components: { MenuItem },

  data() {
    return {
      menu,
      menus: [],
      leftDrawerOpen: true,
      store: useUserStore(),
      users: [],
    };
  },

  computed: {
    getUser() {
      return this.store.getUser.user;
    },
  },

  mounted() {
    this.users = this.store.getUsers;
    this.menus = this.mountMenu();
  },

  methods: {
    toggleLeftDrawer() {
      this.leftDrawerOpen = !this.leftDrawerOpen;
    },
    setUser(user) {
      this.store.setUser(user);
      this.menus = this.mountMenu();
    },
    mountMenu() {
      const user = this.getUser;
      return this.menu.filter(
        (mn) => user === 'admin'
          || mn.permission
          || mn.permissions.some((p) => (user === p || (user === 'mentor' && p === 'producer'))),
      );
    },
  },
});
</script>
