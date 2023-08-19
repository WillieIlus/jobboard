<template>
  <div>
    <div>
      <!-- Start Section-->
      <section class="relative md:py-24 py-16 bg-gray-50 dark:bg-slate-800">
        <div class="container">
          <div class="grid lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-[30px]">
            <div v-for="company in companies" :key="company.id" class="group bg-white dark:bg-slate-900 p-6 rounded shadow dark:shadow-gray-800 hover:shadow-md dark:hover:shadow-gray-700 border-4 border-white dark:border-slate-900 hover:border-b-indigo-600 dark:hover:border-b-indigo-600 text-center duration-500 ease-in-out">
              <img :src="company.logoUrl" class="h-16 w-16 mx-auto p-3 rounded-full bg-gray-50 dark:bg-slate-800 shadow-md dark:shadow-gray-800" alt="">
              <div class="content mt-3">
                <span class="text-lg font-semibold group-hover:text-indigo-600 transition duration-500 block">{{ company.name }}</span>
                <span class="text-base text-slate-400 block"><i class="uil uil-map-marker text-indigo-600 mr-1"></i> {{ company.location }}</span>
                <button @click="showContact(company)" class="text-indigo-600 hover:underline mt-2">Contact</button>
                <div v-if="showCompanyContact && selectedCompanyId === company.id" class="contact-details">
                  <a :href="`mailto:${company.email}`" class="contact-email">
                    <EnvelopeIcon class="contact-icon" />
                    {{ company.email }}
                  </a>
                  <a :href="`tel:${company.telephone}`" class="contact-telephone">
                    <PhoneIcon class="contact-icon" />
                    {{ company.telephone }}
                  </a>
                </div>
              </div>
            </div>
          </div>
          <!--end grid-->
        </div>
        <!--end container-->
      </section>
      <!--end section-->
    </div>
  </div>
</template>

<script setup>
import { EnvelopeIcon } from '@heroicons/vue/20/solid'

const companies = [
  {
    name: 'Company A',
    industry: 'Technology',
    location: 'New York',
    email: 'contact@companya.com',
    logoUrl: 'http://pigment.github.io/fake-logos/logos/medium/color/greens-food-suppliers.png',
    id: 1,
  },
  {
    name: 'Company B',
    industry: 'Technology',
    location: 'San Francisco',
    email: 'contact@company.com',
    logoUrl: 'http://pigment.github.io/fake-logos/logos/medium/color/auto-speed.png',
    id: 2,
  },
  {
    name: 'Company C',
    industry: 'Technology',
    location: 'Los Angeles',
    email: 'contact@companybb.com',
    logoUrl: 'http://pigment.github.io/fake-logos/logos/medium/color/crofts-accountants.png',
    id: 3,
  },
  {
    name: 'Company D',
    industry: 'Technology',
    location: 'Chicago',
    email: 'emal@co@gma.com',
    logoUrl: 'http://pigment.github.io/fake-logos/logos/medium/color/bee.png',
    id: 4,
  },
  {
    name: 'Company E',
    industry: 'Technology',
    location: 'Seattle',
    email: 'email@gma.com',
    logoUrl: 'http://pigment.github.io/fake-logos/logos/medium/color/bee.png',
    id: 5,
    
  }
]

let showCompanyContact = false;
let selectedCompanyId = null;

function showContact(company) {
  showCompanyContact = !showCompanyContact;
  selectedCompanyId = company.id;
}
</script>
