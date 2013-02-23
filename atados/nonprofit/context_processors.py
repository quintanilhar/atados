from atados.nonprofit.models import Nonprofit

def nonprofit(request):
    if request.user.is_authenticated():
        list = Nonprofit.objects.filter(user=request.user)
        return {'nonprofit_list': list}
    return {}

