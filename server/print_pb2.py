# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: print.proto

from google.protobuf import symbol_database as _symbol_database
from google.protobuf import reflection as _reflection
from google.protobuf import message as _message
from google.protobuf import descriptor as _descriptor
import sys
_b = sys.version_info[0] < 3 and (
    lambda x: x) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='print.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b('\n\x0bprint.proto\"\x90\x01\n\x0cPrintRequest\x12\x0e\n\x06\x63opies\x18\x01 \x01(\r\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12+\n\x07options\x18\x03 \x03(\x0b\x32\x1a.PrintRequest.OptionsEntry\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\" \n\rPrintResponse\x12\x0f\n\x07message\x18\x01 \x01(\t25\n\x07Printer\x12*\n\tPrintPage\x12\r.PrintRequest\x1a\x0e.PrintResponseb\x06proto3')
)


_PRINTREQUEST_OPTIONSENTRY = _descriptor.Descriptor(
    name='OptionsEntry',
    full_name='PrintRequest.OptionsEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='PrintRequest.OptionsEntry.key', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value', full_name='PrintRequest.OptionsEntry.value', index=1,
            number=2, type=9, cpp_type=9, label=1,
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
    serialized_options=_b('8\001'),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=114,
    serialized_end=160,
)

_PRINTREQUEST = _descriptor.Descriptor(
    name='PrintRequest',
    full_name='PrintRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='copies', full_name='PrintRequest.copies', index=0,
            number=1, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='destination', full_name='PrintRequest.destination', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='options', full_name='PrintRequest.options', index=2,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_PRINTREQUEST_OPTIONSENTRY, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=16,
    serialized_end=160,
)


_PRINTRESPONSE = _descriptor.Descriptor(
    name='PrintResponse',
    full_name='PrintResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='message', full_name='PrintResponse.message', index=0,
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
    serialized_start=162,
    serialized_end=194,
)

_PRINTREQUEST_OPTIONSENTRY.containing_type = _PRINTREQUEST
_PRINTREQUEST.fields_by_name['options'].message_type = _PRINTREQUEST_OPTIONSENTRY
DESCRIPTOR.message_types_by_name['PrintRequest'] = _PRINTREQUEST
DESCRIPTOR.message_types_by_name['PrintResponse'] = _PRINTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PrintRequest = _reflection.GeneratedProtocolMessageType('PrintRequest', (_message.Message,), {

    'OptionsEntry': _reflection.GeneratedProtocolMessageType('OptionsEntry', (_message.Message,), {
        'DESCRIPTOR': _PRINTREQUEST_OPTIONSENTRY,
        '__module__': 'print_pb2'
        # @@protoc_insertion_point(class_scope:PrintRequest.OptionsEntry)
    }),
    'DESCRIPTOR': _PRINTREQUEST,
    '__module__': 'print_pb2'
    # @@protoc_insertion_point(class_scope:PrintRequest)
})
_sym_db.RegisterMessage(PrintRequest)
_sym_db.RegisterMessage(PrintRequest.OptionsEntry)

PrintResponse = _reflection.GeneratedProtocolMessageType('PrintResponse', (_message.Message,), {
    'DESCRIPTOR': _PRINTRESPONSE,
    '__module__': 'print_pb2'
    # @@protoc_insertion_point(class_scope:PrintResponse)
})
_sym_db.RegisterMessage(PrintResponse)


_PRINTREQUEST_OPTIONSENTRY._options = None

_PRINTER = _descriptor.ServiceDescriptor(
    name='Printer',
    full_name='Printer',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=196,
    serialized_end=249,
    methods=[
        _descriptor.MethodDescriptor(
            name='PrintPage',
            full_name='Printer.PrintPage',
            index=0,
            containing_service=None,
            input_type=_PRINTREQUEST,
            output_type=_PRINTRESPONSE,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_PRINTER)

DESCRIPTOR.services_by_name['Printer'] = _PRINTER

# @@protoc_insertion_point(module_scope)
