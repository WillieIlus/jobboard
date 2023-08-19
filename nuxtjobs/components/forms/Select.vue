<template>
  <label class="text-lg font-semibold p-3 text-gray-700" v-if="label" :for="uuid">
    {{ label }}</label>
  <div class="mt-2">
    <select id="{{ label }}" name=" {{ label }}" autocomplete="{{ label }}"
      class="block min-w-full rounded-md border-2 p-3 text-gray-900 shadow-inner  focus:ring-indigo-600" v-bind="{
        ...$attrs,
        onChange: ($event) => { $emit('update:modelValue', $event.target.value) }
      }" :value="modelValue" :id="uuid" :aria-describedby="error ? `${uuid}-error` : null"
      :aria-invalid="error ? true : false" :class="{ error }">
      <option v-for="option in options" :value="option" :key="option" :selected="option === modelValue">
        {{ option }}
      </option>
    </select>
    <FormsErrorMessage v-if="error" :id="`${uuid}-error`">
      {{ error }}
    </FormsErrorMessage>
  </div>
</template>

<script>
export default {
  props: {
    options: {
      type: Array,
      required: true
    },
    label: {
      type: String,
      default: ""
    },
    error: {
      type: String,
      default: ""
    },
    modelValue: {
      type: [String, Number]
    }
  },
}
</script>
