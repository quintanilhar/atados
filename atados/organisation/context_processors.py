from atados.organisation.models import Organisation

def organisation(request):
    if request.user.is_authenticated():
        list = Organisation.objects.filter(user=request.user)
        return {'organisation_list': list}
    return {}

