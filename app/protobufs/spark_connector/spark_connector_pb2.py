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


import utils_pb2 as utils__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spark_connector.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15spark_connector.proto\x1a\x0butils.proto\"!\n\x0f\x45xecutionResult\x12\x0e\n\x06output\x18\x01 \x01(\t2\x87\x01\n\x0fSpark_Connector\x12G\n+GetPersonWhoWorkedWithMorePeopleToSameMovie\x12\x06.Empty\x1a\x10.ExecutionResult\x12+\n\x0fGetBestDirector\x12\x06.Empty\x1a\x10.ExecutionResultb\x06proto3'
  ,
  dependencies=[utils__pb2.DESCRIPTOR,])




_EXECUTIONRESULT = _descriptor.Descriptor(
  name='ExecutionResult',
  full_name='ExecutionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='output', full_name='ExecutionResult.output', index=0,
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
  serialized_start=38,
  serialized_end=71,
)

DESCRIPTOR.message_types_by_name['ExecutionResult'] = _EXECUTIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExecutionResult = _reflection.GeneratedProtocolMessageType('ExecutionResult', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTIONRESULT,
  '__module__' : 'spark_connector_pb2'
  # @@protoc_insertion_point(class_scope:ExecutionResult)
  })
_sym_db.RegisterMessage(ExecutionResult)



_SPARK_CONNECTOR = _descriptor.ServiceDescriptor(
  name='Spark_Connector',
  full_name='Spark_Connector',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=74,
  serialized_end=209,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPersonWhoWorkedWithMorePeopleToSameMovie',
    full_name='Spark_Connector.GetPersonWhoWorkedWithMorePeopleToSameMovie',
    index=0,
    containing_service=None,
    input_type=utils__pb2._EMPTY,
    output_type=_EXECUTIONRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBestDirector',
    full_name='Spark_Connector.GetBestDirector',
    index=1,
    containing_service=None,
    input_type=utils__pb2._EMPTY,
    output_type=_EXECUTIONRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPARK_CONNECTOR)

DESCRIPTOR.services_by_name['Spark_Connector'] = _SPARK_CONNECTOR

# @@protoc_insertion_point(module_scope)
