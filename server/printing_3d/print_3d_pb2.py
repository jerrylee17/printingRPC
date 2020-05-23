# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: print_3d.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='print_3d.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0eprint_3d.proto\"j\n\x0ePrint3dRequest\x12\x13\n\x0bmember_name\x18\x01 \x01(\t\x12\x1d\n\x15print_volume_cubic_cm\x18\x02 \x01(\r\x12\x0e\n\x06\x63opies\x18\x03 \x01(\r\x12\x14\n\x0c\x65ncoded_file\x18\x04 \x01(\x0c\"\"\n\x0fPrint3dResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2?\n\tPrinter3d\x12\x32\n\rHandle3dPrint\x12\x0f.Print3dRequest\x1a\x10.Print3dResponseb\x06proto3')
)




_PRINT3DREQUEST = _descriptor.Descriptor(
  name='Print3dRequest',
  full_name='Print3dRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='member_name', full_name='Print3dRequest.member_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='print_volume_cubic_cm', full_name='Print3dRequest.print_volume_cubic_cm', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='copies', full_name='Print3dRequest.copies', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoded_file', full_name='Print3dRequest.encoded_file', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=124,
)


_PRINT3DRESPONSE = _descriptor.Descriptor(
  name='Print3dResponse',
  full_name='Print3dResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='Print3dResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=126,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['Print3dRequest'] = _PRINT3DREQUEST
DESCRIPTOR.message_types_by_name['Print3dResponse'] = _PRINT3DRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Print3dRequest = _reflection.GeneratedProtocolMessageType('Print3dRequest', (_message.Message,), {
  'DESCRIPTOR' : _PRINT3DREQUEST,
  '__module__' : 'print_3d_pb2'
  # @@protoc_insertion_point(class_scope:Print3dRequest)
  })
_sym_db.RegisterMessage(Print3dRequest)

Print3dResponse = _reflection.GeneratedProtocolMessageType('Print3dResponse', (_message.Message,), {
  'DESCRIPTOR' : _PRINT3DRESPONSE,
  '__module__' : 'print_3d_pb2'
  # @@protoc_insertion_point(class_scope:Print3dResponse)
  })
_sym_db.RegisterMessage(Print3dResponse)



_PRINTER3D = _descriptor.ServiceDescriptor(
  name='Printer3d',
  full_name='Printer3d',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=162,
  serialized_end=225,
  methods=[
  _descriptor.MethodDescriptor(
    name='Handle3dPrint',
    full_name='Printer3d.Handle3dPrint',
    index=0,
    containing_service=None,
    input_type=_PRINT3DREQUEST,
    output_type=_PRINT3DRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRINTER3D)

DESCRIPTOR.services_by_name['Printer3d'] = _PRINTER3D

# @@protoc_insertion_point(module_scope)