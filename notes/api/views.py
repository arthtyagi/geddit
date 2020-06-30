from notes.models import Notes
from notes.api.serializers import NotesSerializer
from django.http import Http404
from rest_framework import generics, permissions, serializers
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

class NotesList(generics.ListCreateAPIView):

	queryset = Notes.objects.all()
	serializer_class = NotesSerializer


class NotesDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = Notes.objects.all()
	serializer_class = NotesSerializer


"""
from rest_framework import mixins
class notesList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
	queryset = notes.objects.all()
	serializer_class = notesSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
class notesDetail(mixins.RetrieveModelMixin,	mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
	queryset = notes.objects.all()
	serializer_class = notesSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
"""