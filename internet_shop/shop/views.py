from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import DeletionMixin, FormMixin
from django.views.generic.list import MultipleObjectMixin
from django_filters import filters
from django.views import generic
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.views.generic.base import View
from django.db.models import Q, F, Sum
from .models import *
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .filters import ProductFilter


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all().order_by('-price')
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class CategoryList(SingleObjectMixin, ListView):
    template_name = "category_list.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.object
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return self.object.product_category.all()


class ProductSearch(ListView):
    template_name = 'product_list.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return queryset


class BasketDeleteOne(DeleteView):
    model = Basket
    success_url = 'http://127.0.0.1:8000/basket/'


def BasketDeleteAll(request):
    Basket.objects.all().delete()
    return redirect('http://127.0.0.1:8000')


class BasketListView(ListView):
    template_name = 'basket.html'
    model = Basket

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["get_sum"] = Basket.objects.all().aggregate(Sum("cost"))['cost__sum']
        return context


class AddBasket(View):
    def get(self, request):
        offer_id = request.GET.get('offer_id')
        if Basket.objects.filter(product_id=offer_id):
            Basket.objects.filter(product_id=offer_id).update(
                product_id=offer_id,
                count_products=Basket.objects.get(product_id=offer_id).count_products + int(
                    request.GET.get('cost')),
                cost=(Basket.objects.get(product_id=offer_id).count_products + int(
                    request.GET.get('cost'))) * (
                         Product.objects.get(id=offer_id).price)
            )
        else:
            Basket.objects.create(
                product_id=offer_id,
                count_products=int(request.GET.get('cost')),
                cost=Product.objects.get(id=offer_id).price
            )
        return redirect('http://127.0.0.1:8000/basket/')
