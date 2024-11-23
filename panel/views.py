from datetime import datetime
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import user
from django.utils.timezone import now

# Create your views here.
TEMPLATE_DIRS =(
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request , "index.html")

def list(request):
    users=user.objects.all()
    datos={'user':users}
    return render(request , "CRUD_user/list.html",datos)

from django.shortcuts import render, redirect
from .models import user  # Ensure your model is correctly imported

def add(request):
    if request.method == 'POST':
        # Validate that all required fields are present in the POST request
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        born = request.POST.get('born')

        if name and last_name and mail and phone and born:
            # Create an instance of the user model and save it
            new_user = user(
                name=name,
                last_name=last_name,
                mail=mail,
                phone=phone,
                born=born
            )
            new_user.save()
            print("User created:", new_user)  # Log the created user
            return redirect('list')  # Redirect to a valid URL name
        else:
            # If any field is missing, you may want to provide feedback to the user
            return render(request, 'CRUD_user/add.html', {
                'error': 'All fields are required. Please fill out the form completely.'
            })
    else:
        users=user.objects.all()
        # Render the form for a GET request
        return render(request, 'CRUD_user/add.html')

def update(request):
    if request.method=='POST':
        if request.POST.get('id') and request.POST.get('name') and request.POST.get('last_name') and request.POST.get('mail') and request.POST.get('phone') and request.POST.get('born'):
           user_id_old=request.POST.get('id')
           user_old =user()
           user_old =user.objects.get(id = user_id_old)

           users=user()
           user.id=request.POST.get('id')
           user.name = request.POST.get('name')
           user.last_name = request.POST.get('last_name')
           user.mail = request.POST.get('mail')
           user.phone = request.POST.get('phone')
           user.born = request.POST.get('born')
           user.register = user_old.register 
           user.save()
           return redirect('list')
    else:  
      users=user.objects.all()
      datos={'user':users}
      return render(request , "CRUD_user/update.html",datos)

def eliminate(request):
    if request.method=='POST':
        if request.POST.get('id'):
            id_a_borrar = request.POST.get('id')
            tuple = user.objects.get(id=id_a_borrar)
            tuple.delete()
            return redirect('list')
    else:
        users=user.objects.all()
        datos={'user':users}
        return render(request , "CRUD_user/eliminate.html",datos)