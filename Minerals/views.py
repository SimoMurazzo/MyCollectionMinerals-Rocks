from django.views.generic import ListView, DetailView

from Minerals.models import Mineral


class MineralList(ListView):
    template_name = 'listview.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return Mineral.objects.filter(name__icontains=query, description__icontains=query)
        else:
            return Mineral.objects.all()
