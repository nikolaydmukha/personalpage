# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protos.pilling.rpc.protos.client_pb2 as client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='services.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0eservices.proto\x1a\x0c\x63lient.proto\"r\n\x15\x43lientServicesRequest\x12\n\n\x02id\x18\x01 \x02(\t\x12\x14\n\x0cwith_balance\x18\x02 \x02(\x08\x12\x37\n\x0e\x62\x61lance_method\x18\x03 \x01(\x0e\x32\x0e.BalanceMethod:\x0f\x42M_PROPORTIONAL\"V\n\x13\x43lientServicesReply\x12\x1c\n\x06\x63lient\x18\x01 \x02(\x0b\x32\x0c.ClientReply\x12!\n\tcontracts\x18\x02 \x03(\x0b\x32\x0e.ContractReply\"\xda\x02\n\rContractReply\x12\n\n\x02id\x18\x01 \x02(\t\x12\r\n\x05login\x18\x02 \x02(\t\x12\x0e\n\x06\x61\x63tive\x18\x03 \x02(\x08\x12\x12\n\ncommercial\x18\x04 \x02(\t\x12\x0b\n\x03own\x18\x05 \x02(\x08\x12\x0f\n\x07\x61\x64vance\x18\x06 \x02(\x08\x12(\n\x0corganization\x18\x07 \x02(\x0b\x32\x12.OrganizationReply\x12$\n\x08provider\x18\x08 \x02(\x0b\x32\x12.OrganizationReply\x12\'\n\x0cpayment_type\x18\t \x02(\x0b\x32\x11.PaymentTypeReply\x12(\n\rservice_packs\x18\n \x03(\x0b\x32\x11.ServicePackReply\x12\x0f\n\x07ts_from\x18\x0b \x02(\x05\x12\r\n\x05ts_to\x18\x0c \x01(\x05\x12\x0f\n\x07\x62\x61lance\x18\r \x01(\x03\x12\x18\n\x10required_payment\x18\x0e \x01(\x03\"<\n\x11OrganizationReply\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\r\n\x05\x64\x65scr\x18\x03 \x02(\t\";\n\x10PaymentTypeReply\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\r\n\x05\x64\x65scr\x18\x03 \x02(\t\"\xc6\x02\n\x10ServicePackReply\x12\n\n\x02id\x18\x01 \x02(\t\x12\r\n\x05login\x18\x02 \x02(\t\x12\x0e\n\x06\x61\x63tive\x18\x03 \x02(\x08\x12\x12\n\ncommercial\x18\x04 \x02(\t\x12\x12\n\ntotal_cost\x18\x05 \x02(\x03\x12\x18\n\x10\x63onditional_cost\x18\x06 \x02(\x03\x12\x1a\n\x12unconditional_cost\x18\x07 \x02(\x03\x12\x30\n\x13\x61\x63\x63ounting_interval\x18\x08 \x02(\x0e\x32\x13.AccountingInterval\x12,\n\x0f\x63harge_interval\x18\t \x02(\x0e\x32\x13.AccountingInterval\x12\x0f\n\x07ts_from\x18\n \x02(\x05\x12\r\n\x05ts_to\x18\x0b \x01(\x05\x12\x0f\n\x07\x62\x61lance\x18\x0c \x01(\x03\x12\x18\n\x10required_payment\x18\r \x01(\x03*L\n\rBalanceMethod\x12\x13\n\x0f\x42M_PERIOD_START\x10\x00\x12\x11\n\rBM_PERIOD_END\x10\x01\x12\x13\n\x0f\x42M_PROPORTIONAL\x10\x02*\x82\x01\n\x12\x41\x63\x63ountingInterval\x12\x0b\n\x07\x41I_HOUR\x10\x00\x12\n\n\x06\x41I_DAY\x10\x01\x12\x0b\n\x07\x41I_WEEK\x10\x02\x12\x0c\n\x08\x41I_MONTH\x10\x03\x12\r\n\tAI_MONTH2\x10\x04\x12\r\n\tAI_MONTH3\x10\x05\x12\r\n\tAI_MONTH6\x10\x06\x12\x0b\n\x07\x41I_YEAR\x10\x07\x32O\n\x08Services\x12\x43\n\x11GetClientServices\x12\x16.ClientServicesRequest\x1a\x14.ClientServicesReply\"\x00')
  ,
  dependencies=[client__pb2.DESCRIPTOR,])

