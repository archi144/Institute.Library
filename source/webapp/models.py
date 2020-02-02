from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50, verbose_name="Издатель")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return self.name

class Book(models.Model):

    TYPE_EBOOK = 'Электронная'
    TYPE_PBOOK = 'Печатная'

    TYPE_CHOICES = (
        (TYPE_EBOOK, 'e-version'),
        (TYPE_PBOOK, 'print version')
    )

    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    type = models.CharField(max_length=50, default=TYPE_PBOOK, choices=TYPE_CHOICES, verbose_name='Статус')
    author = models.CharField(max_length=200, verbose_name="Автор")
    link = models.CharField(max_length=200, blank=True, verbose_name="Ссылка")
    amount = models.IntegerField(blank=True, verbose_name="Количество")
    publisher = models.ForeignKey(Publisher, blank=True, related_name='books', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
class Request(models.Model):

    STATUS_NEW = 'На рассмотрении'
    STATUS_OK = 'Одобрена'
    STATUS_NO = 'Отклонена'

    STATUS_CHOICES = (
        (STATUS_NEW, 'На рассмотрении'),
        (STATUS_OK, 'Одобрена'),
        (STATUS_NO, 'Отклонена')
    )

    TYPE_WRITEDOWN = 'На списание'
    TYPE_PURCHASE = 'На закупку'

    TYPE_CHOICES = (
        (TYPE_WRITEDOWN, 'На списание'),
        (TYPE_PURCHASE, 'На закупку')
    )

    type = models.CharField(max_length=20, default=TYPE_PURCHASE, choices=TYPE_CHOICES)
    status = models.CharField(max_length=20, default=STATUS_NEW, choices=STATUS_CHOICES)

    def __str__(self):
        return self.id

class RequestBook(models.Model):
    request = models.ForeignKey(Request, related_name='request_books', verbose_name='Заявка', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='request_books', verbose_name='Книга', on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True, default=1, verbose_name="Количество")

    def __str__(self):
        return self.book.title

class Order(models.Model):

    STATUS_NEW = 'Новый'
    STATUS_DELIVERED = 'Принят'
    STATUS_CANCELED = 'Отменён'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый'),
        (STATUS_DELIVERED, 'Принят'),
        (STATUS_CANCELED, 'Отменён')
    )

    status = models.CharField(max_length=20, default=STATUS_NEW, verbose_name='Статус', choices=STATUS_CHOICES)
    publisher = models.ForeignKey(Publisher, blank=True, null=True, related_name='orders', on_delete=models.PROTECT)
    book = models.ManyToManyField(RequestBook, related_name='order_books', verbose_name='Книга')

    def __str__(self):
        return self.id












