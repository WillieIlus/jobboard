<template>
  <!-- Start Hero -->
  <section
    class="relative table w-full py-36 lg:py-44 bg-[url('https://images.unsplash.com/photo-1531482615713-2afd69097998?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80')] bg-no-repeat bg-center"
    style="z-index: 0;"
  >
    <div class="absolute inset-0 bg-blue-800 opacity-80" style="z-index: -1;"></div>
    <!-- Set z-index to -1 to place this element below other layers -->

    <div class="container mx-auto">
      <div class="grid grid-cols-1 pb-8 text-center mt-12">
        <h3 class="md:text-4xl text-3xl md:leading-normal tracking-wide leading-normal font-medium text-white"
          style="z-index: 0;"
        >Company List</h3>
        <BreadCrumbs style="z-index: 0;" />
      </div>
      <!--end grid-->
    </div>
  </section>
  <!-- End Hero -->
</template>

<script setup>
</script>
