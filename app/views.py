from flask.views import View

class WelcomeView(View):
    def dispatch_request(self):
        return "Bienvenidos al sistema"
