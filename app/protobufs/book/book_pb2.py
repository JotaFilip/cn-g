# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='book.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nbook.proto\"z\n\x08\x42ookData\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\t\x12\x12\n\nbook_title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06genres\x18\x04 \x03(\t\x12\x13\n\x0b\x62ook_rating\x18\x05 \x01(\x01\x12\x0f\n\x07img_url\x18\x06 \x01(\t\"(\n\x0c\x42ookDataList\x12\x18\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\t.BookData\"\"\n\x0f\x42ookByIdRequest\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\t\"\'\n\x0c\x42ookResponse\x12\x17\n\x04\x62ook\x18\x01 \x01(\x0b\x32\t.BookData\"7\n\x12\x42ooksByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\"?\n\x16\x42ooksByCategoryRequest\x12\x10\n\x08\x63\x61tegory\x18\x01 \x03(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\x32\xa5\x01\n\x04\x42ook\x12-\n\nSearchById\x12\x10.BookByIdRequest\x1a\r.BookResponse\x12\x32\n\x0cSearchByName\x12\x13.BooksByNameRequest\x1a\r.BookDataList\x12:\n\x10SearchByCategory\x12\x17.BooksByCategoryRequest\x1a\r.BookDataListb\x06proto3'
)




_BOOKDATA = _descriptor.Descriptor(
  name='BookData',
  full_name='BookData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='book_id', full_name='BookData.book_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book_title', full_name='BookData.book_title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='BookData.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genres', full_name='BookData.genres', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book_rating', full_name='BookData.book_rating', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='img_url', full_name='BookData.img_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=14,
  serialized_end=136,
)


_BOOKDATALIST = _descriptor.Descriptor(
  name='BookDataList',
  full_name='BookDataList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='books', full_name='BookDataList.books', index=0,
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
  serialized_start=138,
  serialized_end=178,
)


_BOOKBYIDREQUEST = _descriptor.Descriptor(
  name='BookByIdRequest',
  full_name='BookByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='book_id', full_name='BookByIdRequest.book_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=180,
  serialized_end=214,
)


_BOOKRESPONSE = _descriptor.Descriptor(
  name='BookResponse',
  full_name='BookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='book', full_name='BookResponse.book', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=216,
  serialized_end=255,
)


_BOOKSBYNAMEREQUEST = _descriptor.Descriptor(
  name='BooksByNameRequest',
  full_name='BooksByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='BooksByNameRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_results', full_name='BooksByNameRequest.max_results', index=1,
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
  serialized_start=257,
  serialized_end=312,
)


_BOOKSBYCATEGORYREQUEST = _descriptor.Descriptor(
  name='BooksByCategoryRequest',
  full_name='BooksByCategoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='BooksByCategoryRequest.category', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_results', full_name='BooksByCategoryRequest.max_results', index=1,
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
  serialized_start=314,
  serialized_end=377,
)

_BOOKDATALIST.fields_by_name['books'].message_type = _BOOKDATA
_BOOKRESPONSE.fields_by_name['book'].message_type = _BOOKDATA
DESCRIPTOR.message_types_by_name['BookData'] = _BOOKDATA
DESCRIPTOR.message_types_by_name['BookDataList'] = _BOOKDATALIST
DESCRIPTOR.message_types_by_name['BookByIdRequest'] = _BOOKBYIDREQUEST
DESCRIPTOR.message_types_by_name['BookResponse'] = _BOOKRESPONSE
DESCRIPTOR.message_types_by_name['BooksByNameRequest'] = _BOOKSBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['BooksByCategoryRequest'] = _BOOKSBYCATEGORYREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BookData = _reflection.GeneratedProtocolMessageType('BookData', (_message.Message,), {
  'DESCRIPTOR' : _BOOKDATA,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:BookData)
  })
_sym_db.RegisterMessage(BookData)

BookDataList = _reflection.GeneratedProtocolMessageType('BookDataList', (_message.Message,), {
  'DESCRIPTOR' : _BOOKDATALIST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:BookDataList)
  })
_sym_db.RegisterMessage(BookDataList)

BookByIdRequest = _reflection.GeneratedProtocolMessageType('BookByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKBYIDREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:BookByIdRequest)
  })
_sym_db.RegisterMessage(BookByIdRequest)

BookResponse = _reflection.GeneratedProtocolMessageType('BookResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOOKRESPONSE,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:BookResponse)
  })
_sym_db.RegisterMessage(BookResponse)

BooksByNameRequest = _reflection.GeneratedProtocolMessageType('BooksByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKSBYNAMEREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:BooksByNameRequest)
  })
_sym_db.RegisterMessage(BooksByNameRequest)

BooksByCategoryRequest = _reflection.GeneratedProtocolMessageType('BooksByCategoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKSBYCATEGORYREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:BooksByCategoryRequest)
  })
_sym_db.RegisterMessage(BooksByCategoryRequest)



_BOOK = _descriptor.ServiceDescriptor(
  name='Book',
  full_name='Book',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=380,
  serialized_end=545,
  methods=[
  _descriptor.MethodDescriptor(
    name='SearchById',
    full_name='Book.SearchById',
    index=0,
    containing_service=None,
    input_type=_BOOKBYIDREQUEST,
    output_type=_BOOKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchByName',
    full_name='Book.SearchByName',
    index=1,
    containing_service=None,
    input_type=_BOOKSBYNAMEREQUEST,
    output_type=_BOOKDATALIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchByCategory',
    full_name='Book.SearchByCategory',
    index=2,
    containing_service=None,
    input_type=_BOOKSBYCATEGORYREQUEST,
    output_type=_BOOKDATALIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOK)

DESCRIPTOR.services_by_name['Book'] = _BOOK

# @@protoc_insertion_point(module_scope)
