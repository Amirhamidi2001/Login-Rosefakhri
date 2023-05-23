from django.views.generic.base import TemplateView


class TemplateView(TemplateView):
    """
    Render a template and redirect to api versions
    """

    template_name = "index.html"
