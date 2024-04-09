# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authzed/api/v1/debug.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from authzed.api.v1 import core_pb2 as authzed_dot_api_dot_v1_dot_core__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x61uthzed/api/v1/debug.proto\x12\x0e\x61uthzed.api.v1\x1a\x19\x61uthzed/api/v1/core.proto\x1a\x17validate/validate.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/duration.proto\"j\n\x10\x44\x65\x62ugInformation\x12\x35\n\x05\x63heck\x18\x01 \x01(\x0b\x32\x1f.authzed.api.v1.CheckDebugTraceR\x05\x63heck\x12\x1f\n\x0bschema_used\x18\x02 \x01(\tR\nschemaUsed\"\xf3\x07\n\x0f\x43heckDebugTrace\x12\x45\n\x08resource\x18\x01 \x01(\x0b\x32\x1f.authzed.api.v1.ObjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x08resource\x12\x1e\n\npermission\x18\x02 \x01(\tR\npermission\x12\x63\n\x0fpermission_type\x18\x03 \x01(\x0e\x32..authzed.api.v1.CheckDebugTrace.PermissionTypeB\n\xfa\x42\x07\x82\x01\x04\x10\x01 \x00R\x0epermissionType\x12\x44\n\x07subject\x18\x04 \x01(\x0b\x32 .authzed.api.v1.SubjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x07subject\x12R\n\x06result\x18\x05 \x01(\x0e\x32..authzed.api.v1.CheckDebugTrace.PermissionshipB\n\xfa\x42\x07\x82\x01\x04\x10\x01 \x00R\x06result\x12T\n\x16\x63\x61veat_evaluation_info\x18\x08 \x01(\x0b\x32\x1e.authzed.api.v1.CaveatEvalInfoR\x14\x63\x61veatEvaluationInfo\x12\x35\n\x08\x64uration\x18\t \x01(\x0b\x32\x19.google.protobuf.DurationR\x08\x64uration\x12,\n\x11was_cached_result\x18\x06 \x01(\x08H\x00R\x0fwasCachedResult\x12P\n\x0csub_problems\x18\x07 \x01(\x0b\x32+.authzed.api.v1.CheckDebugTrace.SubProblemsH\x00R\x0bsubProblems\x1a\x46\n\x0bSubProblems\x12\x37\n\x06traces\x18\x01 \x03(\x0b\x32\x1f.authzed.api.v1.CheckDebugTraceR\x06traces\"o\n\x0ePermissionType\x12\x1f\n\x1bPERMISSION_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18PERMISSION_TYPE_RELATION\x10\x01\x12\x1e\n\x1aPERMISSION_TYPE_PERMISSION\x10\x02\"\xa0\x01\n\x0ePermissionship\x12\x1e\n\x1aPERMISSIONSHIP_UNSPECIFIED\x10\x00\x12 \n\x1cPERMISSIONSHIP_NO_PERMISSION\x10\x01\x12!\n\x1dPERMISSIONSHIP_HAS_PERMISSION\x10\x02\x12)\n%PERMISSIONSHIP_CONDITIONAL_PERMISSION\x10\x03\x42\x11\n\nresolution\x12\x03\xf8\x42\x01\"\x94\x03\n\x0e\x43\x61veatEvalInfo\x12\x1e\n\nexpression\x18\x01 \x01(\tR\nexpression\x12=\n\x06result\x18\x02 \x01(\x0e\x32%.authzed.api.v1.CaveatEvalInfo.ResultR\x06result\x12\x31\n\x07\x63ontext\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructR\x07\x63ontext\x12Q\n\x13partial_caveat_info\x18\x04 \x01(\x0b\x32!.authzed.api.v1.PartialCaveatInfoR\x11partialCaveatInfo\x12\x1f\n\x0b\x63\x61veat_name\x18\x05 \x01(\tR\ncaveatName\"|\n\x06Result\x12\x16\n\x12RESULT_UNSPECIFIED\x10\x00\x12\x16\n\x12RESULT_UNEVALUATED\x10\x01\x12\x10\n\x0cRESULT_FALSE\x10\x02\x12\x0f\n\x0bRESULT_TRUE\x10\x03\x12\x1f\n\x1bRESULT_MISSING_SOME_CONTEXT\x10\x04\x42H\n\x12\x63om.authzed.api.v1Z2github.com/authzed/authzed-go/proto/authzed/api/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authzed.api.v1.debug_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\022com.authzed.api.v1Z2github.com/authzed/authzed-go/proto/authzed/api/v1'
  _globals['_CHECKDEBUGTRACE'].oneofs_by_name['resolution']._loaded_options = None
  _globals['_CHECKDEBUGTRACE'].oneofs_by_name['resolution']._serialized_options = b'\370B\001'
  _globals['_CHECKDEBUGTRACE'].fields_by_name['resource']._loaded_options = None
  _globals['_CHECKDEBUGTRACE'].fields_by_name['resource']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_CHECKDEBUGTRACE'].fields_by_name['permission_type']._loaded_options = None
  _globals['_CHECKDEBUGTRACE'].fields_by_name['permission_type']._serialized_options = b'\372B\007\202\001\004\020\001 \000'
  _globals['_CHECKDEBUGTRACE'].fields_by_name['subject']._loaded_options = None
  _globals['_CHECKDEBUGTRACE'].fields_by_name['subject']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_CHECKDEBUGTRACE'].fields_by_name['result']._loaded_options = None
  _globals['_CHECKDEBUGTRACE'].fields_by_name['result']._serialized_options = b'\372B\007\202\001\004\020\001 \000'
  _globals['_DEBUGINFORMATION']._serialized_start=160
  _globals['_DEBUGINFORMATION']._serialized_end=266
  _globals['_CHECKDEBUGTRACE']._serialized_start=269
  _globals['_CHECKDEBUGTRACE']._serialized_end=1280
  _globals['_CHECKDEBUGTRACE_SUBPROBLEMS']._serialized_start=915
  _globals['_CHECKDEBUGTRACE_SUBPROBLEMS']._serialized_end=985
  _globals['_CHECKDEBUGTRACE_PERMISSIONTYPE']._serialized_start=987
  _globals['_CHECKDEBUGTRACE_PERMISSIONTYPE']._serialized_end=1098
  _globals['_CHECKDEBUGTRACE_PERMISSIONSHIP']._serialized_start=1101
  _globals['_CHECKDEBUGTRACE_PERMISSIONSHIP']._serialized_end=1261
  _globals['_CAVEATEVALINFO']._serialized_start=1283
  _globals['_CAVEATEVALINFO']._serialized_end=1687
  _globals['_CAVEATEVALINFO_RESULT']._serialized_start=1563
  _globals['_CAVEATEVALINFO_RESULT']._serialized_end=1687
# @@protoc_insertion_point(module_scope)
