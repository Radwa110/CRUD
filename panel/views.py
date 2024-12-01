from datetime import datetime
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import user
from django.utils.timezone import now
from django.db.models import Q

# Create your views here.
TEMPLATE_DIRS =(
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request , "index.html")

def list(request):
    if request.method=='POST':
        palabra = request.POST.get('keyword')
        lista = user.object.all()

        if palabra is not None :
            resultado_busqueda = lista.filter(
                Q(id_iconatins=palabra) |
                Q(name__iconatins=palabra)|
                Q(last_name_iconatins=palabra)|
                Q(mail_iconatins=palabra)|
                Q(phone_iconatins=palabra)
            )
            datos = {'user': resultado_busqueda}
            return render(request , "CRUD_user/list.html",datos)
        else:
            datos = {'user': lista}
            return render(request , "CRUD_user/list.html",datos)
    else:
        users=user.objects.order_by('-id')[:10]
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

def update(request, iduser):
    try:
        if request.method == 'POST':
            if (
                request.POST.get('id') and 
                request.POST.get('name') and 
                request.POST.get('last_name') and 
                request.POST.get('mail') and 
                request.POST.get('phone') and 
                request.POST.get('born')
            ):
                user_id_old = request.POST.get('id')
                # جلب المستخدم الموجود من قاعدة البيانات
                user_old = user.objects.get(id=user_id_old)

                # تحديث بيانات المستخدم الموجود
                user_old.name = request.POST.get('name')
                user_old.last_name = request.POST.get('last_name')
                user_old.mail = request.POST.get('mail')
                user_old.phone = request.POST.get('phone')
                user_old.born = request.POST.get('born')
                user_old.save()  # حفظ التعديلات في قاعدة البيانات
                
                return redirect('list')
        else:  
            users = user.objects.all()
            User = user.objects.get(id=iduser)
            datos = {'user': users , 'User': User}
            return render(request, "CRUD_user/update.html", datos)
        
    except user.DoesNotExist:
        users = user.objects.all()
        User = None
        datos = {'user': users , 'User':User}
        return render(request, "CRUD_user/update.html", datos)


def eliminate(request ,iduser):
    try:
        if request.method == 'POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                # حذف المستخدم باستخدام الـ ID
                user_to_delete = user.objects.get(id=id_a_borrar)
                user_to_delete.delete()
                return redirect('list')
        else:
            # تمرير قائمة المستخدمين إلى القالب
            users = user.objects.all()
            User = user.objects.get(id=iduser)
            datos = {'users': users , 'User':User }  # تغيير المفتاح إلى 'users'
            return render(request, "CRUD_user/eliminate.html", datos)
        
    except user.DoesNotExist:
        users = user.objects.all()
        User = None
        datos = {'user': users , 'User':User}
        return render(request, "CRUD_user/eliminate.html", datos)
    
        