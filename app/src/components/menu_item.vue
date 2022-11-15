<template>
  <q-item
    clickable
    tag="a"
  >
    <q-item-section v-if="icon" avatar>
      <q-icon :name="icon" color="primary"/>
    </q-item-section>

    <q-item-section>
      <q-item-label>{{ title }}</q-item-label>
    </q-item-section>
  </q-item>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'MenuItem',
  props: {
    title: {
      type: String,
      required: true,
    },

    caption: {
      type: String,
      default: '',
    },

    icon: {
      type: String,
      default: '',
    },
  },
});
</script>
