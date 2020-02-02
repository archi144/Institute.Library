from django.contrib import admin
from webapp.models import Book, Publisher, Order, Request, RequestBook

class PublisherInline(admin.ModelAdmin):
    model = Publisher
    fields = ['name']


class BookAdmin(admin.ModelAdmin):
    model = Book

class RequestBooksInline(admin.TabularInline):
    model = RequestBook
    fields = ['book', 'amount']

class RequestAdmin(admin.ModelAdmin):
    model = Request
    inlines = [RequestBooksInline]

admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Publisher)
admin.site.register(Request, RequestAdmin)
admin.site.register(RequestBook)