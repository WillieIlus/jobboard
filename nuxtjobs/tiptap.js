import { Editor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.component('EditorContent', EditorContent)
  nuxtApp.vueApp.component('Editor', Editor)
})