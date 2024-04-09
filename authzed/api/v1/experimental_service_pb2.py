# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authzed/api/v1/experimental_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from authzed.api.v1 import core_pb2 as authzed_dot_api_dot_v1_dot_core__pb2
from authzed.api.v1 import permission_service_pb2 as authzed_dot_api_dot_v1_dot_permission__service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)authzed/api/v1/experimental_service.proto\x12\x0e\x61uthzed.api.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17validate/validate.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x17google/rpc/status.proto\x1a\x19\x61uthzed/api/v1/core.proto\x1a\'authzed/api/v1/permission_service.proto\"\xb0\x01\n\x1a\x42ulkCheckPermissionRequest\x12=\n\x0b\x63onsistency\x18\x01 \x01(\x0b\x32\x1b.authzed.api.v1.ConsistencyR\x0b\x63onsistency\x12S\n\x05items\x18\x02 \x03(\x0b\x32..authzed.api.v1.BulkCheckPermissionRequestItemB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01R\x05items\"\xb6\x02\n\x1e\x42ulkCheckPermissionRequestItem\x12\x45\n\x08resource\x18\x01 \x01(\x0b\x32\x1f.authzed.api.v1.ObjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x08resource\x12J\n\npermission\x18\x02 \x01(\tB*\xfa\x42\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$R\npermission\x12\x44\n\x07subject\x18\x03 \x01(\x0b\x32 .authzed.api.v1.SubjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x07subject\x12;\n\x07\x63ontext\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\x07\x63ontext\"\xae\x01\n\x1b\x42ulkCheckPermissionResponse\x12\x41\n\nchecked_at\x18\x01 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\tcheckedAt\x12L\n\x05pairs\x18\x02 \x03(\x0b\x32\'.authzed.api.v1.BulkCheckPermissionPairB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01R\x05pairs\"\xe2\x01\n\x17\x42ulkCheckPermissionPair\x12H\n\x07request\x18\x01 \x01(\x0b\x32..authzed.api.v1.BulkCheckPermissionRequestItemR\x07request\x12\x45\n\x04item\x18\x02 \x01(\x0b\x32/.authzed.api.v1.BulkCheckPermissionResponseItemH\x00R\x04item\x12*\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x05\x65rrorB\n\n\x08response\"\xea\x01\n\x1f\x42ulkCheckPermissionResponseItem\x12j\n\x0epermissionship\x18\x01 \x01(\x0e\x32\x36.authzed.api.v1.CheckPermissionResponse.PermissionshipB\n\xfa\x42\x07\x82\x01\x04\x10\x01 \x00R\x0epermissionship\x12[\n\x13partial_caveat_info\x18\x02 \x01(\x0b\x32!.authzed.api.v1.PartialCaveatInfoB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\x11partialCaveatInfo\"s\n\x1e\x42ulkImportRelationshipsRequest\x12Q\n\rrelationships\x18\x01 \x03(\x0b\x32\x1c.authzed.api.v1.RelationshipB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01R\rrelationships\"@\n\x1f\x42ulkImportRelationshipsResponse\x12\x1d\n\nnum_loaded\x18\x01 \x01(\x04R\tnumLoaded\"\xb9\x02\n\x1e\x42ulkExportRelationshipsRequest\x12=\n\x0b\x63onsistency\x18\x01 \x01(\x0b\x32\x1b.authzed.api.v1.ConsistencyR\x0b\x63onsistency\x12\x31\n\x0eoptional_limit\x18\x02 \x01(\rB\n\xfa\x42\x07*\x05\x18\x90N(\x00R\roptionalLimit\x12?\n\x0foptional_cursor\x18\x03 \x01(\x0b\x32\x16.authzed.api.v1.CursorR\x0eoptionalCursor\x12\x64\n\x1coptional_relationship_filter\x18\x04 \x01(\x0b\x32\".authzed.api.v1.RelationshipFilterR\x1aoptionalRelationshipFilter\"\xad\x01\n\x1f\x42ulkExportRelationshipsResponse\x12\x46\n\x13\x61\x66ter_result_cursor\x18\x01 \x01(\x0b\x32\x16.authzed.api.v1.CursorR\x11\x61\x66terResultCursor\x12\x42\n\rrelationships\x18\x02 \x03(\x0b\x32\x1c.authzed.api.v1.RelationshipR\rrelationships2\xad\x04\n\x13\x45xperimentalService\x12\xb2\x01\n\x17\x42ulkImportRelationships\x12..authzed.api.v1.BulkImportRelationshipsRequest\x1a/.authzed.api.v1.BulkImportRelationshipsResponse\"4\x82\xd3\xe4\x93\x02.\")/v1/experimental/relationships/bulkimport:\x01*(\x01\x12\xb2\x01\n\x17\x42ulkExportRelationships\x12..authzed.api.v1.BulkExportRelationshipsRequest\x1a/.authzed.api.v1.BulkExportRelationshipsResponse\"4\x82\xd3\xe4\x93\x02.\")/v1/experimental/relationships/bulkexport:\x01*0\x01\x12\xab\x01\n\x13\x42ulkCheckPermission\x12*.authzed.api.v1.BulkCheckPermissionRequest\x1a+.authzed.api.v1.BulkCheckPermissionResponse\";\x82\xd3\xe4\x93\x02\x35\"0/v1/experimental/permissions/bulkcheckpermission:\x01*BH\n\x12\x63om.authzed.api.v1Z2github.com/authzed/authzed-go/proto/authzed/api/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authzed.api.v1.experimental_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\022com.authzed.api.v1Z2github.com/authzed/authzed-go/proto/authzed/api/v1'
  _globals['_BULKCHECKPERMISSIONREQUEST'].fields_by_name['items']._loaded_options = None
  _globals['_BULKCHECKPERMISSIONREQUEST'].fields_by_name['items']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _globals['_BULKCHECKPERMISSIONREQUESTITEM'].fields_by_name['resource']._loaded_options = None
  _globals['_BULKCHECKPERMISSIONREQUESTITEM'].fields_by_name['resource']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_BULKCHECKPERMISSIONREQUESTITEM'].fields_by_name['permission']._loaded_options = None
  _globals['_BULKCHECKPERMISSIONREQUESTITEM'].fields_by_name['permission']._serialized_options = b'\372B\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$'
  _globals['_BULKCHECKPERMISSIONREQUESTITEM'].fields_by_name['subject']._loaded_options = None
  _globals['_BULKCHECKPERMISSIONREQUESTITEM'].fields_by_name['subject']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_BULKCHECKPERMISSIONREQUESTITEM'].fields_by_name['context']._loaded_options = None
  _globals['_BULKCHECKPERMISSIONREQUESTITEM'].fields_by_name['context']._serialized_options = b'\372B\005\212\001\002\020\000'
  _globals['_BULKCHECKPERMISSIONRESPONSE'].fields_by_name['checked_at']._loaded_options = None
  _globals['_BULKCHECKPERMISSIONRESPONSE'].fields_by_name['checked_at']._serialized_options = b'\372B\005\212\001\002\020\000'
  _globals['_BULKCHECKPERMISSIONRESPONSE'].fields_by_name['pairs']._loaded_options = None
  _globals['_BULKCHECKPERMISSIONRESPONSE'].fields_by_name['pairs']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _globals['_BULKCHECKPERMISSIONRESPONSEITEM'].fields_by_name['permissionship']._loaded_options = None
  _globals['_BULKCHECKPERMISSIONRESPONSEITEM'].fields_by_name['permissionship']._serialized_options = b'\372B\007\202\001\004\020\001 \000'
  _globals['_BULKCHECKPERMISSIONRESPONSEITEM'].fields_by_name['partial_caveat_info']._loaded_options = None
  _globals['_BULKCHECKPERMISSIONRESPONSEITEM'].fields_by_name['partial_caveat_info']._serialized_options = b'\372B\005\212\001\002\020\000'
  _globals['_BULKIMPORTRELATIONSHIPSREQUEST'].fields_by_name['relationships']._loaded_options = None
  _globals['_BULKIMPORTRELATIONSHIPSREQUEST'].fields_by_name['relationships']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _globals['_BULKEXPORTRELATIONSHIPSREQUEST'].fields_by_name['optional_limit']._loaded_options = None
  _globals['_BULKEXPORTRELATIONSHIPSREQUEST'].fields_by_name['optional_limit']._serialized_options = b'\372B\007*\005\030\220N(\000'
  _globals['_EXPERIMENTALSERVICE'].methods_by_name['BulkImportRelationships']._loaded_options = None
  _globals['_EXPERIMENTALSERVICE'].methods_by_name['BulkImportRelationships']._serialized_options = b'\202\323\344\223\002.\")/v1/experimental/relationships/bulkimport:\001*'
  _globals['_EXPERIMENTALSERVICE'].methods_by_name['BulkExportRelationships']._loaded_options = None
  _globals['_EXPERIMENTALSERVICE'].methods_by_name['BulkExportRelationships']._serialized_options = b'\202\323\344\223\002.\")/v1/experimental/relationships/bulkexport:\001*'
  _globals['_EXPERIMENTALSERVICE'].methods_by_name['BulkCheckPermission']._loaded_options = None
  _globals['_EXPERIMENTALSERVICE'].methods_by_name['BulkCheckPermission']._serialized_options = b'\202\323\344\223\0025\"0/v1/experimental/permissions/bulkcheckpermission:\001*'
  _globals['_BULKCHECKPERMISSIONREQUEST']._serialized_start=240
  _globals['_BULKCHECKPERMISSIONREQUEST']._serialized_end=416
  _globals['_BULKCHECKPERMISSIONREQUESTITEM']._serialized_start=419
  _globals['_BULKCHECKPERMISSIONREQUESTITEM']._serialized_end=729
  _globals['_BULKCHECKPERMISSIONRESPONSE']._serialized_start=732
  _globals['_BULKCHECKPERMISSIONRESPONSE']._serialized_end=906
  _globals['_BULKCHECKPERMISSIONPAIR']._serialized_start=909
  _globals['_BULKCHECKPERMISSIONPAIR']._serialized_end=1135
  _globals['_BULKCHECKPERMISSIONRESPONSEITEM']._serialized_start=1138
  _globals['_BULKCHECKPERMISSIONRESPONSEITEM']._serialized_end=1372
  _globals['_BULKIMPORTRELATIONSHIPSREQUEST']._serialized_start=1374
  _globals['_BULKIMPORTRELATIONSHIPSREQUEST']._serialized_end=1489
  _globals['_BULKIMPORTRELATIONSHIPSRESPONSE']._serialized_start=1491
  _globals['_BULKIMPORTRELATIONSHIPSRESPONSE']._serialized_end=1555
  _globals['_BULKEXPORTRELATIONSHIPSREQUEST']._serialized_start=1558
  _globals['_BULKEXPORTRELATIONSHIPSREQUEST']._serialized_end=1871
  _globals['_BULKEXPORTRELATIONSHIPSRESPONSE']._serialized_start=1874
  _globals['_BULKEXPORTRELATIONSHIPSRESPONSE']._serialized_end=2047
  _globals['_EXPERIMENTALSERVICE']._serialized_start=2050
  _globals['_EXPERIMENTALSERVICE']._serialized_end=2607
# @@protoc_insertion_point(module_scope)
