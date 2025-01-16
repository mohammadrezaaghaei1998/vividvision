from django.shortcuts import render,redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact , Video, Partner_Company,Banner, Blog

from itertools import zip_longest

def chunk_blogs(blogs, n):
    """Split the blogs into chunks of size n."""
    args = [iter(blogs)] * n
    return zip_longest(*args, fillvalue=None)

def home(request):
    partners = Partner_Company.objects.all() 
    banners = Banner.objects.all() 
    blogs = Blog.objects.all()
    
    # Split blogs into chunks of 3
    blog_chunks = chunk_blogs(blogs, 3)
    
    return render(request, 'main/home.html', {
        'partners': partners,
        'banners': banners,
        'blog_chunks': blog_chunks
    })



def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'main/blogs.html', {'blog': blog})




def gallery(request):
    
    videos = Video.objects.all() 
    return render(request, "main/gallery.html", {'videos': videos})




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



