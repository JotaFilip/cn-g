# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: library.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import book_pb2 as book__pb2
import imdb_pb2 as imdb__pb2
import anime_pb2 as anime__pb2
import account_pb2 as account__pb2
import utils_pb2 as utils__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='library.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rlibrary.proto\x1a\nbook.proto\x1a\nimdb.proto\x1a\x0b\x61nime.proto\x1a\raccount.proto\x1a\x0butils.proto\"6\n\x10ItemInfoResponse\x12\"\n\x0frecommendations\x18\x01 \x03(\x0b\x32\t.ItemInfo\"9\n\x08ItemInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x04type\x18\x03 \x01(\x0e\x32\x05.Type\"\x9c\x01\n\x04Item\x12\x1c\n\x04\x62ook\x18\x01 \x01(\x0b\x32\t.BookDataH\x00\x88\x01\x01\x12\x1c\n\x04imdb\x18\x02 \x01(\x0b\x32\t.IMDBDataH\x01\x88\x01\x01\x12\x1e\n\x05\x61nime\x18\x03 \x01(\x0b\x32\n.AnimeDataH\x02\x88\x01\x01\x12\r\n\x05likes\x18\x04 \x01(\x03\x12\r\n\x05seens\x18\x05 \x01(\x03\x42\x07\n\x05_bookB\x07\n\x05_imdbB\x08\n\x06_anime\"3\n\x0eLibPageRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\"S\n\x15RecommendationRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\x12\x14\n\x05types\x18\x03 \x03(\x0e\x32\x05.Type\"N\n\x13SearchByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\x12\x14\n\x05types\x18\x03 \x01(\x0e\x32\x05.Type\"V\n\x17SearchByCategoryRequest\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\x12\x14\n\x05types\x18\x03 \x01(\x0e\x32\x05.Type\"\x9d\x01\n\x0e\x41\x64\x64ItemRequest\x12\x1c\n\x04\x62ook\x18\x01 \x01(\x0b\x32\t.BookDataH\x00\x88\x01\x01\x12\x1c\n\x04imdb\x18\x02 \x01(\x0b\x32\t.IMDBDataH\x01\x88\x01\x01\x12\x1e\n\x05\x61nime\x18\x03 \x01(\x0b\x32\n.AnimeDataH\x02\x88\x01\x01\x12\x13\n\x04type\x18\x04 \x01(\x0e\x32\x05.TypeB\x07\n\x05_bookB\x07\n\x05_imdbB\x08\n\x06_anime\")\n\x06ItemId\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x04type\x18\x02 \x01(\x0e\x32\x05.Type\"A\n\rItemIdAndUser\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x13\n\x04type\x18\x03 \x01(\x0e\x32\x05.Type2\xac\x03\n\x07Library\x12-\n\x07Library\x12\x0f.LibPageRequest\x1a\x11.ItemInfoResponse\x12\x36\n\tRecommend\x12\x16.RecommendationRequest\x1a\x11.ItemInfoResponse\x12#\n\x07\x41\x64\x64Item\x12\x0f.AddItemRequest\x1a\x07.ItemId\x12\x19\n\x07GetItem\x12\x07.ItemId\x1a\x05.Item\x12\x1f\n\nRemoveItem\x12\x07.ItemId\x1a\x08.Success\x12\'\n\x0b\x41\x64\x64SeenItem\x12\x0e.ItemIdAndUser\x1a\x08.Success\x12*\n\x0eRemoveSeenItem\x12\x0e.ItemIdAndUser\x1a\x08.Success\x12\'\n\x0b\x41\x64\x64LikeItem\x12\x0e.ItemIdAndUser\x1a\x08.Success\x12*\n\x0eRemoveLikeItem\x12\x0e.ItemIdAndUser\x1a\x08.Success\x12/\n\tGetTopTen\x12\x0e.TopTenRequest\x1a\x12.SeensAndLikesInfob\x06proto3'
  ,
  dependencies=[book__pb2.DESCRIPTOR,imdb__pb2.DESCRIPTOR,anime__pb2.DESCRIPTOR,account__pb2.DESCRIPTOR,utils__pb2.DESCRIPTOR,])




