from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Contact , Image , Video, Partner_Company, Team, Banner

# Create your views here.




def home(request):
    partners = Partner_Company.objects.all() 
    banners = Banner.objects.all() 
   
    return render(request, 'main/home.html', {'partners': partners,'banners': banners})


def about(request):
    partners = Partner_Company.objects.all()
    team_members = Team.objects.all()  # Fetch all team members
    return render(request, "main/about.html", {'partners': partners, 'team_members': team_members})


def contactus(request):
    return render(request,"main/contactus.html")


def service(request):
    return render(request,"main/service.html")

def gallery(request):
    # youtubevideourls = YoutubeVideoUrl.objects.all() 
    images_by_category = {
        'street': Image.objects.filter(category='street'),
        'advertisement': Image.objects.filter(category='advertisement'),
        'fashionista': Image.objects.filter(category='fashionista'),
        'artist': Image.objects.filter(category='artist'),
    }
    videos = Video.objects.all() 
    return render(request, "main/gallery.html", {
        'images_by_category': images_by_category,
        'videos': videos
        # 'youtubevideourls':youtubevideourls
    })




def contact(request):
    success_message = None
    form = ContactForm()  

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            contact = Contact(
                name=name,
                email=email,
                message=message
            )
            contact.save()

            success_message = 'Your message has been sent successfully!'
            return redirect('success')

    return render(request, 'main/contactus.html', {'form': form, 'success_message': success_message})



def success(request):
    return render(request,'main/success.html')



