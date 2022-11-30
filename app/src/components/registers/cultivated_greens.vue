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
          v-if="!isPurchaser"
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
          <q-card-section v-for="item in keySet(row, true)" :key="item"
            class="row justify-between q-pa-xs q-ma-sm">
            <span class="text-subtitle1" style="color: #C3C3C3;"> {{ getProp(item) }} </span>
            <span class="text-subtitle2"> {{ getValue(row, item) }} </span>
          </q-card-section>
          <q-card-section class="row justify-center q-py-xs">
            <q-btn
              flat
              round
              size="sm"
              :icon="storage.getUser.id === 4 ? 'add_circle' : 'edit'"
              color="secondary"
              @click="editItem(row)"
            />
          </q-card-section>
        </q-card>
      </template>
    </q-table>
    <q-dialog v-model="edit">
      <q-card>
        <q-img v-if="edited.id" src="~assets/salsinha.webp" />
        <q-img v-else src="~assets/upload.png" />
        <q-btn
          flat
          icon="close"
          color="white"
          @click="edit = false;"
          class="absolute"
          style="right: 0;"
        />

        <q-card-section>
          <q-btn
            fab
            size="md"
            color="primary"
            icon="place"
            class="absolute"
            style="top: 0; right: 12px; transform: translateY(-50%);"
          />

          <div class="row no-wrap items-center">
            <div class="col text-h6 ellipsis">
              {{ edited.green_name }}
            </div>
            <div class="col-auto text-grey text-caption q-pt-md row no-wrap items-center">
              <q-icon name="place" />
              1,25km
              <!-- value must calculate the distance from real location to the producer -->
              <!-- just a sample here -->
            </div>
          </div>
        </q-card-section>

        <q-card-section class="row q-pt-none justify-between">
          <q-checkbox v-model="edited.available" label="disponível" />
          <q-input v-model="edited.green_name"
            label="nome"
            dense
            outlined
            stack-label
            class="col-xs-6 q-pa-sm"
          />
          <q-select
            v-model="edited.producer_id"
            label="produtor"
            dense
            outlined
            stack-label
            :options="producers"
            option-label="name"
            option-value="id"
            emit-value
            map-options
            class="col-xs-6 q-pa-sm"
          />
          <q-input v-model="edited.price"
            label="preço"
            dense
            outlined
            stack-label
            prefix="R$"
            mask="#.##"
            fill-mask="0"
            reverse-fill-mask
            class="col-xs-6 q-pa-sm"
          />
          <q-input v-model="edited.picked"
            label="colhido em"
            dense
            outlined
            stack-label
            mask="##-##-## ##:##"
            class="col-xs-6 q-pa-sm"
          >
            <template v-slot:append>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                  <div class="q-gutter-md row items-start">
                    <q-date v-model="edited.picked" mask="DD-MM-YY HH:mm" color="primary" />
                    <q-time
                      v-model="edited.picked"
                      format24h
                      mask="DD-MM-YY HH:mm"
                      color="primary"
                    />
                  </div>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
          <q-input v-model="edited.deadline"
            label="previsão colheita"
            dense
            outlined
            stack-label
            mask="##-##-## ##:##"
            class="col-xs-6 q-pa-sm"
          >
            <template v-slot:append>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                  <div class="q-gutter-md row items-start">
                    <q-date v-model="edited.deadline" mask="DD-MM-YY HH:mm" color="primary" />
                    <q-time
                      v-model="edited.deadline"
                      format24h
                      mask="DD-MM-YY HH:mm"
                      color="primary"
                    />
                  </div>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </q-card-section>

        <q-separator />

        <q-card-actions>
          <q-space />
          <div v-if="isPurchaser">
            <q-btn flat round icon="attach_money" />
            <q-btn flat color="primary">comprar</q-btn>
          </div>
          <div v-else>
            <q-btn flat color="red" @click="edit = false;">cancelar</q-btn>
            <q-btn flat color="green" @click="saveItem">salvar</q-btn>
          </div>
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';
import { useUserStore } from 'stores/user';

export default defineComponent({
  name: 'RegisterGreens',

  props: {},

  computed: {
    isPurchaser() {
      return this.storage.getUser.user === 'purchaser';
    },
  },

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
      storage: useUserStore(),
      producers: [],
    };
  },

  async mounted() {
    const response = await this.$http.get('/producer/');
    this.producers = response.producers;
    await this.searchData();
  },

  methods: {
    keySet(row, filter) {
      const mandatory = ['id', 'producer_id'];
      const filterKeys = ['available', 'green_name', 'deadline'];
      filterKeys.push(...mandatory);
      const keys = Object.keys(row);
      return filter
        ? keys.filter((key) => !filterKeys.some((k) => k === key))
        : keys.filter((key) => !mandatory.some((k) => k === key));
    },

    getProp(row) {
      switch (row) {
        case 'green_name':
          return 'nome';
        case 'deadline':
          return 'previsão de colheita';
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

    getValue(object, key) {
      if (key === 'price') {
        return `R$ ${object[key]}`;
      }
      return object[key];
    },

    async searchData() {
      try {
        const response = await this.$http.get('/green/');
        this.table.items = [];
        this.table.items = response.greens;
      } catch (e) {
        this.$q.notify({ type: 'error', message: 'erro ao carregar os alimentos...' });
      } finally {
        this.table.loading = false;
      }
    },

    editItem(item) {
      if (!item) {
        item = {
          available: null,
          green_name: null,
          producer_id: null,
          price: null,
          picked: null,
          deadline: null,
        };
      }
      this.edited = JSON.parse(JSON.stringify(item));
      this.edit = true;
    },

    async saveItem() {
      this.edited.picked = this.edited.picked === '' ? null : this.edited.picked;
      this.edited.deadline = this.edited.deadline === '' ? null : this.edited.deadline;

      await this.$http.post('/green/', { ...this.edited });
      this.$q.notify({ type: 'info', message: 'cultivados registrados!' });

      await this.searchData();
      this.edit = false;
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
