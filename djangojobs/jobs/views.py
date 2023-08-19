from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import JobSerializer
from .models import Job



class JobListCreateAPIView(ListCreateAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        jobs = Job.objects.all()
        query = self.request.GET.get('query', '')
        categories = self.request.GET.get('category', '')

        # if query:
        #     jobs = jobs.filter(title__icontains=query)

        # if categories:
        #     categories_list = categories.split(',')
        #     jobs = jobs.filter(category__slug__in=categories_list)

        # # Exclude the 'applicant' field from the serialized data
        # # Note that 'applicant' is a ManyToManyField, so we use 'values' to exclude it
        # jobs = jobs.values(
        #     'id', 'title', 'slug', 'description', 'job_type', 'published_at',
        #     'vacancy', 'salary', 'experience', 'category', 'company', 'location',
        #     'image', 'is_published', 'last_date', 'created_at', 'updated_at',
        #     'active', 'views_count', 'click_count', 'featured', 'paid', 'paid_amount',
        #     'paid_at', 'paid_until', 'phone_number', 'address', 'email', 'author',
        #     'openings'
        # )
        return jobs

    def post(self, request, *args, **kwargs):
        # You can implement custom logic for POST requests here if needed
        return self.create(request, *args, **kwargs)


class JobListCreateAPIView(ListCreateAPIView):
    serializer_class = JobSerializer
    # lookup_field = 'slug'

    def get_queryset(self):
        jobs = Job.objects.all()  # # Job.get_sorted_jobs()
        query = self.request.GET.get('query', '')
        categories = self.request.GET.get('category', '')

        if query:
            jobs = jobs.filter(title__icontains=query)

        if categories:
            categories_list = categories.split(',')
            jobs = jobs.filter(category__slug__in=categories_list)

        return jobs

    def post(self, request, *args, **kwargs):
        # You can implement custom logic for POST requests here if needed
        return self.create(request, *args, **kwargs)


# class JobListCreateAPIView(ListCreateAPIView):
#     serializer_class = JobSerializer
#     lookup_field = 'slug'

#     def get_queryset(self):
#         jobs = Job.objects.all()  # # Job.get_sorted_jobs()
#         query = self.request.GET.get('query', '')
#         categories = self.request.GET.get('category', '')

#         if query:
#             jobs = jobs.filter(title__icontains=query)

#         if categories:
#             categories_list = categories.split(',')
#             jobs = jobs.filter(category__slug__in=categories_list)

#         return jobs


class JobRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Job.objects.get_queryset()
