<template>
  <q-page class="flex">
    <q-table grid
      title="cultivados"
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

      <template v-slot:item="{ row }">
        <q-card style="min-height: 17rem; max-height: 17rem; min-width: 17rem; max-width: 17rem;">
          <q-card-section class="text-h5 q-pa-sm">
            {{ row.green_name }}
          </q-card-section>
          <q-card-section class="row justify-between q-pa-xs q-ma-sm">
            <span
              class="text-subtitle1"
              :style="`color: ${row['available'] ? '#2D7E23' : '#8B0000'}`"
            >
              {{ row['available'] ? 'disponível' : 'indisponível' }}
            </span>
          </q-card-section>
          <q-card-section v-for="item in keySet(row)" :key="item"
            class="row justify-between q-pa-xs q-ma-sm">
            <span class="text-subtitle1" style="color: #C3C3C3;"> {{ getProp(item) }} </span>
            <span class="text-subtitle2"> {{ row[item] }} </span>
          </q-card-section>
          <q-card-section class="row justify-center q-py-xs">
            <q-btn
              flat
              round
              size="sm"
              icon="add_circle"
              color="secondary"
              @click="editItem(row)"
            />
          </q-card-section>
        </q-card>
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
            name: 'green_name',
            required: true,
            label: 'nome',
            align: 'left',
            field: (row) => row.green_name,
            sortable: true,
          },
          {
            name: 'available',
            required: true,
            label: 'disponível',
            align: 'left',
            field: (row) => row.available,
            sortable: true,
          },
          {
            name: 'deadline',
            required: false,
            label: 'prazo',
            align: 'left',
            field: (row) => row.deadline,
            sortable: true,
          },
          {
            name: 'picked',
            required: false,
            label: 'colhido em',
            align: 'left',
            field: (row) => row.picked,
            sortable: true,
          },
          {
            name: 'producer',
            required: true,
            label: 'produtor',
            align: 'left',
            field: (row) => row.producer,
            sortable: true,
          },
          {
            name: 'price',
            required: true,
            label: 'preço',
            align: 'left',
            field: (row) => row.price,
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
    keySet(row) {
      const filterKeys = ['id', 'available', 'green_name', 'deadline', 'producer_id'];
      return Object.keys(row).filter((key) => !filterKeys.some((k) => k === key));
    },

    getProp(row) {
      switch (row) {
        case 'picked':
          return 'colhido em';
        case 'price':
          return 'preço';
        case 'producer':
          return 'produtor';
        default:
          return '';
      }
    },

    async searchData() {
      try {
        const response = await this.$http.get('/green/');
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
div >>> .q-table__grid-content {
  display: flex;
  justify-content: space-evenly;
}
</style>
