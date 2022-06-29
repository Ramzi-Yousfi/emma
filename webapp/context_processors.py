
from .models import Galeries


def base(request):
    submenu = Galeries.objects.all()
    return  {'submenu': submenu}
