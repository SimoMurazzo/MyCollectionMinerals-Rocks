from django.db.models import Q
from django.views.generic import ListView, DetailView

from Minerals.models import Mineral


class MineralList(ListView):
    template_name = 'listview.html'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('query')
        print(query)
        if query:
            return Mineral.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        else:
            return Mineral.objects.all()


class MineralDetail(DetailView):
    template_name = 'detailview.html'
    model = Mineral
