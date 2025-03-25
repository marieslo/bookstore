from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Main Page'
        context['content'] = "HOME Furniture Store"
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - About Us'
        context['content'] = "About Us"
        context['text_on_page'] = "Text about why this store is so great, and what good products we offer."
        return context