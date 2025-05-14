from django.shortcuts import render

# Create your views here.


def index(request):
    page = "Accueil"
    return render(request, 'app/index.html', {
        'page': page
    })


def about(request):
    page = "Qui sommes-nous ?"
    return render(request, 'app/about.html', {
        'page': page
    })


def contact(request):
    page = "Contact" 
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        
        print(name, email, phone, subject, message)
        print("Données affichées avec succès !!!")

    return render(request, 'app/contact.html', {
        'page': page
    })


def services(request):
    page = "Nos services"
    return render(request, 'app/services.html', {
        'page': page
    })
