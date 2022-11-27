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
        <div class="col-2 q-table__title">cultivados</div>
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
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'RegisterGreens',

  props: {},

  computed: {},

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
        ],
        items: [],
        search: '',
        loading: true,
      },
      edit: false,
      edited: undefined,
    };
  },

  async mounted() {
    await this.searchData();
  },

  methods: {
    async searchData() {
      try {
        // TODO implement the endpoint
        // const response = await this.$http.get('/greens/');
        this.table.items = response.greens;
      } catch (e) {
        this.$q.notify({ type: 'error', message: 'erro ao carregar os alimentos...' });
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
      // TODO implement the endpoint
      // await this.$http.post('/greens/', { ...this.edited });
      this.$q.notify({ type: 'info', message: '' });
      await this.searchData();
    },

    async deleteItem(item) {
      // TODO implement the endpoint
      // await this.$http.delete(`/greens/${item.id}`);
      this.$q.notify({ type: 'info', message: '' });
      await this.searchData();
    },
  },
});
</script>
<style scoped>
</style>
