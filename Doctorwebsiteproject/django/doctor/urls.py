from django.urls import path, include
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentsTemplateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', HomeTemplateView.as_view(), name="home"),
    path('make-an-appointment/', AppointmentTemplateView.as_view(), name="appointment"),
    path('manage-appointment/', ManageAppointmentsTemplateView.as_view(), name="manager"),
]