from django.http import HttpResponse
from django.views import View
from django.shortcuts import render,get_object_or_404
from .models import Contact, Data 




def index(request):
    if request.method == "POST":
        name = request.POST.get('name', '')  # Provide a default value if name is not present
        email = request.POST.get('email', '')  
        mobile = request.POST.get('mobile', '')
        subject = request.POST.get('subject', '') 
        description = request.POST.get('description', '') 

        # Assuming 'Contact' is a model, create an instance and save it
        rc = Contact.objects.create(name=name, email=email, mobile=mobile, subject=subject, description=description)

    return render(request, 'apps/index.html', locals())



def about(request):
    return render(request, 'apps/about.html', locals())



def contact(request):
    return render(request, 'apps/contact.html', locals())


def download_file(request, file_id):
    
    file_object = get_object_or_404(Data, id=file_id)


    response = HttpResponse(file_object.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file_object.file}"'
    return response