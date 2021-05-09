from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

app_name = "core"

urlpatterns = [
    path(
        "", login_required(TemplateView.as_view(template_name="root.html")), name="root"
    ),
    # 404 구현할 때 re_path("", ...)를 사용하는 패턴!
]
