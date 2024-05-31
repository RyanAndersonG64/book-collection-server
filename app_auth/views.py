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
@permission_classes([IsAuthenticated])
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



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_book(request):
    print(f'wefewfewfsafwetrweherh {request.data}')
    author_data = request.data.get('author', {}.get('name'))
    author, created = Author.objects.get_or_create(name=author_data)
    book = Book.objects.create(
        title = request.data['title'],
        author = author,
        published = request.data['published'],
    )
    # if Author.objects.get(name = author_data):
    #     book.author.add(name = author_data)
    # else:
    #     author = Author(author_data)
    #     book.author.add(author)
    book.readers.add(request.data.get('readers'))
    book.save()
    serialized_book = BookSerializer(book)
    return Response(serialized_book.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
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
