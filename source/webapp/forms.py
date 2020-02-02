from django import forms
from webapp.models import Book, Order, Publisher, Request, RequestBook

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = []

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = []

class RequestBookForm(forms.ModelForm):
    class Meta:
        model = RequestBook
        exclude = ['request']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        exclude = []

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = []

