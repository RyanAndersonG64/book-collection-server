from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import *
from .serializers import *

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serialized_profile = ProfileSerializer(profile)
    return Response(serialized_profile.data)

@api_view(['POST'])
@permission_classes([])
def create_user(request):
    user = User.objects.create(
        username = request.data['username'],
    )
    user.set_password(request.data['password'])
    user.save()
    profile = Profile.objects.create(
        user=user,
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )
    profile.save()
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

@api_view(['POST'])
@permission_classes([])
def create_author(request):
    author = Author.objects.create(
        name = request.data.get('name'),
    )
    author.save()
    serialized_author = AuthorSerializer(author)
    return Response(serialized_author.data)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['POST'])
@permission_classes([])
def create_book(request):
    book = Book.objects.create(
        title = request.data.get('title'),
        author = request.data.get('author'),
        published = request.data.get('published'),
    )
    book.readers.add(request.data.get('readers'))
    book.save()
    serialized_book = BookSerializer(book)
    return Response(serialized_book.data)

@api_view(['PUT'])
@permission_classes([])
def add_reader(request):
    book_pk = request.data.get('bookId')
    book = Book.objects.get(pk=book_pk)
    reader_id = request.data.get('readers')
    print(book_pk)
    print(reader_id)
    reader = Profile.objects.get(pk = reader_id)
    book.readers.add(reader)
    book.save()
    serialized_book = BookSerializer(book)
    return Response(serialized_book.data)
