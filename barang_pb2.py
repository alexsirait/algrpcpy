# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: barang.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'barang.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x62\x61rang.proto\x12\x06\x62\x61rang\"3\n\x06\x42\x61rang\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06\x62\x61rang\x18\x02 \x01(\t\x12\r\n\x05harga\x18\x03 \x01(\x02\"\x1b\n\rBarangRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"A\n\x0e\x42\x61rangResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x1e\n\x06\x62\x61rang\x18\x02 \x01(\x0b\x32\x0e.barang.Barang2\xfa\x01\n\rBarangService\x12\x36\n\x0c\x43reateBarang\x12\x0e.barang.Barang\x1a\x16.barang.BarangResponse\x12:\n\tGetBarang\x12\x15.barang.BarangRequest\x1a\x16.barang.BarangResponse\x12\x36\n\x0cUpdateBarang\x12\x0e.barang.Barang\x1a\x16.barang.BarangResponse\x12=\n\x0c\x44\x65leteBarang\x12\x15.barang.BarangRequest\x1a\x16.barang.BarangResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'barang_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BARANG']._serialized_start=24
  _globals['_BARANG']._serialized_end=75
  _globals['_BARANGREQUEST']._serialized_start=77
  _globals['_BARANGREQUEST']._serialized_end=104
  _globals['_BARANGRESPONSE']._serialized_start=106
  _globals['_BARANGRESPONSE']._serialized_end=171
  _globals['_BARANGSERVICE']._serialized_start=174
  _globals['_BARANGSERVICE']._serialized_end=424
# @@protoc_insertion_point(module_scope)
