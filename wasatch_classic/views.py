from django.views.generic.edit import FormView

from .forms import RegistrationForm


class RegistrationFormView(FormView):
    template_name = "registration.html"
    form_class = RegistrationForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(RegistrationFormView, self).form_valid(form)
