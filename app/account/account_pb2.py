# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: account.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='account.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\raccount.proto\"\x91\x01\n\x15LikesAndViewsResponse\x12\x12\n\nbook_likes\x18\x01 \x03(\t\x12\x12\n\nbook_views\x18\x02 \x03(\t\x12\x12\n\nimdb_likes\x18\x03 \x03(\t\x12\x12\n\nimdb_views\x18\x04 \x03(\t\x12\x13\n\x0b\x61nime_likes\x18\x05 \x03(\t\x12\x13\n\x0b\x61nime_views\x18\x06 \x03(\t\"=\n\x14LikesAndViewsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x14\n\x05types\x18\x02 \x01(\x0e\x32\x05.Type*.\n\x04Type\x12\x08\n\x04\x42OOK\x10\x00\x12\x08\n\x04IMDB\x10\x01\x12\t\n\x05\x41NIME\x10\x02\x12\x07\n\x03\x41LL\x10\x03\x32L\n\x07\x41\x63\x63ount\x12\x41\n\x10GetLikesAndViews\x12\x15.LikesAndViewsRequest\x1a\x16.LikesAndViewsResponseb\x06proto3'
)

_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOOK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IMDB', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANIME', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=228,
  serialized_end=274,
)
_sym_db.RegisterEnumDescriptor(_TYPE)

Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
BOOK = 0
IMDB = 1
ANIME = 2
ALL = 3



_LIKESANDVIEWSRESPONSE = _descriptor.Descriptor(
  name='LikesAndViewsResponse',
  full_name='LikesAndViewsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='book_likes', full_name='LikesAndViewsResponse.book_likes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book_views', full_name='LikesAndViewsResponse.book_views', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imdb_likes', full_name='LikesAndViewsResponse.imdb_likes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imdb_views', full_name='LikesAndViewsResponse.imdb_views', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='anime_likes', full_name='LikesAndViewsResponse.anime_likes', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='anime_views', full_name='LikesAndViewsResponse.anime_views', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=163,
)


_LIKESANDVIEWSREQUEST = _descriptor.Descriptor(
  name='LikesAndViewsRequest',
  full_name='LikesAndViewsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='LikesAndViewsRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='types', full_name='LikesAndViewsRequest.types', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=226,
)

_LIKESANDVIEWSREQUEST.fields_by_name['types'].enum_type = _TYPE
DESCRIPTOR.message_types_by_name['LikesAndViewsResponse'] = _LIKESANDVIEWSRESPONSE
DESCRIPTOR.message_types_by_name['LikesAndViewsRequest'] = _LIKESANDVIEWSREQUEST
DESCRIPTOR.enum_types_by_name['Type'] = _TYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LikesAndViewsResponse = _reflection.GeneratedProtocolMessageType('LikesAndViewsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LIKESANDVIEWSRESPONSE,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:LikesAndViewsResponse)
  })
_sym_db.RegisterMessage(LikesAndViewsResponse)

LikesAndViewsRequest = _reflection.GeneratedProtocolMessageType('LikesAndViewsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LIKESANDVIEWSREQUEST,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:LikesAndViewsRequest)
  })
_sym_db.RegisterMessage(LikesAndViewsRequest)



_ACCOUNT = _descriptor.ServiceDescriptor(
  name='Account',
  full_name='Account',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=276,
  serialized_end=352,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetLikesAndViews',
    full_name='Account.GetLikesAndViews',
    index=0,
    containing_service=None,
    input_type=_LIKESANDVIEWSREQUEST,
    output_type=_LIKESANDVIEWSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNT)

DESCRIPTOR.services_by_name['Account'] = _ACCOUNT

# @@protoc_insertion_point(module_scope)
