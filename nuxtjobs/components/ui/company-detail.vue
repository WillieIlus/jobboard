<template>
  <!-- Start -->
  <section class="relative md:py-24 py-16">
    <div class="container">
      <div class="grid md:grid-cols-12 grid-cols-1 gap-[30px]">
        <div class="lg:col-span-4 md:col-span-5">
          <div class="lg:-mt-[330px] -mt-[299px]" style="z-index: 3;">
            <div class="rounded-md bg-white dark:bg-slate-900 shadow dark:shadow-gray-800" style="z-index: 3;">
              <div class="text-center py-8 p-6 border-b border-gray-100 dark:border-gray-700">
                <img src="assets/images/client/circle-logo.png" class="h-24 w-24 p-4 shadow-md mx-auto rounded-full block"
                  alt="">
                <h5 class="mt-5 text-xl font-semibold mb-0">CircleCi</h5>
                <p class="text-slate-400 mb-0">Internet Services</p>
              </div>

              <div class="p-6">
                <h5 class="font-semibold">Company Details :</h5>
                <ul class="list-none mt-4">
                  <li class="flex mt-2 items-center font-medium"><i data-feather="map-pin"
                      class="h-4 w-4 text-amber-500 mr-3"></i><span class="text-slate-400 mr-3">Location :</span> San
                    Francisco</li>
                  <li class="flex mt-2 items-center font-medium"><i data-feather="link"
                      class="h-4 w-4 text-amber-500 mr-3"></i><span class="text-slate-400 mr-3">Comapny :</span>
                    circleci.com</li>
                  <li class="flex mt-2 items-center font-medium"><i data-feather="dollar-sign"
                      class="h-4 w-4 text-amber-500 mr-3"></i><span class="text-slate-400 mr-3">Revenue :</span> $ 5M /
                    Annual</li>
                  <li class="flex mt-2 items-center font-medium"><i data-feather="users"
                      class="h-4 w-4 text-amber-500 mr-3"></i><span class="text-slate-400 mr-3">No. of employees :</span>
                    200</li>
                </ul>

                <a href="page-job-apply.html"
                  class="btn bg-indigo-600 hover:bg-indigo-700 border-indigo-600 hover:border-indigo-700 text-white rounded-md mt-6">Apply
                  Now</a>
              </div>
            </div>
          </div>
        </div>

        <div class="lg:col-span-8 md:col-span-7">
          <h4 class="text-xl font-semibold">About us :</h4>
          <p class="text-slate-400 mt-4">Almost no business is immune from the need for quality software development. The
            act of building quality software, and shipping it quickly, has become the core engine of value creation in
            companies across all industries. CircleCI allows teams to rapidly release code they trust by automating the
            build, test, and delivery process. Thousands of leading companies, including Samsung, Ford Motor Company,
            Spotify, Lyft, Coinbase, PagerDuty, Stitch Fix, and BuzzFeed rely on CircleCI to accelerate delivery and
            improve quality.</p>
          <p class="text-slate-400 mt-4">CircleCI was named a Leader in cloud-native continuous integration by Forrester
            in 2021 and has been named to multiple Best DevOps Tools lists. CircleCI is the first CI/CD tool to become
            FedRAMP certified and processes more than 30 million builds each month across Linux, macOS, Docker and Windows
            build environments.</p>
          <p class="text-slate-400 mt-4">Founded in 2011 and headquartered in San Francisco with a global remote
            workforce, CircleCI is venture-backed by Scale Venture Partners, Threshold Ventures (formerly DFJ), Baseline
            Ventures, Top Tier Capital, Industry Ventures, Heavybit, Harrison Metal Capital, Owl Rock Capital Partners,
            and NextEquity Partners.</p>
        </div>
      </div><!--end grid-->
    </div><!--end container-->

  </section><!--end section-->
  <!-- End -->
</template>


<script setup>
import { EnvelopeIcon, PhoneIcon } from '@heroicons/vue/24/solid';

const company = {
  name: 'Company A',
  industry: 'Technology',
  location: 'New York',
  email: 'contact@companya.com',
  telephone: '+1-123-456-7890',
  logoUrl: 'https://example.com/companya-logo.jpg',
};
</script>
