from base.models import Location


class MyMiddleware(object):
    def process_request(self, request):
        loc = Location(name=request.get_full_path())
        loc.save()
