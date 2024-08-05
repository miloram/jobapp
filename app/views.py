from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse

job_title = [
    "First job",
    "Second Job",
    "Third Job"
]

job_description = [
    "First Job Description",
    "Second Job Description",
    "Third Job Description"
]

# Create your views here.
#def hello(request):
#    return HttpResponse("<h3>Hello World</h3>")

def job_list(request):
    list_of_jobs = "<ul>"
    for j in job_title:
        job_id = job_title.index(j)
        detail_url = reverse('jobs_detail', args=(job_id,))
        list_of_jobs += f"<li><a href='{detail_url}'>{j}</li>"
    list_of_jobs += "</ul>"
    return HttpResponse(list_of_jobs)

def job_detail(request, id):
    print(type(id))

    try:
        if id ==0:
            return redirect(reverse('jobs_home'))
        return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        return HttpResponse(return_html)
    except:
        return HttpResponseNotFound("Not Found")

    # "<domain>/job/1" --> Job detail page