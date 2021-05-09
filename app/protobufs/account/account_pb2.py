# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: account.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import utils_pb2 as utils__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='account.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\raccount.proto\x1a\x0butils.proto\"j\n\x08UserData\x12\x10\n\x08username\x18\x01 \x01(\t\x12%\n\x05likes\x18\x02 \x03(\x0b\x32\x16.SeenAndLikeInfoReturn\x12%\n\x05seens\x18\x03 \x03(\x0b\x32\x16.SeenAndLikeInfoReturn\"\x1e\n\x0bUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\":\n\x11UpdateUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x14\n\x0cnew_username\x18\x02 \x01(\t\"(\n\x14LikesAndViewsRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"W\n\x0fSeenAndLikeInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x13\n\x04type\x18\x03 \x01(\x0e\x32\x05.Type\x12\x12\n\ncategories\x18\x04 \x03(\t\"7\n\x12ViewsAndLikesCount\x12!\n\x06tuples\x18\x01 \x03(\x0b\x32\x11.TupleForCategory\"B\n\x10TupleForCategory\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\r\n\x05views\x18\x02 \x01(\x03\x12\r\n\x05likes\x18\x03 \x01(\x03\"8\n\x15SeenAndLikeInfoReturn\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x04type\x18\x02 \x01(\x0e\x32\x05.Type\"2\n\x0fSeenAndLikeItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x04type\x18\x02 \x01(\x0e\x32\x05.Type\":\n\x11SeensAndLikesInfo\x12%\n\x05infos\x18\x01 \x03(\x0b\x32\x16.SeenAndLikeInfoReturn\"\x14\n\x06UserId\x12\n\n\x02id\x18\x01 \x01(\t\"\x1a\n\tCountInfo\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\"\x16\n\x05\x43ount\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\"$\n\rTopTenRequest\x12\x13\n\x04type\x18\x01 \x01(\x0e\x32\x05.Type2\xe0\x03\n\x07\x41\x63\x63ount\x12\"\n\x04Seen\x12\x10.SeenAndLikeInfo\x1a\x08.Success\x12\"\n\x04Like\x12\x10.SeenAndLikeInfo\x1a\x08.Success\x12,\n\x0cGetLikesItem\x12\x10.SeenAndLikeItem\x1a\n.CountInfo\x12,\n\x0cGetSeensItem\x12\x10.SeenAndLikeItem\x1a\n.CountInfo\x12\x38\n\x18GetContagemLikesAndViews\x12\x07.UserId\x1a\x13.ViewsAndLikesCount\x12(\n\rGetUserByName\x12\x0c.UserRequest\x1a\t.UserData\x12*\n\nUpdateUser\x12\x12.UpdateUserRequest\x1a\x08.Success\x12$\n\nDeleteUser\x12\x0c.UserRequest\x1a\x08.Success\x12$\n\x08GetViews\x12\x10.SeenAndLikeItem\x1a\x06.Count\x12$\n\x08GetLikes\x12\x10.SeenAndLikeItem\x1a\x06.Count\x12/\n\tGetTopTen\x12\x0e.TopTenRequest\x1a\x12.SeensAndLikesInfob\x06proto3'
  ,
  dependencies=[utils__pb2.DESCRIPTOR,])




_USERDATA = _descriptor.Descriptor(
  name='UserData',
  full_name='UserData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='UserData.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='likes', full_name='UserData.likes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seens', full_name='UserData.seens', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=30,
  serialized_end=136,
)


_USERREQUEST = _descriptor.Descriptor(
  name='UserRequest',
  full_name='UserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='UserRequest.user_id', index=0,
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
  serialized_start=138,
  serialized_end=168,
)


_UPDATEUSERREQUEST = _descriptor.Descriptor(
  name='UpdateUserRequest',
  full_name='UpdateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='UpdateUserRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_username', full_name='UpdateUserRequest.new_username', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=170,
  serialized_end=228,
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
      name='username', full_name='LikesAndViewsRequest.username', index=0,
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
  serialized_start=230,
  serialized_end=270,
)


_SEENANDLIKEINFO = _descriptor.Descriptor(
  name='SeenAndLikeInfo',
  full_name='SeenAndLikeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SeenAndLikeInfo.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='SeenAndLikeInfo.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='SeenAndLikeInfo.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='categories', full_name='SeenAndLikeInfo.categories', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=272,
  serialized_end=359,
)


_VIEWSANDLIKESCOUNT = _descriptor.Descriptor(
  name='ViewsAndLikesCount',
  full_name='ViewsAndLikesCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tuples', full_name='ViewsAndLikesCount.tuples', index=0,
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
  serialized_start=361,
  serialized_end=416,
)


_TUPLEFORCATEGORY = _descriptor.Descriptor(
  name='TupleForCategory',
  full_name='TupleForCategory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='TupleForCategory.category', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='views', full_name='TupleForCategory.views', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='likes', full_name='TupleForCategory.likes', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=418,
  serialized_end=484,
)