_ITEMINFORESPONSE = _descriptor.Descriptor(
  name='ItemInfoResponse',
  full_name='ItemInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='recommendations', full_name='ItemInfoResponse.recommendations', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=82,
  serialized_end=136,
)


_ITEMINFO = _descriptor.Descriptor(
  name='ItemInfo',
  full_name='ItemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ItemInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='ItemInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='ItemInfo.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=138,
  serialized_end=195,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='book', full_name='Item.book', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imdb', full_name='Item.imdb', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='anime', full_name='Item.anime', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='likes', full_name='Item.likes', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seens', full_name='Item.seens', index=4,
      number=5, type=3, cpp_type=2, label=1,
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
    _descriptor.OneofDescriptor(
      name='_book', full_name='Item._book',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_imdb', full_name='Item._imdb',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_anime', full_name='Item._anime',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=198,
  serialized_end=354,
)


_LIBPAGEREQUEST = _descriptor.Descriptor(
  name='LibPageRequest',
  full_name='LibPageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='LibPageRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_results', full_name='LibPageRequest.max_results', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=356,
  serialized_end=407,
)


_RECOMMENDATIONREQUEST = _descriptor.Descriptor(
  name='RecommendationRequest',
  full_name='RecommendationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='RecommendationRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_results', full_name='RecommendationRequest.max_results', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='types', full_name='RecommendationRequest.types', index=2,
      number=3, type=14, cpp_type=8, label=3,
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
  serialized_start=409,
  serialized_end=492,
)


_SEARCHBYNAMEREQUEST = _descriptor.Descriptor(
  name='SearchByNameRequest',
  full_name='SearchByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SearchByNameRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_results', full_name='SearchByNameRequest.max_results', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='types', full_name='SearchByNameRequest.types', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=494,
  serialized_end=572,
)


_SEARCHBYCATEGORYREQUEST = _descriptor.Descriptor(
  name='SearchByCategoryRequest',
  full_name='SearchByCategoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='SearchByCategoryRequest.category', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_results', full_name='SearchByCategoryRequest.max_results', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='types', full_name='SearchByCategoryRequest.types', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=574,
  serialized_end=660,
)


_ADDITEMREQUEST = _descriptor.Descriptor(
  name='AddItemRequest',
  full_name='AddItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='book', full_name='AddItemRequest.book', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imdb', full_name='AddItemRequest.imdb', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='anime', full_name='AddItemRequest.anime', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='AddItemRequest.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
    _descriptor.OneofDescriptor(
      name='_book', full_name='AddItemRequest._book',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_imdb', full_name='AddItemRequest._imdb',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_anime', full_name='AddItemRequest._anime',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=663,
  serialized_end=820,
)


_ITEMID = _descriptor.Descriptor(
  name='ItemId',
  full_name='ItemId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ItemId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='ItemId.type', index=1,
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
  serialized_start=822,
  serialized_end=863,
)


_ITEMIDANDUSER = _descriptor.Descriptor(
  name='ItemIdAndUser',
  full_name='ItemIdAndUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ItemIdAndUser.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='ItemIdAndUser.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='ItemIdAndUser.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=865,
  serialized_end=930,
)

_ITEMINFORESPONSE.fields_by_name['recommendations'].message_type = _ITEMINFO
_ITEMINFO.fields_by_name['type'].enum_type = utils__pb2._TYPE
_ITEM.fields_by_name['book'].message_type = book__pb2._BOOKDATA
_ITEM.fields_by_name['imdb'].message_type = imdb__pb2._IMDBDATA
_ITEM.fields_by_name['anime'].message_type = anime__pb2._ANIMEDATA
_ITEM.oneofs_by_name['_book'].fields.append(
  _ITEM.fields_by_name['book'])
_ITEM.fields_by_name['book'].containing_oneof = _ITEM.oneofs_by_name['_book']
_ITEM.oneofs_by_name['_imdb'].fields.append(
  _ITEM.fields_by_name['imdb'])
_ITEM.fields_by_name['imdb'].containing_oneof = _ITEM.oneofs_by_name['_imdb']
_ITEM.oneofs_by_name['_anime'].fields.append(
  _ITEM.fields_by_name['anime'])
_ITEM.fields_by_name['anime'].containing_oneof = _ITEM.oneofs_by_name['_anime']
_RECOMMENDATIONREQUEST.fields_by_name['types'].enum_type = utils__pb2._TYPE
_SEARCHBYNAMEREQUEST.fields_by_name['types'].enum_type = utils__pb2._TYPE
_SEARCHBYCATEGORYREQUEST.fields_by_name['types'].enum_type = utils__pb2._TYPE
_ADDITEMREQUEST.fields_by_name['book'].message_type = book__pb2._BOOKDATA
_ADDITEMREQUEST.fields_by_name['imdb'].message_type = imdb__pb2._IMDBDATA
_ADDITEMREQUEST.fields_by_name['anime'].message_type = anime__pb2._ANIMEDATA
_ADDITEMREQUEST.fields_by_name['type'].enum_type = utils__pb2._TYPE
_ADDITEMREQUEST.oneofs_by_name['_book'].fields.append(
  _ADDITEMREQUEST.fields_by_name['book'])
_ADDITEMREQUEST.fields_by_name['book'].containing_oneof = _ADDITEMREQUEST.oneofs_by_name['_book']
_ADDITEMREQUEST.oneofs_by_name['_imdb'].fields.append(
  _ADDITEMREQUEST.fields_by_name['imdb'])
_ADDITEMREQUEST.fields_by_name['imdb'].containing_oneof = _ADDITEMREQUEST.oneofs_by_name['_imdb']
_ADDITEMREQUEST.oneofs_by_name['_anime'].fields.append(
  _ADDITEMREQUEST.fields_by_name['anime'])
_ADDITEMREQUEST.fields_by_name['anime'].containing_oneof = _ADDITEMREQUEST.oneofs_by_name['_anime']
_ITEMID.fields_by_name['type'].enum_type = utils__pb2._TYPE
_ITEMIDANDUSER.fields_by_name['type'].enum_type = utils__pb2._TYPE
DESCRIPTOR.message_types_by_name['ItemInfoResponse'] = _ITEMINFORESPONSE
DESCRIPTOR.message_types_by_name['ItemInfo'] = _ITEMINFO
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['LibPageRequest'] = _LIBPAGEREQUEST
DESCRIPTOR.message_types_by_name['RecommendationRequest'] = _RECOMMENDATIONREQUEST
DESCRIPTOR.message_types_by_name['SearchByNameRequest'] = _SEARCHBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['SearchByCategoryRequest'] = _SEARCHBYCATEGORYREQUEST
DESCRIPTOR.message_types_by_name['AddItemRequest'] = _ADDITEMREQUEST
DESCRIPTOR.message_types_by_name['ItemId'] = _ITEMID
DESCRIPTOR.message_types_by_name['ItemIdAndUser'] = _ITEMIDANDUSER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ItemInfoResponse = _reflection.GeneratedProtocolMessageType('ItemInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _ITEMINFORESPONSE,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:ItemInfoResponse)
  })
_sym_db.RegisterMessage(ItemInfoResponse)

ItemInfo = _reflection.GeneratedProtocolMessageType('ItemInfo', (_message.Message,), {
  'DESCRIPTOR' : _ITEMINFO,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:ItemInfo)
  })
