from django.http import HttpResponsePermanentRedirect

class RedirectToWwwMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.get_host().startswith('www.'):
            new_url = request.build_absolute_uri().replace("://", "://www.", 1)
            return HttpResponsePermanentRedirect(new_url)
        return self.get_response(request)