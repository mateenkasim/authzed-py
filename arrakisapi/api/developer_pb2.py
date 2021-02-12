# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arrakisapi/api/developer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from arrakisapi.api import core_pb2 as arrakisapi_dot_api_dot_core__pb2
from arrakisapi.api import namespace_pb2 as arrakisapi_dot_api_dot_namespace__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='arrakisapi/api/developer.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z$github.com/petricorp/code/arrakisapi',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x61rrakisapi/api/developer.proto\x1a\x19\x61rrakisapi/api/core.proto\x1a\x1e\x61rrakisapi/api/namespace.proto\"2\n\x10NamespaceContext\x12\x0e\n\x06handle\x18\x01 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x02 \x01(\t\"W\n\x0eRequestContext\x12%\n\nnamespaces\x18\x01 \x03(\x0b\x32\x11.NamespaceContext\x12\x1e\n\x06tuples\x18\x02 \x03(\x0b\x32\x0e.RelationTuple\"L\n\x0fValidateRequest\x12 \n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x0f.RequestContext\x12\x17\n\x0fvalidation_yaml\x18\x03 \x01(\t\"\xbe\x03\n\x0fValidationError\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04line\x18\x02 \x01(\r\x12\x0e\n\x06\x63olumn\x18\x03 \x01(\r\x12\'\n\x06source\x18\x04 \x01(\x0e\x32\x17.ValidationError.Source\x12(\n\x04kind\x18\x05 \x01(\x0e\x32\x1a.ValidationError.ErrorKind\x12\x0c\n\x04path\x18\x06 \x03(\t\x12\x10\n\x08metadata\x18\x07 \x01(\t\"]\n\x06Source\x12\x12\n\x0eUNKNOWN_SOURCE\x10\x00\x12\x14\n\x10NAMESPACE_CONFIG\x10\x01\x12\x14\n\x10VALIDATION_TUPLE\x10\x02\x12\x13\n\x0fVALIDATION_YAML\x10\x03\"\xa9\x01\n\tErrorKind\x12\x10\n\x0cUNKNOWN_KIND\x10\x00\x12\x0f\n\x0bPARSE_ERROR\x10\x01\x12\x1a\n\x16NAMESPACE_CONFIG_ISSUE\x10\x02\x12\x13\n\x0f\x44UPLICATE_TUPLE\x10\x03\x12\x1a\n\x16MISSING_EXPECTED_TUPLE\x10\x04\x12\x15\n\x11\x45XTRA_TUPLE_FOUND\x10\x05\x12\x15\n\x11UNKNOWN_NAMESPACE\x10\x06\"\xf3\x01\n\x10ValidateResponse\x12\x42\n\x12\x63ontext_namespaces\x18\x01 \x03(\x0b\x32&.ValidateResponse.NamespaceInformation\x12+\n\x11validation_errors\x18\x02 \x03(\x0b\x32\x10.ValidationError\x1an\n\x14NamespaceInformation\x12\x0e\n\x06handle\x18\x01 \x01(\t\x12$\n\x06parsed\x18\x02 \x01(\x0b\x32\x14.NamespaceDefinition\x12 \n\x06\x65rrors\x18\x03 \x03(\x0b\x32\x10.ValidationError2E\n\x10\x44\x65veloperService\x12\x31\n\x08Validate\x12\x10.ValidateRequest\x1a\x11.ValidateResponse\"\x00\x42&Z$github.com/petricorp/code/arrakisapib\x06proto3'
  ,
  dependencies=[arrakisapi_dot_api_dot_core__pb2.DESCRIPTOR,arrakisapi_dot_api_dot_namespace__pb2.DESCRIPTOR,])



_VALIDATIONERROR_SOURCE = _descriptor.EnumDescriptor(
  name='Source',
  full_name='ValidationError.Source',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_SOURCE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NAMESPACE_CONFIG', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VALIDATION_TUPLE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VALIDATION_YAML', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=494,
  serialized_end=587,
)
_sym_db.RegisterEnumDescriptor(_VALIDATIONERROR_SOURCE)

_VALIDATIONERROR_ERRORKIND = _descriptor.EnumDescriptor(
  name='ErrorKind',
  full_name='ValidationError.ErrorKind',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_KIND', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PARSE_ERROR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NAMESPACE_CONFIG_ISSUE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_TUPLE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MISSING_EXPECTED_TUPLE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXTRA_TUPLE_FOUND', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_NAMESPACE', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=590,
  serialized_end=759,
)
_sym_db.RegisterEnumDescriptor(_VALIDATIONERROR_ERRORKIND)


_NAMESPACECONTEXT = _descriptor.Descriptor(
  name='NamespaceContext',
  full_name='NamespaceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='handle', full_name='NamespaceContext.handle', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='NamespaceContext.config', index=1,
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
  serialized_start=93,
  serialized_end=143,
)


_REQUESTCONTEXT = _descriptor.Descriptor(
  name='RequestContext',
  full_name='RequestContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespaces', full_name='RequestContext.namespaces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tuples', full_name='RequestContext.tuples', index=1,
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
  serialized_start=145,
  serialized_end=232,
)


_VALIDATEREQUEST = _descriptor.Descriptor(
  name='ValidateRequest',
  full_name='ValidateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='ValidateRequest.context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validation_yaml', full_name='ValidateRequest.validation_yaml', index=1,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=234,
  serialized_end=310,
)


_VALIDATIONERROR = _descriptor.Descriptor(
  name='ValidationError',
  full_name='ValidationError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='ValidationError.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line', full_name='ValidationError.line', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column', full_name='ValidationError.column', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='ValidationError.source', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kind', full_name='ValidationError.kind', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='ValidationError.path', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ValidationError.metadata', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VALIDATIONERROR_SOURCE,
    _VALIDATIONERROR_ERRORKIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=759,
)


