from django.forms import ModelForm

from .models import BugReport


class BugReport(ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'status', 'priority']
