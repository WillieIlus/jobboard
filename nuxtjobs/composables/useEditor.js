import { ref } from 'vue'
import { Editor } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'

export default function useEditor() {
  const editor = ref(null)

  const createEditor = () => {
    editor.value = new Editor({
      extensions: [
        StarterKit
      ]  
    })
  }

  return { editor, createEditor }
}