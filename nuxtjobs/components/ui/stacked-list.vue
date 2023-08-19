<template>

      <div class="bg-white py-24 sm:py-32">
        <div class="mx-auto max-w-7xl px-6 lg:px-8">
          <div class="mx-auto max-w-2xl lg:mx-0">
            <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Job Vacancies</h2>
            <p class="mt-2 text-lg leading-8 text-gray-600">Check out our latest job openings.</p>
          </div>
          <div class="mt-10 space-y-16">
            
            <article v-for="job in jobs" :key="job.id" class="flex flex-col">
              <BasicCard>
              <div class="flex items-center gap-x-4 text-xs">
                <time :datetime="job.datetime" class="text-gray-500">{{ job.date }}</time>
                <span class="relative z-10 rounded-full bg-gray-50 px-3 py-1.5 font-medium text-gray-600">{{
                  job.category.title }}</span>
              </div>
              <div class="group relative">
                <h3 class="mt-3 text-lg font-semibold leading-6 text-gray-900 group-hover:text-gray-600">
                  <a :href="job.href">
                    <span class="absolute inset-0" />
                    {{ job.title }}
                  </a>
                </h3>
                <p class="mt-5 line-clamp-3 text-sm leading-6 text-gray-600">{{ job.description }}</p>
              </div>
              <div class="relative mt-8 flex items-center gap-x-4">
                <img :src="job.companyLogo" alt="" class="h-10 w-10 rounded-full bg-gray-50" />
                <div class="text-sm leading-6">
                  <p class="font-semibold text-gray-900">
                    <a :href="job.companyUrl">
                      <span class="absolute inset-0" />
                      {{ job.companyName }}
                    </a>
                  </p>
                  <p class="text-gray-600">{{ job.location }}</p>
                </div>
              </div>
            </BasicCard>
            </article>
          </div>
        </div>
      </div>
  
</template>

<script setup>
const jobs = [
  {
    id: 1,
    title: 'Backend Developer',
    href: '#',
    description:
      'We are looking for a skilled Backend Developer to join our team and help us build and maintain robust web applications.',
    date: 'Jul 18, 2023',
    datetime: '2023-07-18',
    category: { title: 'Engineering', href: '#' },
    companyLogo:
      'https://example.com/path-to-your-company-logo.png',
    companyName: 'Your Company Name',
    companyUrl: 'https://www.yourcompanywebsite.com/',
    location: 'City, Country',
  },
  {
    id: 2,
    title: 'Frontend Developer',
    href: '#',
    description:
      'We are looking for a skilled Frontend Developer to join our team and help us build and maintain robust web applications and more details to add here.',
    date: 'Jul 18, 2023',
    datetime: '2023-07-18',
    category: { title: 'Engineering', href: '#' },
    companyLogo:
      'https://example.com/path-to-your-company-logo.png',
    companyName: 'Your Company Name',
    companyUrl: 'https://www.yourcompanywebsite.com/',
    location: 'City, Country',
  },
  {
    id: 6,
    title: 'UX Designer',
    href: '#',
    description:
      'We are looking for a skilled UX Designer to join our team and help us build and maintain robust web applications and more details to add here.',
    date: 'Jul 18, 2023',
    datetime: '2023-07-18',
    category: { title: 'Design', href: '#' },
    companyLogo:
      'https://example.com/path-to-your-company-logo.png',
    companyName: 'Your Company Name',
    companyUrl: 'https://www.yourcompanywebsite.com/',
    location: 'City, Country',
  },


];
</script>
