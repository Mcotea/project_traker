from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import BugReportForm, FeatureRequestForm
from .models import BugReport, FeatureRequest


def index(request):
    return render(request, 'quality_control/index.html')


def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})


def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})


def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})


def create_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_create.html', {'form': form})


def create_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_create.html', {'form': form})


def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bug_id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})


def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature_id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})


def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bug_list')


def delete_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:feature_list')


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


class BugsListView(ListView):
    model = BugReport
    template_name = 'quality_control/bug_list.html'
    context_object_name = 'bug_list'


class FeaturesListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_list.html'
    context_object_name = 'feature_list'


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    context_object_name = 'bug'


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'
    context_object_name = 'feature'


class BugCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_create.html'
    success_url = reverse_lazy('quality_control:bug_list')
    context_object_name = 'bug'


class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_create.html'
    success_url = reverse_lazy('quality_control:feature_list')
    context_object_name = 'feature'


class BugUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bug_list')
    context_object_name = 'bug'


class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:feature_list')
    context_object_name = 'feature'


class BugDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bug_list')
    context_object_name = 'bug'
    template_name = 'quality_control/bug_confirm_delete.html'


class FeatureDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:feature_list')
    context_object_name = 'feature'
    template_name = 'quality_control/feature_confirm_delete.html'
