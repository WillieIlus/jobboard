<template>
  <label class="text-lg font-semibold p-4 text-gray-700">{{ label }}</label>
  <input
  class="field min-w-full border-2 border-slate-200 rounded-md p-3 shadow-inner focus:border-gray-400"
   v-bind="
  {
    ...$attrs,
    onInput: updateValue
  }" :id="uuid" :value="modelValue" :placeholder="label" :aria-describedby="error ? `${uuid}-error` : null"
  :aria-invalid="error ? true : false" :class="{ error }" @input="$emit('update:modelValue', $event.target.value)"/>
  <FormsErrorMessage v-if="error" :id="`${uuid}-error`">
    {{ error }}
  </FormsErrorMessage>
</template>

<script setup>


const props = defineProps({
  label: {
    type: String,
    default: ""
  },
  error: {
    type: String,
    default: ""
  },
  modelValue: {
    type: [String, Number],
    default: ""
  }
})
</script>
