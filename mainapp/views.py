from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog, Newsletter, Membership
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Send mail
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# end


# Create your views here.

class HomePageView(TemplateView):
    template_name="mainapp/index.html"

class AboutPageView(TemplateView):
    template_name="mainapp/about.html"

class OutreachPageView(TemplateView):
    template_name="mainapp/outreach.html"

class ChallengebowlPageView(TemplateView):
    template_name="mainapp/seg-challengebowl.html"

class ComferencesPageView(TemplateView):
    template_name="mainapp/seg-conferences.html"

class FieldcampsPageView(TemplateView):
    template_name="mainapp/seg-fieldcamps.html"

class ScholarshipPageView(TemplateView):
    template_name="mainapp/seg-scholarships.html"

class SymposiumPageView(TemplateView):
    template_name="mainapp/seg-symposium.html"

class workshopPageView(TemplateView):
    template_name="mainapp/webinars-workshop.html"


class BlogsPageView(ListView):
    template_name="mainapp/blog.html"
    model=Blog
    context_object_name="blogs"

class BlogDetailPageView(DetailView):
    template_name="mainapp/blog-single.html"
    model=Blog
    context_object_name="blog"


@csrf_exempt
def ContactPageView(request):
    if request.method=="POST":
        email=request.POST["email"]
        name=request.POST["name"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        email_message = send_mail(subject=subject, message=message,
            from_email="nwaforglory6@gmail.com",
            recipient_list=["nwaforglory6@gmail.com"],
        )
        # email_message.send()
        return JsonResponse({"detail":"Mail send successfully."})
    return render(request, "mainapp/contact.html")

def membershipView(request):
    if request.method=="POST":
        membership=Membership.objects.create(
            full_name=request.POST["full_name"],
            email=request.POST["email"],
            course_of_study=request.POST["course_of_study"],
            university=request.POST["university"],
            excepted_year_of_graduation=request.POST["excepted_year_of_graduation"],
            date_of_birth=request.POST["date_of_birth"],
            gender=request.POST["gender"],
            phone_number=request.POST["phone_number"],
            address=request.POST["address"],
            payment_slip=request.FILES["payment_slip"],
            
        )
        full_name=request.POST["full_name"]
        email=request.POST["email"]
        subject="Membership application recieved successfully"
        # Render the HTML template using the user's email and name
        html_content = render_to_string('partials/membership_success_mail.html', {'full_name': full_name})

        # Create the EmailMultiAlternatives object
        email_message = EmailMultiAlternatives(subject=subject,
            from_email="nwaforglory6@gmail.com",
            to=[email],
        )

        # Attach the HTML content to the email message
        email_message.attach_alternative(html_content, "text/html")

        # Send the email
        email_message.send()
        messages.success(request, 'Application sent !!')
    return render(request, "mainapp/membership.html")

@csrf_exempt
def Subscribe(request):
    if request.method=="POST":
        email=request.POST["email"]
        try:
            Newsletter.objects.create(email=email)
        except:
            return JsonResponse({"detail":"Already a subscriber !!"})
        subject="Welcome to SEGNAU newsletter"
        # Render the HTML template using the user's email and name
        html_content = render_to_string('partials/newsletter_confirm.html', {'email': email})

        # Create the EmailMultiAlternatives object
        email_message = EmailMultiAlternatives(subject=subject,
            from_email="nwaforglory6@gmail.com",
            to=[email],
        )

        # Attach the HTML content to the email message
        email_message.attach_alternative(html_content, "text/html")

        # Send the email
        email_message.send()
    return JsonResponse({"detail":"Thank you for subscribing."})
    