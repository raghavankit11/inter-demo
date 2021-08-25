from django.utils import timezone
import pytz
from django.utils.deprecation import MiddlewareMixin

from core import settings

class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_anonymous:
            timezone_selected = request.user.profile.timezone
            if not timezone_selected:
                timezone_selected = settings.TIME_ZONE
            timezone.activate(pytz.timezone(timezone_selected))
        else:
            timezone.deactivate()