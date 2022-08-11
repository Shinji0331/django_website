# djangoで用意されているテンプレートを取り出す
from django.views.generic import TemplateView

# トップページアクセス時のindex.htmlを定義する。
class IndexView(TemplateView):
    template_name = "index.html"

    # 変数を渡して表示する
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "Shun"
        return ctxt

# aboutページのabout.htmlを定義する。
class AboutView(TemplateView):
    template_name = "about.html"

    # 変数を渡して表示する
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_service"] = "1123456"
        ctxt["skills"] = [
            "Python",
            "C++",
            "Javascript",
            "Rust",
            "Go",
        ]
        return ctxt