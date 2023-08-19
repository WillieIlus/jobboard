<template>
  <p aria-live="assertive" class="errorMessage" :id="id">
    <slot>

    </slot>
  </p>
</template>

<script>
export default {
  props: {
    id: {
      type: [String, Number],
      required: true
    }
  }
}
</script>