_BALANCEMETHOD = _descriptor.EnumDescriptor(
  name='BalanceMethod',
  full_name='BalanceMethod',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BM_PERIOD_START', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BM_PERIOD_END', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BM_PROPORTIONAL', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1037,
  serialized_end=1113,
)
_sym_db.RegisterEnumDescriptor(_BALANCEMETHOD)

BalanceMethod = enum_type_wrapper.EnumTypeWrapper(_BALANCEMETHOD)
_ACCOUNTINGINTERVAL = _descriptor.EnumDescriptor(
  name='AccountingInterval',
  full_name='AccountingInterval',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AI_HOUR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AI_DAY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AI_WEEK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AI_MONTH', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AI_MONTH2', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AI_MONTH3', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AI_MONTH6', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AI_YEAR', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1116,
  serialized_end=1246,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNTINGINTERVAL)

AccountingInterval = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTINGINTERVAL)
BM_PERIOD_START = 0
BM_PERIOD_END = 1
BM_PROPORTIONAL = 2
AI_HOUR = 0
AI_DAY = 1
AI_WEEK = 2
AI_MONTH = 3
AI_MONTH2 = 4
AI_MONTH3 = 5
AI_MONTH6 = 6
AI_YEAR = 7



_CLIENTSERVICESREQUEST = _descriptor.Descriptor(
  name='ClientServicesRequest',
  full_name='ClientServicesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ClientServicesRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_balance', full_name='ClientServicesRequest.with_balance', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance_method', full_name='ClientServicesRequest.balance_method', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=146,
)


_CLIENTSERVICESREPLY = _descriptor.Descriptor(
  name='ClientServicesReply',
  full_name='ClientServicesReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client', full_name='ClientServicesReply.client', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contracts', full_name='ClientServicesReply.contracts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=234,
)


_CONTRACTREPLY = _descriptor.Descriptor(
  name='ContractReply',
  full_name='ContractReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ContractReply.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='login', full_name='ContractReply.login', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active', full_name='ContractReply.active', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commercial', full_name='ContractReply.commercial', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='own', full_name='ContractReply.own', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='advance', full_name='ContractReply.advance', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organization', full_name='ContractReply.organization', index=6,
      number=7, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider', full_name='ContractReply.provider', index=7,
      number=8, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_type', full_name='ContractReply.payment_type', index=8,
      number=9, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_packs', full_name='ContractReply.service_packs', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts_from', full_name='ContractReply.ts_from', index=10,
      number=11, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts_to', full_name='ContractReply.ts_to', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance', full_name='ContractReply.balance', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required_payment', full_name='ContractReply.required_payment', index=13,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=583,
)


_ORGANIZATIONREPLY = _descriptor.Descriptor(
  name='OrganizationReply',
  full_name='OrganizationReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='OrganizationReply.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='OrganizationReply.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descr', full_name='OrganizationReply.descr', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=645,
)


_PAYMENTTYPEREPLY = _descriptor.Descriptor(
  name='PaymentTypeReply',
  full_name='PaymentTypeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PaymentTypeReply.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='PaymentTypeReply.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descr', full_name='PaymentTypeReply.descr', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=647,
  serialized_end=706,
)


_SERVICEPACKREPLY = _descriptor.Descriptor(
  name='ServicePackReply',
  full_name='ServicePackReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ServicePackReply.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='login', full_name='ServicePackReply.login', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active', full_name='ServicePackReply.active', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commercial', full_name='ServicePackReply.commercial', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_cost', full_name='ServicePackReply.total_cost', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conditional_cost', full_name='ServicePackReply.conditional_cost', index=5,
      number=6, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unconditional_cost', full_name='ServicePackReply.unconditional_cost', index=6,
      number=7, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accounting_interval', full_name='ServicePackReply.accounting_interval', index=7,
      number=8, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charge_interval', full_name='ServicePackReply.charge_interval', index=8,
      number=9, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts_from', full_name='ServicePackReply.ts_from', index=9,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts_to', full_name='ServicePackReply.ts_to', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance', full_name='ServicePackReply.balance', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required_payment', full_name='ServicePackReply.required_payment', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=709,
  serialized_end=1035,
)

