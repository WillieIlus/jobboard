<script setup>
import { ref, watch } from 'vue'
import StarterKit from '@tiptap/starter-kit'
import { Editor, EditorContent } from '@tiptap/vue-3'

const props = defineProps({
  modelValue: {
    type: String,
    default: '',
  },
})

const emit = defineEmits(['update:modelValue']) 

const editor = ref(null)

watch(() => props.modelValue, (newValue) => {
  if (editor.value.getHTML() === newValue) return

  editor.value.commands.setContent(newValue, false) 
})

onMounted(() => {
  editor.value = new Editor({
    extensions: [
      StarterKit,
    ],
    content: props.modelValue,
    onUpdate: () => {
      emit('update:modelValue', editor.value.getHTML())
    }
  })
})

onBeforeUnmount(() => {
  editor.value.destroy()
})
</script>

<template>
  <editor-content :editor="editor" />
</template>