_SEENANDLIKEINFORETURN = _descriptor.Descriptor(
  name='SeenAndLikeInfoReturn',
  full_name='SeenAndLikeInfoReturn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SeenAndLikeInfoReturn.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='SeenAndLikeInfoReturn.type', index=1,
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
  serialized_start=486,
  serialized_end=542,
)


_SEENANDLIKEITEM = _descriptor.Descriptor(
  name='SeenAndLikeItem',
  full_name='SeenAndLikeItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SeenAndLikeItem.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='SeenAndLikeItem.type', index=1,
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
  serialized_start=544,
  serialized_end=594,
)


_SEENSANDLIKESINFO = _descriptor.Descriptor(
  name='SeensAndLikesInfo',
  full_name='SeensAndLikesInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='infos', full_name='SeensAndLikesInfo.infos', index=0,
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
  serialized_start=596,
  serialized_end=654,
)


_USERID = _descriptor.Descriptor(
  name='UserId',
  full_name='UserId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UserId.id', index=0,
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
  serialized_start=656,
  serialized_end=676,
)


_COUNTINFO = _descriptor.Descriptor(
  name='CountInfo',
  full_name='CountInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='CountInfo.count', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=678,
  serialized_end=704,
)


_COUNT = _descriptor.Descriptor(
  name='Count',
  full_name='Count',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='Count.count', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=706,
  serialized_end=728,
)


_TOPTENREQUEST = _descriptor.Descriptor(
  name='TopTenRequest',
  full_name='TopTenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='TopTenRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=730,
  serialized_end=766,
)

_USERDATA.fields_by_name['likes'].message_type = _SEENANDLIKEINFORETURN
_USERDATA.fields_by_name['seens'].message_type = _SEENANDLIKEINFORETURN
_SEENANDLIKEINFO.fields_by_name['type'].enum_type = utils__pb2._TYPE
_VIEWSANDLIKESCOUNT.fields_by_name['tuples'].message_type = _TUPLEFORCATEGORY
_SEENANDLIKEINFORETURN.fields_by_name['type'].enum_type = utils__pb2._TYPE
_SEENANDLIKEITEM.fields_by_name['type'].enum_type = utils__pb2._TYPE
_SEENSANDLIKESINFO.fields_by_name['infos'].message_type = _SEENANDLIKEINFORETURN
_TOPTENREQUEST.fields_by_name['type'].enum_type = utils__pb2._TYPE
DESCRIPTOR.message_types_by_name['UserData'] = _USERDATA
DESCRIPTOR.message_types_by_name['UserRequest'] = _USERREQUEST
DESCRIPTOR.message_types_by_name['UpdateUserRequest'] = _UPDATEUSERREQUEST
DESCRIPTOR.message_types_by_name['LikesAndViewsRequest'] = _LIKESANDVIEWSREQUEST
DESCRIPTOR.message_types_by_name['SeenAndLikeInfo'] = _SEENANDLIKEINFO
DESCRIPTOR.message_types_by_name['ViewsAndLikesCount'] = _VIEWSANDLIKESCOUNT
DESCRIPTOR.message_types_by_name['TupleForCategory'] = _TUPLEFORCATEGORY
DESCRIPTOR.message_types_by_name['SeenAndLikeInfoReturn'] = _SEENANDLIKEINFORETURN
DESCRIPTOR.message_types_by_name['SeenAndLikeItem'] = _SEENANDLIKEITEM
DESCRIPTOR.message_types_by_name['SeensAndLikesInfo'] = _SEENSANDLIKESINFO
DESCRIPTOR.message_types_by_name['UserId'] = _USERID
DESCRIPTOR.message_types_by_name['CountInfo'] = _COUNTINFO
DESCRIPTOR.message_types_by_name['Count'] = _COUNT
DESCRIPTOR.message_types_by_name['TopTenRequest'] = _TOPTENREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserData = _reflection.GeneratedProtocolMessageType('UserData', (_message.Message,), {
  'DESCRIPTOR' : _USERDATA,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:UserData)
  })
_sym_db.RegisterMessage(UserData)

UserRequest = _reflection.GeneratedProtocolMessageType('UserRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERREQUEST,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:UserRequest)
  })
_sym_db.RegisterMessage(UserRequest)

UpdateUserRequest = _reflection.GeneratedProtocolMessageType('UpdateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERREQUEST,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:UpdateUserRequest)
  })
_sym_db.RegisterMessage(UpdateUserRequest)

LikesAndViewsRequest = _reflection.GeneratedProtocolMessageType('LikesAndViewsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LIKESANDVIEWSREQUEST,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:LikesAndViewsRequest)
  })
_sym_db.RegisterMessage(LikesAndViewsRequest)