_sym_db.RegisterMessage(ItemInfo)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:Item)
  })
_sym_db.RegisterMessage(Item)

LibPageRequest = _reflection.GeneratedProtocolMessageType('LibPageRequest', (_message.Message,), {
  'DESCRIPTOR' : _LIBPAGEREQUEST,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:LibPageRequest)
  })
_sym_db.RegisterMessage(LibPageRequest)

RecommendationRequest = _reflection.GeneratedProtocolMessageType('RecommendationRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDATIONREQUEST,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:RecommendationRequest)
  })
_sym_db.RegisterMessage(RecommendationRequest)

SearchByNameRequest = _reflection.GeneratedProtocolMessageType('SearchByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHBYNAMEREQUEST,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:SearchByNameRequest)
  })
_sym_db.RegisterMessage(SearchByNameRequest)

SearchByCategoryRequest = _reflection.GeneratedProtocolMessageType('SearchByCategoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHBYCATEGORYREQUEST,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:SearchByCategoryRequest)
  })
_sym_db.RegisterMessage(SearchByCategoryRequest)

AddItemRequest = _reflection.GeneratedProtocolMessageType('AddItemRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDITEMREQUEST,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:AddItemRequest)
  })
_sym_db.RegisterMessage(AddItemRequest)

ItemId = _reflection.GeneratedProtocolMessageType('ItemId', (_message.Message,), {
  'DESCRIPTOR' : _ITEMID,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:ItemId)
  })
