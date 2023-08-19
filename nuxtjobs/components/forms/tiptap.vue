<template>
  <div class="toolbar">
    <label class="text-lg font-semibold p-4 text-gray-700">{{ label }}</label>
    <div v-if="editor">
          <div class="border border-gray-200 overflow-hidden rounded-md">
            <div class="w-full flex border-b border-gray-200 text-xl text-gray-600">
              <button v-for="command in commands" :key="command.name" @click="command.command"
                :class="{ 'active:bg-gray-50 text-white': command.isActive }"
                class="p-3 mr-1 outline-none focus:outline-none border-r border-gray-200 w-10 h-10 hover:text-indigo-500">
                <component :is="command.icon" class="" />
              </button>
            </div>
            <editor-content :editor="editor"/>
           
            <FormsErrorMessage v-if="error" :id="`${uuid}-error`">
              {{ error }}
            </FormsErrorMessage>
          </div>
        </div>
  </div>
</template>


<script setup>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import { Editor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import { isActive } from '@tiptap/core'
import {
  RiStrikethrough,
  RiBold,
  RiItalic,
  RiUnderline,
  RiHeading,
  RiListOrdered,
  RiListUnordered,
  RiGitMergeLine,
  RiArrowGoBackLine,
  RiArrowGoForwardLine
} from "vue-remix-icons"

import Document from '@tiptap/extension-document'
import Paragraph from '@tiptap/extension-paragraph'
import Text from '@tiptap/extension-text'
import Bold from '@tiptap/extension-bold'
import Italic from '@tiptap/extension-italic'
import Strike from '@tiptap/extension-strike'
import BulletList from '@tiptap/extension-bullet-list'
import ListItem from '@tiptap/extension-list-item'
import OrderedList from '@tiptap/extension-ordered-list'
import HorizontalRule from '@tiptap/extension-horizontal-rule'
import Underline from '@tiptap/extension-underline'
import Heading from '@tiptap/extension-heading'
import History from '@tiptap/extension-history'


const props = defineProps({
  label: {
    type: String,
    default: '',
  },
  error: {
    type: String,
    default: '',
  },
  modelValue: {
    type: [String, Number],
    default: '',
  },
});

const emit = defineEmits(['update:modelValue']);


const editor = ref(null)



watch(() => props.modelValue, (newValue) => {
  if (editor.value.getHTML() === newValue) return

  editor.value.commands.setContent(newValue, false)
})


const extensions = [
  Document,
  Paragraph,
  Text,
  Strike,
  ListItem,
  BulletList,
  OrderedList,
  HorizontalRule,
  Bold,
  Italic,
  Underline,
  Heading,
  History
]

const toggleStrike = () => {
  editor.value.chain().focus().toggleStrike().run()
}

const toggleBold = () => {
  editor.value.chain().focus().toggleBold().run()
}

const toggleItalic = () => {
  editor.value.chain().focus().toggleItalic().run()
}

const toggleUnderline = () => {
  editor.value.chain().focus().toggleUnderline().run()
}


const toggleOrderedList = () => {
  editor.value.chain().focus().toggleOrderedList().run()
}


const toggleBulletList = () => {
  editor.value.chain().focus().toggleBulletList().run()
}

const toggleHeading = () => {
  editor.value.chain().focus().toggleHeading({ level: 1 }).run()
}

const toggleHistory = () => {
  editor.value.chain().focus().toggleHistory().run()
}

const toggleHorizontalRule = () => {
  editor.value.chain().focus().toggleHorizontalRule().run()
}

const commands = ref([
  {
    name: 'bold',
    icon: RiBold,
    command: toggleBold,
    isActive: () => isActive('bold')(editor.value)
  },
  {
    name: 'italic',
    icon: RiItalic,
    command: toggleItalic,
    isActive: () => isActive('italic')(editor.value)
  },
  {
    name: 'orderedList',
    icon: RiListOrdered,
    command: toggleOrderedList,
    isActive: () => isActive('orderedList')(editor.value)
  },
  {
    name: 'unorderedList',
    icon: RiListUnordered,
    command: toggleBulletList,
    isActive: () => isActive('unorderedList')(editor.value)
  },
  {
    name: 'underline',
    icon: RiUnderline,
    command: toggleUnderline,
    isActive: () => isActive('underline')(editor.value)
  },
  {
    name: 'strike',
    icon: RiStrikethrough,
    command: toggleStrike,
    isActive: () => isActive('strike')(editor.value)
  },
  {
    name: 'heading',
    icon: RiHeading,
    command: toggleHeading,
    isActive: () => isActive('heading')(editor.value)
  },
  {
    name: 'horizontalRule',
    icon: RiGitMergeLine,
    command: toggleHorizontalRule,
    isActive: () => isActive('horizontalRule')(editor.value)
  },
  {
    name: 'undo',
    icon: RiArrowGoBackLine,
    command: toggleHistory,
    isActive: () => isActive('undo')(editor.value)
  },
  {
    name: 'redo',
    icon: RiArrowGoForwardLine,
    command: toggleHistory,
    isActive: () => isActive('redo')(editor.value)
  }
])



onMounted(() => {
  editor.value = new Editor({
    extensions: [
      StarterKit,
    ],
    content: props.modelValue,
    onUpdate() {
      let content = editor.value.getHTML();
      emit('update:modelValue', content);
    },
  })
})

onBeforeUnmount(() => {
  if (editor.value) {
    editor.value.destroy()
  }
})


</script>


<style>
.ProseMirror {
  >*+* {
    /* "field min-w-full border-2 border-slate-200 rounded-md p-3 shadow-inner focus:border-gray-400 h-24"/> */
    margin-top: 0.75em;
    box-shadow: inset 0 -1px 0 #eee;
    min-width: full;
    border: 2px solid #eee;
    border-radius: 0.375rem;
    padding: 0.75rem;
    outline: none;
    &:focus {
      border-color: #aaa;
    }
  }

  ul,
  ol {
    padding: 0 1rem;
  }
}

H1 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

H2 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.toolbar {
  border-bottom: 1px solid #eee;
  padding: 0.5rem;
}

.toolbar button {
  background: none;
  border: none;
  font-size: 18px;
  cursor: pointer;
  margin-right: 0.5rem;
  color: #aaa;
}

.toolbar button.is-active {
  color: black;
}

.editor {
  border: 1px solid #eee;
  border-bottom: none;
  padding: 0.5rem;
  height: 300px;
}
</style>