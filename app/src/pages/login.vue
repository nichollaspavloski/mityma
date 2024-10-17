<template>
  <div class="fullscreen q-pa-none flex flex-center">
    <q-layout view="lHh lpr lFf" class="container fit default-font">
      <div class="row" style="height: 100vh; overflow-y: hidden">
        <div class="col-4">
          <q-card flat style="height: 100%;">
            <!-- logo -->
            <q-card-section class="flex items-center justify-center" style="height: 25%;">
              <div class="col-3">
                <img
                  alt="mityma logo"
                  src="~assets/seeding.svg"
                  style="width: 100px; height: 100px;"
                />
              </div>
            </q-card-section>
            <!-- inputs -->
            <q-card-actions class="q-pa-lg" style="height: 50%;">
              <div class="col-6 full-width">
                <q-input v-model="login" dense label="Usuário">
                  <template v-slot:prepend>
                    <q-icon name="person" color="black"/>
                  </template>
                </q-input>
                <q-input
                  v-model="password"
                  :type="'password'"
                  dense
                  label="Senha"
                  @keyup.enter="validateUser"
                  class="q-py-md"
                >
                  <template v-slot:prepend>
                    <q-icon name="lock" color="black"/>
                  </template>
                </q-input>
                <div class="flex row justify-between q-pb-md">
                  <q-checkbox
                    v-model="keepAlive"
                    size="sm"
                    dense
                    label="Mantenha-me logado"
                  />
                  <span href="https://google.com" style="color: #2d7e23;">Esqueceu sua senha?</span>
                </div>
                <q-btn
                  color="primary"
                  text-color="white"
                  label="Login"
                  dense
                  @click="validateUser"
                  class="full-width button-font"
                >
                </q-btn>
              </div>
            </q-card-actions>
          </q-card>
        </div>
        <div class="col-8">
          <img
            alt="login"
            src="~assets/login.png"
            style="height: 100%; width: 100%; object-fit: cover;"
          >
        </div>
      </div>
    </q-layout>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { useUserStore } from 'stores/user';

export default defineComponent({
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Login',
  data() {
    return {
      login: '',
      password: '',
      keepAlive: false,
      validUsers: {
        admin: {
          login: 'admin',
          pw: 'admin',
        },
        produtor: {
          login: 'produtor',
          pw: 'alimento',
        },
        mentor: {
          login: 'mentor',
          pw: 'mentoria',
        },
        consumidor: {
          login: 'consumidor',
          pw: 'consumo',
        },
      },
      store: useUserStore(),
    };
  },
  methods: {
    validateUser() {
      if (this.validUsers[this.login] && this.validUsers[this.login].pw === this.password) {
        const users = this.store.getUsers;
        const user = users.find((u) => u.user === this.login);
        this.store.setUser(user);
        this.$router.push('/');
      } else {
        this.$q.notify({ type: 'error', message: 'usuário/login inválidos...' });
      }
    },
  },
});
</script>

<style scoped>
.button-font {
  text-transform: none;
  font-weight: 600;
  letter-spacing: 2px;
  font-size: 20px;
}
</style>
