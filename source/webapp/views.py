from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from webapp.models import Book, Order, Publisher, Request, RequestBook
from webapp.forms import OrderForm, BookForm, RequestBookForm, PublisherForm, RequestForm
from collections import Counter


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_create.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('webapp:book_detail', kwargs={'pk': self.object.pk})

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_update.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('webapp:book_detail', kwargs={'pk': self.object.pk})

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'

    def get_success_url(self):
        return reverse('webapp:book_list')

class BookListView(ListView):
    model = Book
    template_name = 'index.html'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderbooks'] = RequestBook.objects.filter(book__publisher=self.object.publisher)
        list = []
        for orderbook in context['orderbooks']:
            list.append(orderbook.book.id)
        a = set(list)
        context['list'] = a
        context['len'] = len(list)

        for orderbook in context['orderbooks']:
            if orderbook.book.id in list:
                amount = orderbook.amount
                amount += orderbook.amount
                context['amount'] = amount

        return context


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'



class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderForm


    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})

# class OrderBookCreateView(CreateView):
#     model = OrderBook
#     form_class = OrderBookForm
#     template_name = 'order_book_create.html'
#
#     def get_success_url(self):
#         return reverse('webapp:order_detail', kwargs={'pk': self.object.order.pk})
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['order'] = Order.objects.get(pk=self.kwargs.get('pk'))
#         return context
#
#     def form_valid(self, form):
#         form.instance.order = Order.objects.get(pk=self.kwargs.get('pk'))
#         return super().form_valid(form)
#
# class OrderBookUpdateView(UpdateView):
#     model = OrderBook
#     form_class = OrderBookForm
#     template_name = 'order_book_update.html'
#
#     def get_success_url(self):
#         return reverse('webapp:order_detail', kwargs={'pk': self.object.order.pk})
#
# class OrderBookDeleteView(DeleteView):
#     model = OrderBook
#     template_name = 'order_book_delete.html'
#
#     def get_success_url(self):
#         return reverse('webapp:order_detail', kwargs={'pk': self.object.order.pk})

class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'publisher_detail.html'


class PublisherListView(ListView):
    model = Publisher
    template_name = 'publisher_list.html'

class PublisherCreateView(CreateView):
    model = Publisher
    template_name = 'publisher_create.html'
    form_class = PublisherForm

    def get_success_url(self):
        return reverse('webapp:publisher_detail', kwargs={'pk': self.object.pk})

class PublisherUpdateView(UpdateView):
    model = Publisher
    template_name = 'publisher_update.html'
    form_class = PublisherForm

    def get_success_url(self):
        return reverse('webapp:publisher_detail', kwargs={'pk': self.object.pk})

class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'publisher_delete.html'


    def get_success_url(self):
        return reverse('webapp:publisher_list')

class RequestDetailView(DetailView):
    model = Request
    template_name = 'request_detail.html'


class RequestListView(ListView):
    model = Request
    template_name = 'request_list.html'


class RequestCreateView(CreateView):
    model = Request
    template_name = 'request_create.html'
    form_class = RequestForm

    def get_success_url(self):
        return reverse('webapp:request_detail', kwargs={'pk': self.object.pk})

class RequestBookCreateView(CreateView):
    model = RequestBook
    form_class = RequestBookForm
    template_name = 'request_book_create.html'

    def get_success_url(self):
        return reverse('webapp:request_detail', kwargs={'pk': self.object.request.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = Request.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.request = Request.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)