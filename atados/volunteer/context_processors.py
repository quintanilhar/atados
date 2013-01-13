from atados.volunteer.models import Volunteer

def volunteer(request):
    if request.user.is_authenticated():
        try:
            return {'volunteer_session': Volunteer.objects.get(user=request.user)}
        except Volunteer.DoesNotExist:
            pass
    return {}

