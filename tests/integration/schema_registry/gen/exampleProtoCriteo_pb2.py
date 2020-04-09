# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exampleProtoCriteo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import metadata_proto_pb2 as metadata__proto__pb2
from . import common_proto_pb2 as common__proto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='exampleProtoCriteo.proto',
  package='Criteo.Glup',
  syntax='proto3',
  serialized_pb=_b('\n\x18\x65xampleProtoCriteo.proto\x12\x0b\x43riteo.Glup\x1a\x14metadata_proto.proto\x1a\x12\x63ommon_proto.proto\"\x9b\x06\n\x08\x43lickCas\x12(\n\x0bglup_origin\x18\x01 \x01(\x0b\x32\x13.Criteo.Glup.Origin\x12)\n\tpartition\x18\x02 \x01(\x0b\x32\x16.Criteo.Glup.Partition\x12\x0b\n\x03uid\x18\x05 \x01(\t\x12:\n\nset_fields\x18\xda\x86\x03 \x03(\x0b\x32$.Criteo.Glup.ClickCas.SetFieldsEntry\x12R\n\x0f\x63ontrol_message\x18\xff\xff\x7f \x03(\x0b\x32%.Criteo.Glup.ControlMessage.WatermarkB\x10\x92\xb5\x18\x0c\n\n__metadata\x1a\x30\n\x0eSetFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01:\xc9\x03\x88\xb5\x18\x01\x82\xb5\x18\x04:\x02\x10\x01\x82\xb5\x18\x12\n\x10\n\x0eglup_click_cas\x82\xb5\x18\xea\x01*\xe7\x01\n\tclick_cas\x12G\n,/glup/datasets/click_cas/data/full/JSON_PAIL\x10\x02@dJ\x13\x46\x45\x44\x45RATED_JSON_PAIL\x12U\n3/glup/datasets/click_cas/data/full/PROTOBUF_PARQUET\x10\x04@2J\x1a\x46\x45\x44\x45RATED_PROTOBUF_PARQUET\x18\x04\"&com.criteo.glup.ClickCasProto$ClickCas2\x0b\x65nginejoins@\x01H\x86\x03\x82\xb5\x18\xb3\x01\x12\xb0\x01\x1a\xad\x01\n\x0b\x65nginejoins\x12\tclick_cas \x04Z9\x12\x30\n\x0eglup_click_cas\"\tclick_cas*\x13\x46\x45\x44\x45RATED_JSON_PAIL\xd2\x0f\x04\x08\x02\x10\x06ZP2G\n\tclick_cas\x12\tclick_cas*\x13\x46\x45\x44\x45RATED_JSON_PAIL2\x1a\x46\x45\x44\x45RATED_PROTOBUF_PARQUET\xd2\x0f\x04\x08\x02\x10\x06\x62\x04R\x02\x18\x04J\x04\x08\x46\x10JJ\x04\x08K\x10LR\x08obsoleteR\tobsolete2B\x11\n\x0f\x63om.criteo.glupb\x06proto3')
  ,
  dependencies=[metadata__proto__pb2.DESCRIPTOR,common__proto__pb2.DESCRIPTOR,])




_CLICKCAS_SETFIELDSENTRY = _descriptor.Descriptor(
  name='SetFieldsEntry',
  full_name='Criteo.Glup.ClickCas.SetFieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Criteo.Glup.ClickCas.SetFieldsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Criteo.Glup.ClickCas.SetFieldsEntry.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=386,
)

