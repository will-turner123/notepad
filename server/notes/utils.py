from hashids import Hashids
from django.conf import settings

hashids = Hashids("ajlskdjf", min_length=5)

def h_encode(id):
    return hashids.encode(id)

def h_decode(h):
    z = hashids.decode(h)
    if z:
        return z[0]

class HashIdConverter:
    regex = '[a-zA-Z0-9]{5,}'

    def to_python(self, value):
        return h_decode(value)

    def to_url(self, value):
        return h_encode(value)