_CLIENTSERVICESREQUEST.fields_by_name['balance_method'].enum_type = _BALANCEMETHOD
_CLIENTSERVICESREPLY.fields_by_name['client'].message_type = client__pb2._CLIENTREPLY
_CLIENTSERVICESREPLY.fields_by_name['contracts'].message_type = _CONTRACTREPLY
_CONTRACTREPLY.fields_by_name['organization'].message_type = _ORGANIZATIONREPLY
_CONTRACTREPLY.fields_by_name['provider'].message_type = _ORGANIZATIONREPLY
_CONTRACTREPLY.fields_by_name['payment_type'].message_type = _PAYMENTTYPEREPLY
_CONTRACTREPLY.fields_by_name['service_packs'].message_type = _SERVICEPACKREPLY
_SERVICEPACKREPLY.fields_by_name['accounting_interval'].enum_type = _ACCOUNTINGINTERVAL
_SERVICEPACKREPLY.fields_by_name['charge_interval'].enum_type = _ACCOUNTINGINTERVAL
DESCRIPTOR.message_types_by_name['ClientServicesRequest'] = _CLIENTSERVICESREQUEST
DESCRIPTOR.message_types_by_name['ClientServicesReply'] = _CLIENTSERVICESREPLY
DESCRIPTOR.message_types_by_name['ContractReply'] = _CONTRACTREPLY
DESCRIPTOR.message_types_by_name['OrganizationReply'] = _ORGANIZATIONREPLY
DESCRIPTOR.message_types_by_name['PaymentTypeReply'] = _PAYMENTTYPEREPLY
DESCRIPTOR.message_types_by_name['ServicePackReply'] = _SERVICEPACKREPLY
DESCRIPTOR.enum_types_by_name['BalanceMethod'] = _BALANCEMETHOD
DESCRIPTOR.enum_types_by_name['AccountingInterval'] = _ACCOUNTINGINTERVAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientServicesRequest = _reflection.GeneratedProtocolMessageType('ClientServicesRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTSERVICESREQUEST,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:ClientServicesRequest)
  ))
_sym_db.RegisterMessage(ClientServicesRequest)

ClientServicesReply = _reflection.GeneratedProtocolMessageType('ClientServicesReply', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTSERVICESREPLY,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:ClientServicesReply)
  ))
_sym_db.RegisterMessage(ClientServicesReply)

ContractReply = _reflection.GeneratedProtocolMessageType('ContractReply', (_message.Message,), dict(
  DESCRIPTOR = _CONTRACTREPLY,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:ContractReply)
  ))
_sym_db.RegisterMessage(ContractReply)

OrganizationReply = _reflection.GeneratedProtocolMessageType('OrganizationReply', (_message.Message,), dict(
  DESCRIPTOR = _ORGANIZATIONREPLY,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:OrganizationReply)
  ))
_sym_db.RegisterMessage(OrganizationReply)

PaymentTypeReply = _reflection.GeneratedProtocolMessageType('PaymentTypeReply', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENTTYPEREPLY,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:PaymentTypeReply)
  ))
_sym_db.RegisterMessage(PaymentTypeReply)

ServicePackReply = _reflection.GeneratedProtocolMessageType('ServicePackReply', (_message.Message,), dict(
  DESCRIPTOR = _SERVICEPACKREPLY,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:ServicePackReply)
  ))
_sym_db.RegisterMessage(ServicePackReply)



_SERVICES = _descriptor.ServiceDescriptor(
  name='Services',
  full_name='Services',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1248,
  serialized_end=1327,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetClientServices',
    full_name='Services.GetClientServices',
    index=0,
    containing_service=None,
    input_type=_CLIENTSERVICESREQUEST,
    output_type=_CLIENTSERVICESREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICES)

DESCRIPTOR.services_by_name['Services'] = _SERVICES

# @@protoc_insertion_point(module_scope)
