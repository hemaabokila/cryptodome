from datetime import date
from home.models import AppVisit

class TrackAppVisitsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/':
            today = date.today()
            visits = AppVisit.objects.filter(app_name="home", date=today)

            if visits.exists():
                visit = visits.first()
                visit.visit_count += 1
                visit.save()
            else:
                AppVisit.objects.create(app_name="home", date=today, visit_count=1)

        response = self.get_response(request)
        return response
