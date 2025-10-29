from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    page = "Accueil"
    return render(request, "app/index.html", {"page": page})


def about(request):
    page = "Qui sommes-nous ?"
    return render(request, "app/about.html", {"page": page})


def contact(request):
    page = "Contact"
    receiver = settings.EMAIL_HOST_USER
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        try:
            email_subject = f"Nouveau contact : {subject}"
            email_content = f"""
            Nouveau message reçu via le formulaire de contact:

            Nom complet: {name}
            Email: {email}
            Téléphone: {phone}
            Sujet: {subject}

            Message:
            {message}

            ---
            Cet email a été envoyé automatiquement depuis le formulaire de contact.
            """
            send_mail(
                email_subject,
                email_content,
                email,
                [receiver],
                fail_silently=False,
            )
            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect(request.path)
        except Exception as e:
            messages.error(request, f"Erreur lors de l'envoi: {str(e)}")
            return redirect(request.path)

    return render(request, "app/contact.html", {"page": page})


def services(request):
    page = "Nos services"
    return render(request, "app/services.html", {"page": page})
