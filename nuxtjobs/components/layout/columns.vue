<template>
  <div class="py-6">
    <div class="mx-auto max-w-3xl sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-12 lg:gap-8 lg:px-8">
      <main class="lg:col-span-9 xl:col-span-8">
        <slot name="main-column">This is the main column</slot>
      </main>
      <aside class="hidden lg:col-span-3 xl:col-span-4 xl:block">
        <div class="sticky top-6 space-y-4">
          <slot name="right-column">This is the right column</slot>
        </div>
      </aside>
    </div>
  </div>
</template>