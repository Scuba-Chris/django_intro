from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutSnickersView(TemplateView):
    template_name = 'about_snickers.html'
