# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark_connector.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spark_connector.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15spark_connector.proto\"\n\n\x08\x44irector\"\x07\n\x05\x41\x63tor\"4\n\x0c\x44irectorWork\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x06movies\x18\x02 \x03(\x0b\x32\x06.Movie\"%\n\x05Movie\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tors\x18\x02 \x03(\t\"\x19\n\tActorName\x12\x0c\n\x04name\x18\x01 \x01(\t2d\n\x0fSpark_Connector\x12+\n\x0fGetDirectorWork\x12\t.Director\x1a\r.DirectorWork\x12$\n\x0eGetFamousActor\x12\x06.Actor\x1a\n.ActorNameb\x06proto3'
)




_DIRECTOR = _descriptor.Descriptor(
  name='Director',
  full_name='Director',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=25,
  serialized_end=35,
)


_ACTOR = _descriptor.Descriptor(
  name='Actor',
  full_name='Actor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=37,
  serialized_end=44,
)


_DIRECTORWORK = _descriptor.Descriptor(
  name='DirectorWork',
  full_name='DirectorWork',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DirectorWork.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='movies', full_name='DirectorWork.movies', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=46,
  serialized_end=98,
)


_MOVIE = _descriptor.Descriptor(
  name='Movie',
  full_name='Movie',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Movie.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actors', full_name='Movie.actors', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_end=137,
)


_ACTORNAME = _descriptor.Descriptor(
  name='ActorName',
  full_name='ActorName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ActorName.name', index=0,
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
  serialized_start=139,
  serialized_end=164,
)

_DIRECTORWORK.fields_by_name['movies'].message_type = _MOVIE
DESCRIPTOR.message_types_by_name['Director'] = _DIRECTOR
DESCRIPTOR.message_types_by_name['Actor'] = _ACTOR
DESCRIPTOR.message_types_by_name['DirectorWork'] = _DIRECTORWORK
DESCRIPTOR.message_types_by_name['Movie'] = _MOVIE
DESCRIPTOR.message_types_by_name['ActorName'] = _ACTORNAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Director = _reflection.GeneratedProtocolMessageType('Director', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTOR,
  '__module__' : 'spark_connector_pb2'
  # @@protoc_insertion_point(class_scope:Director)
  })
_sym_db.RegisterMessage(Director)

Actor = _reflection.GeneratedProtocolMessageType('Actor', (_message.Message,), {
  'DESCRIPTOR' : _ACTOR,
  '__module__' : 'spark_connector_pb2'
  # @@protoc_insertion_point(class_scope:Actor)
  })
_sym_db.RegisterMessage(Actor)

DirectorWork = _reflection.GeneratedProtocolMessageType('DirectorWork', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTORWORK,
  '__module__' : 'spark_connector_pb2'
  # @@protoc_insertion_point(class_scope:DirectorWork)
  })
_sym_db.RegisterMessage(DirectorWork)

Movie = _reflection.GeneratedProtocolMessageType('Movie', (_message.Message,), {
  'DESCRIPTOR' : _MOVIE,
  '__module__' : 'spark_connector_pb2'
  # @@protoc_insertion_point(class_scope:Movie)
  })
_sym_db.RegisterMessage(Movie)

ActorName = _reflection.GeneratedProtocolMessageType('ActorName', (_message.Message,), {
  'DESCRIPTOR' : _ACTORNAME,
  '__module__' : 'spark_connector_pb2'
  # @@protoc_insertion_point(class_scope:ActorName)
  })
_sym_db.RegisterMessage(ActorName)



_SPARK_CONNECTOR = _descriptor.ServiceDescriptor(
  name='Spark_Connector',
  full_name='Spark_Connector',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=166,
  serialized_end=266,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetDirectorWork',
    full_name='Spark_Connector.GetDirectorWork',
    index=0,
    containing_service=None,
    input_type=_DIRECTOR,
    output_type=_DIRECTORWORK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetFamousActor',
    full_name='Spark_Connector.GetFamousActor',
    index=1,
    containing_service=None,
    input_type=_ACTOR,
    output_type=_ACTORNAME,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPARK_CONNECTOR)

DESCRIPTOR.services_by_name['Spark_Connector'] = _SPARK_CONNECTOR

# @@protoc_insertion_point(module_scope)