_CLICKCAS = _descriptor.Descriptor(
  name='ClickCas',
  full_name='Criteo.Glup.ClickCas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='glup_origin', full_name='Criteo.Glup.ClickCas.glup_origin', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partition', full_name='Criteo.Glup.ClickCas.partition', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='Criteo.Glup.ClickCas.uid', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_fields', full_name='Criteo.Glup.ClickCas.set_fields', index=3,
      number=50010, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='control_message', full_name='Criteo.Glup.ClickCas.control_message', index=4,
      number=2097151, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222\265\030\014\n\n__metadata')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLICKCAS_SETFIELDSENTRY, ],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\265\030\001\202\265\030\004:\002\020\001\202\265\030\022\n\020\n\016glup_click_cas\202\265\030\352\001*\347\001\n\tclick_cas\022G\n,/glup/datasets/click_cas/data/full/JSON_PAIL\020\002@dJ\023FEDERATED_JSON_PAIL\022U\n3/glup/datasets/click_cas/data/full/PROTOBUF_PARQUET\020\004@2J\032FEDERATED_PROTOBUF_PARQUET\030\004\"&com.criteo.glup.ClickCasProto$ClickCas2\013enginejoins@\001H\206\003\202\265\030\263\001\022\260\001\032\255\001\n\013enginejoins\022\tclick_cas \004Z9\0220\n\016glup_click_cas\"\tclick_cas*\023FEDERATED_JSON_PAIL\322\017\004\010\002\020\006ZP2G\n\tclick_cas\022\tclick_cas*\023FEDERATED_JSON_PAIL2\032FEDERATED_PROTOBUF_PARQUET\322\017\004\010\002\020\006b\004R\002\030\004')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=879,
)

_CLICKCAS_SETFIELDSENTRY.containing_type = _CLICKCAS
_CLICKCAS.fields_by_name['glup_origin'].message_type = metadata__proto__pb2._ORIGIN
_CLICKCAS.fields_by_name['partition'].message_type = metadata__proto__pb2._PARTITION
_CLICKCAS.fields_by_name['set_fields'].message_type = _CLICKCAS_SETFIELDSENTRY
_CLICKCAS.fields_by_name['control_message'].message_type = metadata__proto__pb2._CONTROLMESSAGE_WATERMARK
DESCRIPTOR.message_types_by_name['ClickCas'] = _CLICKCAS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClickCas = _reflection.GeneratedProtocolMessageType('ClickCas', (_message.Message,), dict(

  SetFieldsEntry = _reflection.GeneratedProtocolMessageType('SetFieldsEntry', (_message.Message,), dict(
    DESCRIPTOR = _CLICKCAS_SETFIELDSENTRY,
    __module__ = 'exampleProtoCriteo_pb2'
    # @@protoc_insertion_point(class_scope:Criteo.Glup.ClickCas.SetFieldsEntry)
    ))
  ,
  DESCRIPTOR = _CLICKCAS,
  __module__ = 'exampleProtoCriteo_pb2'
  # @@protoc_insertion_point(class_scope:Criteo.Glup.ClickCas)
  ))
_sym_db.RegisterMessage(ClickCas)
_sym_db.RegisterMessage(ClickCas.SetFieldsEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\017com.criteo.glup'))
_CLICKCAS_SETFIELDSENTRY.has_options = True
_CLICKCAS_SETFIELDSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_CLICKCAS.fields_by_name['control_message'].has_options = True
_CLICKCAS.fields_by_name['control_message']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222\265\030\014\n\n__metadata'))
_CLICKCAS.has_options = True
_CLICKCAS._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\265\030\001\202\265\030\004:\002\020\001\202\265\030\022\n\020\n\016glup_click_cas\202\265\030\352\001*\347\001\n\tclick_cas\022G\n,/glup/datasets/click_cas/data/full/JSON_PAIL\020\002@dJ\023FEDERATED_JSON_PAIL\022U\n3/glup/datasets/click_cas/data/full/PROTOBUF_PARQUET\020\004@2J\032FEDERATED_PROTOBUF_PARQUET\030\004\"&com.criteo.glup.ClickCasProto$ClickCas2\013enginejoins@\001H\206\003\202\265\030\263\001\022\260\001\032\255\001\n\013enginejoins\022\tclick_cas \004Z9\0220\n\016glup_click_cas\"\tclick_cas*\023FEDERATED_JSON_PAIL\322\017\004\010\002\020\006ZP2G\n\tclick_cas\022\tclick_cas*\023FEDERATED_JSON_PAIL2\032FEDERATED_PROTOBUF_PARQUET\322\017\004\010\002\020\006b\004R\002\030\004'))
# @@protoc_insertion_point(module_scope)