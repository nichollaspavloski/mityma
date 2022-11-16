<template>
  <q-page class="flex">
    <q-table title="produtor"
      :loading="table.loading"
      :columns="table.headers"
      :rows="table.items"
      no-data-label="sem dados disponíveis"
      separator="vertical"
      class="fit q-mx-md q-mt-md"
    >
      <template v-slot:top>
        <div class="col-2 q-table__title">produtor</div>
        <q-space />
        <q-btn
          label="registrar"
          size="small"
          color="secondary"
          outline
          @click="editItem()">
        </q-btn>
      </template>

      <template v-slot:no-data="{ icon, message }">
        <div class="full-width row flex-center text-accent q-gutter-sm">
          <span> {{ message }} </span>
          <q-icon size="2em" :name="icon" />
        </div>
      </template>

      <template v-slot:body-cell-actions="{ row }">
        <div class="row justify-around">
          <q-btn small flat color="primary" icon="edit" @click="editItem(row)" />
          <q-btn small flat color="secondary" icon="delete" @click="deleteItem(row)" />
        </div>
      </template>
    </q-table>

    <q-dialog v-model="edit">
      <q-card style="width: 450px; height: 450px;">
        <q-card-section class="row justify-center">
          <q-avatar size="150px" color="secondary" text-color="white" icon="person_outline" />
        </q-card-section>
        <q-card-section>
          <div class="row wrap items-center justify-between">
            <q-input v-model="edited.name"
              label="nome"
              dense
              outlined
              stack-label
              class="col-6"
            />
            <q-input v-model="edited.login"
              label="login"
              dense
              outlined
              stack-label
              class="col-6"
            />
          </div>
        </q-card-section>
        <q-card-section>
          <div class="row wrap items-center justify-between">
            <q-toggle v-model="edited.active"
              color="primary"
              label="ativo"
              left-label
            />
            <q-toggle v-model="edited.is_mentor"
              color="primary"
              label="instrutor"
              left-label
            />
            <q-toggle v-model="edited.show_location"
              color="primary"
              label="mostrar localização"
              left-label
            />
          </div>
        </q-card-section>
        <q-card-section class="row no-wrap items-center">
          <q-btn :label="formattedLocation"
            small
            color="primary"
            class="col-grow"
            @click="location = true"
          />
        </q-card-section>
        <q-separator />
        <q-card-actions align="right">
          <q-btn v-close-popup flat outline color="green" label="salvar" @click="saveItem()" />
          <q-btn v-close-popup flat outline color="red" label="cancelar" />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <q-dialog v-model="location">
      <q-card>
        <q-card-section class="text-h6 ellipsis">
          location
        </q-card-section>
        <q-card-section class="row justify-between">
          <q-input v-model="edited.location_obj.street"
            label="rua"
            dense
            outlined
            stack-label
            class="col-10"
          />
          <q-input v-model="edited.location_obj.no"
            label="nº"
            dense
            outlined
            stack-label
            class="col-2"
          />
          <q-input v-model="edited.location_obj.zip_code"
            label="cep"
            dense
            outlined
            stack-label
            class="col-4"
          />
          <q-input v-model="edited.location_obj.city"
            label="cidade"
            dense
            outlined
            stack-label
            class="col-4"
          />
          <q-input v-model="edited.location_obj.state"
            label="estado"
            dense
            outlined
            stack-label
            class="col-4"
          />
        </q-card-section>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'RegisterProdutor',

  props: {},

  computed: {
    formattedLocation() {
      if (!this.edited.location_obj.street) {
        return 'insira um endereço';
      }

      const location = this.edited.location_obj;
      return `${location.street || ''}, ${location.no || ''} - ${location.city || ''} [${location.state || ''}]`;
    },
  },

  data() {
    return {
      table: {
        headers: [
          {
            name: 'name',
            required: true,
            label: 'nome',
            align: 'left',
            field: (row) => row.name,
            sortable: true,
          },
          {
            name: 'location',
            required: true,
            label: 'endereço',
            align: 'left',
            field: (row) => row.location,
            sortable: true,
          },
          {
            name: 'login',
            required: true,
            label: 'login',
            align: 'left',
            field: (row) => row.login,
            sortable: true,
          },
          {
            name: 'created_at',
            required: true,
            label: 'criado em',
            align: 'left',
            field: (row) => row.created_at,
            sortable: true,
          },
          {
            name: 'actions',
            required: false,
            label: 'ações',
            align: 'center',
            format: (val) => `${val}`,
            sortable: false,
          },
        ],
        items: [],
        search: '',
        loading: true,
      },
      edit: false,
      edited: undefined,
      location: false,
    };
  },

  async mounted() {
    await this.searchData();
  },

  methods: {
    async searchData() {
      try {
        const response = await this.$http.get('/producer/');
        this.table.items = response.producers;
      } catch (e) {
        this.$q.notify({ type: 'error', message: 'erro ao carregar os produtores...' });
      } finally {
        this.table.loading = false;
      }
    },

    editItem(item) {
      if (!item) {
        item = {};
        item.location_obj = {};
      }
      this.edited = Object.assign(item, {});
      this.edit = true;
    },

    async saveItem() {
      await this.$http.post('/producer/', { ...this.edited });
      this.$q.notify({ type: 'info', message: 'dados do produtor salvo' });
      await this.searchData();
    },

    async deleteItem(item) {
      await this.$http.delete(`/producer/${item.id}`);
      this.$q.notify({ type: 'info', message: 'produtor removido com sucesso' });
      await this.searchData();
    },
  },
});
</script>
<style scoped>
</style>
