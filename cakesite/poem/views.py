from django.db.models import Q
from rest_framework import viewsets
from poem.serialize import PoemListSerializer, ResultPagination, PoetryListSerializer, PoemAuthorSerializer, \
    PoetryAuthorSerializer
from .models import Poems, Poetry, PoemsAuthor, PoetryAuthor
from rest_framework.response import Response
from collections import OrderedDict


# Create your views here.


# 词
class PoemListViewSet(viewsets.ModelViewSet):
    pagination_class = ResultPagination
    queryset = Poems.objects.all()
    serializer_class = PoemListSerializer

    def list(self, request, *args, **kwargs):
        name = request.GET.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(
                Q(title__contains=name) | Q(author__contains=name) | Q(content__contains=name))
        try:
            queryset = self.filter_queryset(self.queryset)
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)

                return Response(OrderedDict([
                    ('code', 200),
                    ('count', self.paginator.page.paginator.count),
                    ('next', self.paginator.get_next_link()),
                    ('previous', self.paginator.get_previous_link()),
                    ('results', serializer.data)
                ]))

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


class PoemAuthorViewSet(viewsets.ModelViewSet):
    queryset = PoemsAuthor.objects.all()
    serializer_class = PoemAuthorSerializer

    def list(self, request, *args, **kwargs):
        author = request.GET.get('author')
        self.queryset = self.queryset.filter(id=author)
        try:
            queryset = self.filter_queryset(self.queryset)
            serializer = self.get_serializer(queryset, many=True)
            return Response(OrderedDict([
                ('code', 200),
                ('results', serializer.data[0])
            ]))
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


# 诗
class PoetryListViewSet(viewsets.ModelViewSet):
    pagination_class = ResultPagination
    queryset = Poetry.objects.all()
    serializer_class = PoetryListSerializer

    def list(self, request, *args, **kwargs):
        name = request.GET.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(
                Q(title__contains=name) | Q(author__contains=name) | Q(content__contains=name))
        try:
            queryset = self.filter_queryset(self.queryset)
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)

                return Response(OrderedDict([
                    ('code', 200),
                    ('count', self.paginator.page.paginator.count),
                    ('next', self.paginator.get_next_link()),
                    ('previous', self.paginator.get_previous_link()),
                    ('results', serializer.data)
                ]))

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


class PoetryAuthorViewSet(viewsets.ModelViewSet):
    queryset = PoetryAuthor.objects.all()
    serializer_class = PoetryAuthorSerializer

    def list(self, request, *args, **kwargs):
        author = request.GET.get('author')
        self.queryset = self.queryset.filter(id=author)
        try:
            queryset = self.filter_queryset(self.queryset)
            serializer = self.get_serializer(queryset, many=True)
            return Response(OrderedDict([
                ('code', 200),
                ('results', serializer.data[0])
            ]))
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))
