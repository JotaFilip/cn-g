# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: imdb.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='imdb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nimdb.proto\"T\n\x08IMDBData\x12\x0f\n\x07imdb_id\x18\x01 \x01(\t\x12\x12\n\nimdb_title\x18\x02 \x01(\t\x12\x0e\n\x06genres\x18\x03 \x01(\t\x12\x13\n\x0bimdb_rating\x18\x04 \x01(\x01\"\'\n\x0cIMDBDataList\x12\x17\n\x04imdb\x18\x01 \x03(\x0b\x32\t.IMDBData\"\"\n\x0fIMDBByIdRequest\x12\x0f\n\x07imdb_id\x18\x01 \x01(\t\"6\n\x11IMDBByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\">\n\x15IMDBByCategoryRequest\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\"\'\n\x0cIMDBResponse\x12\x17\n\x04imdb\x18\x01 \x01(\x0b\x32\t.IMDBData2\xa3\x01\n\x04IMDB\x12-\n\nSearchById\x12\x10.IMDBByIdRequest\x1a\r.IMDBResponse\x12\x31\n\x0cSearchByName\x12\x12.IMDBByNameRequest\x1a\r.IMDBDataList\x12\x39\n\x10SearchByCategory\x12\x16.IMDBByCategoryRequest\x1a\r.IMDBDataListb\x06proto3'
)




_IMDBDATA = _descriptor.Descriptor(
  name='IMDBData',
  full_name='IMDBData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='imdb_id', full_name='IMDBData.imdb_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imdb_title', full_name='IMDBData.imdb_title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genres', full_name='IMDBData.genres', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imdb_rating', full_name='IMDBData.imdb_rating', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_end=98,
)


_IMDBDATALIST = _descriptor.Descriptor(
  name='IMDBDataList',
  full_name='IMDBDataList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='imdb', full_name='IMDBDataList.imdb', index=0,
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
  serialized_start=100,
  serialized_end=139,
)


_IMDBBYIDREQUEST = _descriptor.Descriptor(
  name='IMDBByIdRequest',
  full_name='IMDBByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='imdb_id', full_name='IMDBByIdRequest.imdb_id', index=0,
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
  serialized_start=141,
  serialized_end=175,
)


_IMDBBYNAMEREQUEST = _descriptor.Descriptor(
  name='IMDBByNameRequest',
  full_name='IMDBByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='IMDBByNameRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_results', full_name='IMDBByNameRequest.max_results', index=1,
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
  serialized_start=177,
  serialized_end=231,
)


_IMDBBYCATEGORYREQUEST = _descriptor.Descriptor(
  name='IMDBByCategoryRequest',
  full_name='IMDBByCategoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='IMDBByCategoryRequest.category', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_results', full_name='IMDBByCategoryRequest.max_results', index=1,
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
  serialized_start=233,
  serialized_end=295,
)


_IMDBRESPONSE = _descriptor.Descriptor(
  name='IMDBResponse',
  full_name='IMDBResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='imdb', full_name='IMDBResponse.imdb', index=0,
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
  serialized_start=297,
  serialized_end=336,
)

_IMDBDATALIST.fields_by_name['imdb'].message_type = _IMDBDATA
_IMDBRESPONSE.fields_by_name['imdb'].message_type = _IMDBDATA
DESCRIPTOR.message_types_by_name['IMDBData'] = _IMDBDATA
DESCRIPTOR.message_types_by_name['IMDBDataList'] = _IMDBDATALIST
DESCRIPTOR.message_types_by_name['IMDBByIdRequest'] = _IMDBBYIDREQUEST
DESCRIPTOR.message_types_by_name['IMDBByNameRequest'] = _IMDBBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['IMDBByCategoryRequest'] = _IMDBBYCATEGORYREQUEST
DESCRIPTOR.message_types_by_name['IMDBResponse'] = _IMDBRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IMDBData = _reflection.GeneratedProtocolMessageType('IMDBData', (_message.Message,), {
  'DESCRIPTOR' : _IMDBDATA,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:IMDBData)
  })
_sym_db.RegisterMessage(IMDBData)

IMDBDataList = _reflection.GeneratedProtocolMessageType('IMDBDataList', (_message.Message,), {
  'DESCRIPTOR' : _IMDBDATALIST,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:IMDBDataList)
  })
_sym_db.RegisterMessage(IMDBDataList)

IMDBByIdRequest = _reflection.GeneratedProtocolMessageType('IMDBByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMDBBYIDREQUEST,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:IMDBByIdRequest)
  })
_sym_db.RegisterMessage(IMDBByIdRequest)

IMDBByNameRequest = _reflection.GeneratedProtocolMessageType('IMDBByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMDBBYNAMEREQUEST,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:IMDBByNameRequest)
  })
_sym_db.RegisterMessage(IMDBByNameRequest)

IMDBByCategoryRequest = _reflection.GeneratedProtocolMessageType('IMDBByCategoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMDBBYCATEGORYREQUEST,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:IMDBByCategoryRequest)
  })
_sym_db.RegisterMessage(IMDBByCategoryRequest)

IMDBResponse = _reflection.GeneratedProtocolMessageType('IMDBResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMDBRESPONSE,
  '__module__' : 'imdb_pb2'
  # @@protoc_insertion_point(class_scope:IMDBResponse)
  })
_sym_db.RegisterMessage(IMDBResponse)



_IMDB = _descriptor.ServiceDescriptor(
  name='IMDB',
  full_name='IMDB',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=339,
  serialized_end=502,
  methods=[
  _descriptor.MethodDescriptor(
    name='SearchById',
    full_name='IMDB.SearchById',
    index=0,
    containing_service=None,
    input_type=_IMDBBYIDREQUEST,
    output_type=_IMDBRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchByName',
    full_name='IMDB.SearchByName',
    index=1,
    containing_service=None,
    input_type=_IMDBBYNAMEREQUEST,
    output_type=_IMDBDATALIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchByCategory',
    full_name='IMDB.SearchByCategory',
    index=2,
    containing_service=None,
    input_type=_IMDBBYCATEGORYREQUEST,
    output_type=_IMDBDATALIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMDB)

DESCRIPTOR.services_by_name['IMDB'] = _IMDB

# @@protoc_insertion_point(module_scope)