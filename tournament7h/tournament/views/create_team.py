from django.shortcuts import render
from tournament.models import Team
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def page(request):
    if len(request.POST) > 0:
        form = FormSupervisor(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # If the form is valid, we store the data in a model record in
            # the form.
            return HttpResponseRedirect(reverse('public_index'))
            # This line is used to redirect to the specified URL. We use the
            # reverse() function to get the URL from its name defines urls.py.
        else:
            return render(request, 'public/create_team.html', {'form': form})
    else:
        form = FormSupervisor()
        return render(request, 'public/create_team.html', {'form': form})

class FormSupervisor(forms.ModelForm):
    # Here we create a class that inherits from ModelForm.

    class Meta:
        # We extend the Meta class of the ModelForm. It is this class that
        # will allow us to define the properties of ModelForm.

        model = Team
        # We define the model that should be based on the form.

        exclude = ('date_created', 'last_connexion', )
        # We exclude certain fields of this form. It would also have been
        # possible to do the opposite. That is to say with the fields property,
        # we have defined the desired fields in the form.