_VALIDATERESPONSE_NAMESPACEINFORMATION = _descriptor.Descriptor(
  name='NamespaceInformation',
  full_name='ValidateResponse.NamespaceInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='handle', full_name='ValidateResponse.NamespaceInformation.handle', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parsed', full_name='ValidateResponse.NamespaceInformation.parsed', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errors', full_name='ValidateResponse.NamespaceInformation.errors', index=2,
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
  serialized_start=895,
  serialized_end=1005,
)

_VALIDATERESPONSE = _descriptor.Descriptor(
  name='ValidateResponse',
  full_name='ValidateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='context_namespaces', full_name='ValidateResponse.context_namespaces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validation_errors', full_name='ValidateResponse.validation_errors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_VALIDATERESPONSE_NAMESPACEINFORMATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=762,
  serialized_end=1005,
)

_REQUESTCONTEXT.fields_by_name['namespaces'].message_type = _NAMESPACECONTEXT
_REQUESTCONTEXT.fields_by_name['tuples'].message_type = arrakisapi_dot_api_dot_core__pb2._RELATIONTUPLE
_VALIDATEREQUEST.fields_by_name['context'].message_type = _REQUESTCONTEXT
_VALIDATIONERROR.fields_by_name['source'].enum_type = _VALIDATIONERROR_SOURCE
_VALIDATIONERROR.fields_by_name['kind'].enum_type = _VALIDATIONERROR_ERRORKIND
_VALIDATIONERROR_SOURCE.containing_type = _VALIDATIONERROR
_VALIDATIONERROR_ERRORKIND.containing_type = _VALIDATIONERROR
_VALIDATERESPONSE_NAMESPACEINFORMATION.fields_by_name['parsed'].message_type = arrakisapi_dot_api_dot_namespace__pb2._NAMESPACEDEFINITION
_VALIDATERESPONSE_NAMESPACEINFORMATION.fields_by_name['errors'].message_type = _VALIDATIONERROR
_VALIDATERESPONSE_NAMESPACEINFORMATION.containing_type = _VALIDATERESPONSE
_VALIDATERESPONSE.fields_by_name['context_namespaces'].message_type = _VALIDATERESPONSE_NAMESPACEINFORMATION
_VALIDATERESPONSE.fields_by_name['validation_errors'].message_type = _VALIDATIONERROR
DESCRIPTOR.message_types_by_name['NamespaceContext'] = _NAMESPACECONTEXT
DESCRIPTOR.message_types_by_name['RequestContext'] = _REQUESTCONTEXT
DESCRIPTOR.message_types_by_name['ValidateRequest'] = _VALIDATEREQUEST
DESCRIPTOR.message_types_by_name['ValidationError'] = _VALIDATIONERROR
DESCRIPTOR.message_types_by_name['ValidateResponse'] = _VALIDATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NamespaceContext = _reflection.GeneratedProtocolMessageType('NamespaceContext', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACECONTEXT,
  '__module__' : 'arrakisapi.api.developer_pb2'
  # @@protoc_insertion_point(class_scope:NamespaceContext)
  })
_sym_db.RegisterMessage(NamespaceContext)

RequestContext = _reflection.GeneratedProtocolMessageType('RequestContext', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCONTEXT,
  '__module__' : 'arrakisapi.api.developer_pb2'
  # @@protoc_insertion_point(class_scope:RequestContext)
  })
_sym_db.RegisterMessage(RequestContext)

ValidateRequest = _reflection.GeneratedProtocolMessageType('ValidateRequest', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATEREQUEST,
  '__module__' : 'arrakisapi.api.developer_pb2'
  # @@protoc_insertion_point(class_scope:ValidateRequest)
  })
_sym_db.RegisterMessage(ValidateRequest)

ValidationError = _reflection.GeneratedProtocolMessageType('ValidationError', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATIONERROR,
  '__module__' : 'arrakisapi.api.developer_pb2'
  # @@protoc_insertion_point(class_scope:ValidationError)
  })
_sym_db.RegisterMessage(ValidationError)

ValidateResponse = _reflection.GeneratedProtocolMessageType('ValidateResponse', (_message.Message,), {

  'NamespaceInformation' : _reflection.GeneratedProtocolMessageType('NamespaceInformation', (_message.Message,), {
    'DESCRIPTOR' : _VALIDATERESPONSE_NAMESPACEINFORMATION,
    '__module__' : 'arrakisapi.api.developer_pb2'
    # @@protoc_insertion_point(class_scope:ValidateResponse.NamespaceInformation)
    })
  ,
  'DESCRIPTOR' : _VALIDATERESPONSE,
  '__module__' : 'arrakisapi.api.developer_pb2'
  # @@protoc_insertion_point(class_scope:ValidateResponse)
  })
_sym_db.RegisterMessage(ValidateResponse)
_sym_db.RegisterMessage(ValidateResponse.NamespaceInformation)


DESCRIPTOR._options = None

_DEVELOPERSERVICE = _descriptor.ServiceDescriptor(
  name='DeveloperService',
  full_name='DeveloperService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1007,
  serialized_end=1076,
  methods=[
  _descriptor.MethodDescriptor(
    name='Validate',
    full_name='DeveloperService.Validate',
    index=0,
    containing_service=None,
    input_type=_VALIDATEREQUEST,
    output_type=_VALIDATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEVELOPERSERVICE)

DESCRIPTOR.services_by_name['DeveloperService'] = _DEVELOPERSERVICE

# @@protoc_insertion_point(module_scope)