from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from quality_control.models import BugReport

from quality_control.models import FeatureRequest


def index(request):
    bug_list = reverse('quality_control:bug_list')
    feature_list = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href='{bug_list}'> Список всех багов</a> и <a href='{feature_list}'> Запросы на улучшение</a>"
    return HttpResponse(html)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list = reverse('quality_control:bug_list')
        feature_list = reverse('quality_control:feature_list')
        html = f"<h1>Система контроля качества</h1><a href='{bug_list}'> Список всех багов</a> и <a href='{feature_list}'> Запросы на улучшение</a>"
        return HttpResponse(html)


def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список проблем</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li>{bug.title}({bug.status}) ---> <a href="{bug.id}/">{bug.title}</a></li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список улучшений</h1><ul>'
    for feature in features:
        features_html += f'<li>{feature.title}({feature.status}) ---> <a href="{feature.id}/">{feature.title}</a></li>'
    features_html += '</ul>'
    return HttpResponse(features_html)


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        response_html = f"<h1>{bug.title}</h1><p>{bug.description}</p><p>Статус: {bug.status}</p><p>Приоритет: {bug.priority}</p><p>Проект: {bug.project}</p><p>Задача: {bug.task}</p>"
        return HttpResponse(response_html)


def bug_detail(request, bug_id):
    html = f"Детали бага {bug_id}"
    return HttpResponse(html)


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        feature = self.get_object()
        response_html = f"<h1>{feature.title}</h1><p>{feature.description}</p><p>Статус: {feature.status}</p><p>Приоритет: {feature.priority}</p><p>Проект: {feature.project}</p><p>Задача: {feature.task}</p>"
        return HttpResponse(response_html)


def feature_detail(request, feature_id):
    html = f"Детали улучшения {feature_id}"
    return HttpResponse(html)