_sym_db.RegisterMessage(ItemId)

ItemIdAndUser = _reflection.GeneratedProtocolMessageType('ItemIdAndUser', (_message.Message,), {
  'DESCRIPTOR' : _ITEMIDANDUSER,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:ItemIdAndUser)
  })
_sym_db.RegisterMessage(ItemIdAndUser)



_LIBRARY = _descriptor.ServiceDescriptor(
  name='Library',
  full_name='Library',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=933,
  serialized_end=1361,
  methods=[
  _descriptor.MethodDescriptor(
    name='Library',
    full_name='Library.Library',
    index=0,
    containing_service=None,
    input_type=_LIBPAGEREQUEST,
    output_type=_ITEMINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Recommend',
    full_name='Library.Recommend',
    index=1,
    containing_service=None,
    input_type=_RECOMMENDATIONREQUEST,
    output_type=_ITEMINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddItem',
    full_name='Library.AddItem',
    index=2,
    containing_service=None,
    input_type=_ADDITEMREQUEST,
    output_type=_ITEMID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetItem',
    full_name='Library.GetItem',
    index=3,
    containing_service=None,
    input_type=_ITEMID,
    output_type=_ITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveItem',
    full_name='Library.RemoveItem',
    index=4,
    containing_service=None,
    input_type=_ITEMID,
    output_type=utils__pb2._SUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddSeenItem',
    full_name='Library.AddSeenItem',
    index=5,
    containing_service=None,
    input_type=_ITEMIDANDUSER,
    output_type=utils__pb2._SUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveSeenItem',
    full_name='Library.RemoveSeenItem',
    index=6,
    containing_service=None,
    input_type=_ITEMIDANDUSER,
    output_type=utils__pb2._SUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddLikeItem',
    full_name='Library.AddLikeItem',
    index=7,
    containing_service=None,
    input_type=_ITEMIDANDUSER,
    output_type=utils__pb2._SUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveLikeItem',
    full_name='Library.RemoveLikeItem',
    index=8,
    containing_service=None,
    input_type=_ITEMIDANDUSER,
    output_type=utils__pb2._SUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTopTen',
    full_name='Library.GetTopTen',
    index=9,
    containing_service=None,
    input_type=account__pb2._TOPTENREQUEST,
    output_type=account__pb2._SEENSANDLIKESINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LIBRARY)

DESCRIPTOR.services_by_name['Library'] = _LIBRARY

# @@protoc_insertion_point(module_scope)
