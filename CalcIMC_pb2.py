# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: CalcIMC.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'CalcIMC.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rCalcIMC.proto\"?\n\x11\x43\x61lculoIMCRequest\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\x0c\n\x04peso\x18\x02 \x01(\x01\x12\x0e\n\x06\x61ltura\x18\x03 \x01(\x01\"0\n\x12\x43\x61lculoIMCResponse\x12\r\n\x05\x61viso\x18\x01 \x01(\t\x12\x0b\n\x03imc\x18\x02 \x01(\x01\x32\x43\n\nIMCService\x12\x35\n\nCalculoIMC\x12\x12.CalculoIMCRequest\x1a\x13.CalculoIMCResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CalcIMC_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CALCULOIMCREQUEST']._serialized_start=17
  _globals['_CALCULOIMCREQUEST']._serialized_end=80
  _globals['_CALCULOIMCRESPONSE']._serialized_start=82
  _globals['_CALCULOIMCRESPONSE']._serialized_end=130
  _globals['_IMCSERVICE']._serialized_start=132
  _globals['_IMCSERVICE']._serialized_end=199
# @@protoc_insertion_point(module_scope)
