from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_successful_url(self, request, user):
        return ('registration_create_quote');
