from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from webapp.views import BookCreateView, BookDetailView, BookListView, BookDeleteView, \
    BookUpdateView, OrderListView, OrderDetailView, PublisherDetailView, \
    PublisherListView, OrderUpdateView, OrderCreateView, PublisherCreateView, PublisherDeleteView, PublisherUpdateView, RequestListView, \
    RequestDetailView, RequestCreateView, RequestBookCreateView


app_name = 'webapp'

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book/create', BookCreateView.as_view(), name='book_create'),
    path('book/update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('order/create', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),
    path('orders', OrderListView.as_view(), name='order_list'),
    path('publisher/<int:pk>', PublisherDetailView.as_view(), name='publisher_detail'),
    path('publishers', PublisherListView.as_view(), name='publisher_list'),
    path('publisher/create', PublisherCreateView.as_view(), name='publisher_create'),
    path('publisher/update/<int:pk>', PublisherUpdateView.as_view(), name='publisher_update'),
    path('publisher/delete/<int:pk>', PublisherDeleteView.as_view(), name='publisher_delete'),
    # path('order/<int:pk>/book/create', OrderBookCreateView.as_view(), name='order_book_create'),
    # path('order/book/<int:pk>/update', OrderBookUpdateView.as_view(), name='order_book_update'),
    # path('order/book/<int:pk>/delete', OrderBookDeleteView.as_view(), name='order_book_delete'),
    path('request/<int:pk>', RequestDetailView.as_view(), name='request_detail'),
    path('requests', RequestListView.as_view(), name='request_list'),
    path('request/create', RequestCreateView.as_view(), name='request_create'),
    path('request/<int:pk>/book/create', RequestBookCreateView.as_view(), name='request_book_create')
]
