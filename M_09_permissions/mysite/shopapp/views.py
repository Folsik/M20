from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from .models import Product, Order


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
        }
        return render(request, 'shopapp/shop-index.html', context=context)


class ProductDetailsView(DetailView):
    template_name = "shopapp/products-details.html"
    model = Product
    context_object_name = "product"


class ProductsListView(ListView):
    template_name = "shopapp/products-list.html"
    context_object_name = "products"
    queryset = Product.objects.filter(archived=False)


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "shopapp.add_permission"  # TODO такого разрешения не существует, но есть add_product
    model = Product
    fields = "name", "price", "description", "discount"
    success_url = reverse_lazy("shopapp:products_list")

    # TODO чтобы привязать созданный товар к пользователю, переопределите метод form_valid, где, согласно подсказке
    #  присвоить полю формы объект пользователя из запроса: form.instance.created_by = self.request.user и сохранить
    #  форму

    # TODO По поводу пункта 8: в шаблоне надо проверить наличие разрешения для отображения ссылки на создания товара:
    #  {% if perms.shopapp.add_product %}  тут html-код ссылки на создание товара {% endif %}

class ProductUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.groups.filter(name="").exists() or self.request.user.is_superuser

    model = Product
    fields = "name", "price", "description", "discount"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            "shopapp:product_details",
            kwargs={"pk": self.object.pk},
        )


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OrdersListView(LoginRequiredMixin, ListView):
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
    )


class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ["shopapp.view_order"]
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
    )