SeenAndLikeInfo = _reflection.GeneratedProtocolMessageType('SeenAndLikeInfo', (_message.Message,), {
  'DESCRIPTOR' : _SEENANDLIKEINFO,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:SeenAndLikeInfo)
  })
_sym_db.RegisterMessage(SeenAndLikeInfo)

ViewsAndLikesCount = _reflection.GeneratedProtocolMessageType('ViewsAndLikesCount', (_message.Message,), {
  'DESCRIPTOR' : _VIEWSANDLIKESCOUNT,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:ViewsAndLikesCount)
  })
_sym_db.RegisterMessage(ViewsAndLikesCount)

TupleForCategory = _reflection.GeneratedProtocolMessageType('TupleForCategory', (_message.Message,), {
  'DESCRIPTOR' : _TUPLEFORCATEGORY,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:TupleForCategory)
  })
_sym_db.RegisterMessage(TupleForCategory)

SeenAndLikeInfoReturn = _reflection.GeneratedProtocolMessageType('SeenAndLikeInfoReturn', (_message.Message,), {
  'DESCRIPTOR' : _SEENANDLIKEINFORETURN,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:SeenAndLikeInfoReturn)
  })
_sym_db.RegisterMessage(SeenAndLikeInfoReturn)

SeenAndLikeItem = _reflection.GeneratedProtocolMessageType('SeenAndLikeItem', (_message.Message,), {
  'DESCRIPTOR' : _SEENANDLIKEITEM,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:SeenAndLikeItem)
  })
_sym_db.RegisterMessage(SeenAndLikeItem)

SeensAndLikesInfo = _reflection.GeneratedProtocolMessageType('SeensAndLikesInfo', (_message.Message,), {
  'DESCRIPTOR' : _SEENSANDLIKESINFO,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:SeensAndLikesInfo)
  })
_sym_db.RegisterMessage(SeensAndLikesInfo)

UserId = _reflection.GeneratedProtocolMessageType('UserId', (_message.Message,), {
  'DESCRIPTOR' : _USERID,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:UserId)
  })
_sym_db.RegisterMessage(UserId)

CountInfo = _reflection.GeneratedProtocolMessageType('CountInfo', (_message.Message,), {
  'DESCRIPTOR' : _COUNTINFO,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:CountInfo)
  })
_sym_db.RegisterMessage(CountInfo)

Count = _reflection.GeneratedProtocolMessageType('Count', (_message.Message,), {
  'DESCRIPTOR' : _COUNT,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:Count)
  })
_sym_db.RegisterMessage(Count)

TopTenRequest = _reflection.GeneratedProtocolMessageType('TopTenRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOPTENREQUEST,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:TopTenRequest)
  })
_sym_db.RegisterMessage(TopTenRequest)



_ACCOUNT = _descriptor.ServiceDescriptor(
  name='Account',
  full_name='Account',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=769,
  serialized_end=1249,
  methods=[
  _descriptor.MethodDescriptor(
    name='Seen',
    full_name='Account.Seen',
    index=0,
    containing_service=None,
    input_type=_SEENANDLIKEINFO,
    output_type=utils__pb2._SUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Like',
    full_name='Account.Like',
    index=1,
    containing_service=None,
    input_type=_SEENANDLIKEINFO,
    output_type=utils__pb2._SUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLikesItem',
    full_name='Account.GetLikesItem',
    index=2,
    containing_service=None,
    input_type=_SEENANDLIKEITEM,
    output_type=_COUNTINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSeensItem',
    full_name='Account.GetSeensItem',
    index=3,
    containing_service=None,
    input_type=_SEENANDLIKEITEM,
    output_type=_COUNTINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetContagemLikesAndViews',
    full_name='Account.GetContagemLikesAndViews',
    index=4,
    containing_service=None,
    input_type=_USERID,
    output_type=_VIEWSANDLIKESCOUNT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserByName',
    full_name='Account.GetUserByName',
    index=5,
    containing_service=None,
    input_type=_USERREQUEST,
    output_type=_USERDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateUser',
    full_name='Account.UpdateUser',
    index=6,
    containing_service=None,
    input_type=_UPDATEUSERREQUEST,
    output_type=utils__pb2._SUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteUser',
    full_name='Account.DeleteUser',
    index=7,
    containing_service=None,
    input_type=_USERREQUEST,
    output_type=utils__pb2._SUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetViews',
    full_name='Account.GetViews',
    index=8,
    containing_service=None,
    input_type=_SEENANDLIKEITEM,
    output_type=_COUNT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLikes',
    full_name='Account.GetLikes',
    index=9,
    containing_service=None,
    input_type=_SEENANDLIKEITEM,
    output_type=_COUNT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTopTen',
    full_name='Account.GetTopTen',
    index=10,
    containing_service=None,
    input_type=_TOPTENREQUEST,
    output_type=_SEENSANDLIKESINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNT)

DESCRIPTOR.services_by_name['Account'] = _ACCOUNT

# @@protoc_insertion_point(module_scope)
