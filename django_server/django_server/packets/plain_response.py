import django

class HttpResponsePlain(django.http.HttpResponse):

    def serialize(self):            return self.content
    def serialize_headers(self):    return ''
