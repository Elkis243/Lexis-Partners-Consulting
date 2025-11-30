from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import EmailMessage


def index(request):
    page = "Accueil"
    return render(request, "app/index.html", {"page": page})


def about(request):
    page = "Qui sommes-nous ?"
    return render(request, "app/about.html", {"page": page})


def contact(request):
    page = "Contact"
    receiver = "info@lexispartnersconsulting.com"
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        email_subject = f"Nouveau message de {name}"
        body = f"""
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
        
        
        try:
            mail = EmailMessage(
                subject=email_subject,
                body=body,
                from_email=settings.EMAIL_HOST_USER,  # Email de l'hosting pour répondre
                to=[receiver],  # Destinataire un alias pour répondre
                reply_to=[email],
            )
            mail.send(fail_silently=False)

            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect(request.path)

        except Exception as e:
            messages.error(request, f"Erreur lors de l'envoi: {str(e)}")
            return redirect(request.path)

    return render(request, "app/contact.html", {"page": page})


def services(request):
    page = "Nos services"
    return render(request, "app/services.html", {"page": page})


def robots_txt(request):
    """
    Vue pour servir le fichier robots.txt
    """
    lines = [
        "User-agent: *",
        "Allow: /",
        "",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
