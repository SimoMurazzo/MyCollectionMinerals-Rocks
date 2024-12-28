from django.db.models import Q
from django.views.generic import ListView, DetailView

from Minerals.models import Mineral


class MineralList(ListView):
    template_name = 'listview.html'
    paginate_by = 12

    def get_queryset(self):
        total_query = Q()
        locality = self.request.GET.get('locality')
        if locality:
            total_query = total_query & Q(locality__icontains=locality)
        rarity = self.request.GET.get('rarity')
        if rarity:
            total_query = total_query & Q(rarity__icontains=rarity)
        environment = self.request.GET.get('environment')
        if environment:
            total_query = total_query & Q(environment__icontains=environment)
        crystal_system = self.request.GET.get('crystal_system')
        if crystal_system:
            total_query = total_query & Q(crystal_system__icontains=crystal_system)
        cleavage = self.request.GET.get('cleavage')
        if cleavage:
            total_query = total_query & Q(cleavage__icontains=cleavage)
        luminescence = self.request.GET.get('luminescence')
        if luminescence:
            total_query = total_query & Q(luminescence__icontains=luminescence)
        luster = self.request.GET.get('luster')
        if luster:
            total_query = total_query & Q(luster__icontains=luster)
        streak = self.request.GET.get('streak')
        if streak:
            total_query = total_query & Q(streak__icontains=streak)
        pleochroism = self.request.GET.get('pleochroism')
        if pleochroism:
            total_query = total_query & Q(pleochroism__icontains=pleochroism)
        radioactivity = self.request.GET.get('radioactivity')
        if radioactivity:
            total_query = total_query & Q(radioactivity__icontains=radioactivity)
        query = self.request.GET.get('query')
        if query:
            total_query = total_query & (Q(name__icontains=query) | Q(description__icontains=query) | Q(strunz_class__icontains=query))
        return Mineral.objects.filter(total_query).order_by('strunz_class')


class MineralDetail(DetailView):
    template_name = 'detailview.html'
    model = Mineral
