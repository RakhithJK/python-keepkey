# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='trezor.proto',
  package='',
  serialized_pb='\n\x0ctrezor.proto\"\x0c\n\nInitialize\"[\n\x08\x46\x65\x61tures\x12\x0e\n\x06vendor\x18\x01 \x01(\x0c\x12\x15\n\rmajor_version\x18\x02 \x01(\r\x12\x15\n\rminor_version\x18\x03 \x01(\r\x12\x11\n\tmaxfee_kb\x18\x04 \x01(\x04\"\x17\n\x04Ping\x12\x0f\n\x07message\x18\x01 \x01(\x0c\"#\n\x11\x44\x65\x62ugLinkDecision\x12\x0e\n\x06yes_no\x18\x01 \x02(\x08\"N\n\x11\x44\x65\x62ugLinkGetState\x12\x0e\n\x06layout\x18\x01 \x01(\x08\x12\x0b\n\x03pin\x18\x02 \x01(\x08\x12\x0e\n\x06matrix\x18\x03 \x01(\x08\x12\x0c\n\x04seed\x18\x04 \x01(\x08\"K\n\x0e\x44\x65\x62ugLinkState\x12\x0e\n\x06layout\x18\x01 \x01(\x0c\x12\x0b\n\x03pin\x18\x02 \x01(\x0c\x12\x0e\n\x06matrix\x18\x03 \x01(\x0c\x12\x0c\n\x04seed\x18\x04 \x01(\x0c\"\x0f\n\rDebugLinkStop\"\x1a\n\x07Success\x12\x0f\n\x07message\x18\x01 \x01(\x0c\"(\n\x07\x46\x61ilure\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\x0c\"\t\n\x07GetUUID\"\x14\n\x04UUID\x12\x0c\n\x04UUID\x18\x01 \x02(\x0c\"\x0f\n\rButtonRequest\"\x0b\n\tButtonAck\"\x0e\n\x0c\x42uttonCancel\"#\n\x10PinMatrixRequest\x12\x0f\n\x07message\x18\x01 \x01(\x0c\"\x1b\n\x0cPinMatrixAck\x12\x0b\n\x03pin\x18\x01 \x02(\x0c\"\x11\n\x0fPinMatrixCancel\"\x1a\n\nGetEntropy\x12\x0c\n\x04size\x18\x01 \x02(\r\"\x1a\n\x07\x45ntropy\x12\x0f\n\x07\x65ntropy\x18\x01 \x02(\x0c\" \n\x0bSetMaxFeeKb\x12\x11\n\tmaxfee_kb\x18\x01 \x02(\x04\"\x14\n\x12GetMasterPublicKey\"\x1e\n\x0fMasterPublicKey\x12\x0b\n\x03key\x18\x01 \x02(\x0c\"\x1f\n\nGetAddress\x12\x11\n\taddress_n\x18\x01 \x03(\r\"\x1a\n\x07\x41\x64\x64ress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\x0c\"\'\n\nLoadDevice\x12\x0c\n\x04seed\x18\x01 \x02(\x0c\x12\x0b\n\x03pin\x18\x02 \x01(\x0c\"\x1d\n\x0bResetDevice\x12\x0e\n\x06random\x18\x07 \x01(\x0c\"5\n\x06SignTx\x12\x15\n\routputs_count\x18\x03 \x02(\r\x12\x14\n\x0cinputs_count\x18\x05 \x02(\r\"\x86\x01\n\tTxRequest\x12\x15\n\rrequest_index\x18\x01 \x01(\x05\x12\"\n\x0crequest_type\x18\x02 \x01(\x0e\x32\x0c.RequestType\x12\x14\n\x0csigned_index\x18\x03 \x01(\x05\x12\x11\n\tsignature\x18\x04 \x01(\x0c\x12\x15\n\rserialized_tx\x18\x05 \x01(\x0c\"v\n\x07TxInput\x12\r\n\x05index\x18\x01 \x02(\r\x12\x11\n\taddress_n\x18\x02 \x03(\r\x12\x0e\n\x06\x61mount\x18\x03 \x02(\x04\x12\x11\n\tprev_hash\x18\x04 \x02(\x0c\x12\x12\n\nprev_index\x18\x05 \x02(\r\x12\x12\n\nscript_sig\x18\x06 \x01(\x0c\"\x84\x01\n\x08TxOutput\x12\r\n\x05index\x18\x01 \x02(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x02(\x0c\x12\x11\n\taddress_n\x18\x03 \x03(\r\x12\x0e\n\x06\x61mount\x18\x04 \x02(\x04\x12 \n\x0bscript_type\x18\x05 \x02(\x0e\x32\x0b.ScriptType\x12\x13\n\x0bscript_args\x18\x06 \x03(\x0c*3\n\nScriptType\x12\x10\n\x0cPAYTOADDRESS\x10\x00\x12\x13\n\x0fPAYTOSCRIPTHASH\x10\x01*(\n\x0bRequestType\x12\x0b\n\x07TXINPUT\x10\x00\x12\x0c\n\x08TXOUTPUT\x10\x01')

_SCRIPTTYPE = descriptor.EnumDescriptor(
  name='ScriptType',
  full_name='ScriptType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='PAYTOADDRESS', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PAYTOSCRIPTHASH', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1317,
  serialized_end=1368,
)


_REQUESTTYPE = descriptor.EnumDescriptor(
  name='RequestType',
  full_name='RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='TXINPUT', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TXOUTPUT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1370,
  serialized_end=1410,
)


PAYTOADDRESS = 0
PAYTOSCRIPTHASH = 1
TXINPUT = 0
TXOUTPUT = 1



_INITIALIZE = descriptor.Descriptor(
  name='Initialize',
  full_name='Initialize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=16,
  serialized_end=28,
)


_FEATURES = descriptor.Descriptor(
  name='Features',
  full_name='Features',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='vendor', full_name='Features.vendor', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='major_version', full_name='Features.major_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='minor_version', full_name='Features.minor_version', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxfee_kb', full_name='Features.maxfee_kb', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=30,
  serialized_end=121,
)


_PING = descriptor.Descriptor(
  name='Ping',
  full_name='Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='Ping.message', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=123,
  serialized_end=146,
)


_DEBUGLINKDECISION = descriptor.Descriptor(
  name='DebugLinkDecision',
  full_name='DebugLinkDecision',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='yes_no', full_name='DebugLinkDecision.yes_no', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=148,
  serialized_end=183,
)


_DEBUGLINKGETSTATE = descriptor.Descriptor(
  name='DebugLinkGetState',
  full_name='DebugLinkGetState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='layout', full_name='DebugLinkGetState.layout', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pin', full_name='DebugLinkGetState.pin', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='matrix', full_name='DebugLinkGetState.matrix', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='seed', full_name='DebugLinkGetState.seed', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=185,
  serialized_end=263,
)


_DEBUGLINKSTATE = descriptor.Descriptor(
  name='DebugLinkState',
  full_name='DebugLinkState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='layout', full_name='DebugLinkState.layout', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pin', full_name='DebugLinkState.pin', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='matrix', full_name='DebugLinkState.matrix', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='seed', full_name='DebugLinkState.seed', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=265,
  serialized_end=340,
)


_DEBUGLINKSTOP = descriptor.Descriptor(
  name='DebugLinkStop',
  full_name='DebugLinkStop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=342,
  serialized_end=357,
)


_SUCCESS = descriptor.Descriptor(
  name='Success',
  full_name='Success',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='Success.message', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=359,
  serialized_end=385,
)


_FAILURE = descriptor.Descriptor(
  name='Failure',
  full_name='Failure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='Failure.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='Failure.message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=387,
  serialized_end=427,
)


_GETUUID = descriptor.Descriptor(
  name='GetUUID',
  full_name='GetUUID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=429,
  serialized_end=438,
)


_UUID = descriptor.Descriptor(
  name='UUID',
  full_name='UUID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='UUID', full_name='UUID.UUID', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=440,
  serialized_end=460,
)


_BUTTONREQUEST = descriptor.Descriptor(
  name='ButtonRequest',
  full_name='ButtonRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=462,
  serialized_end=477,
)


_BUTTONACK = descriptor.Descriptor(
  name='ButtonAck',
  full_name='ButtonAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=479,
  serialized_end=490,
)


_BUTTONCANCEL = descriptor.Descriptor(
  name='ButtonCancel',
  full_name='ButtonCancel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=492,
  serialized_end=506,
)


_PINMATRIXREQUEST = descriptor.Descriptor(
  name='PinMatrixRequest',
  full_name='PinMatrixRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='PinMatrixRequest.message', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=508,
  serialized_end=543,
)


_PINMATRIXACK = descriptor.Descriptor(
  name='PinMatrixAck',
  full_name='PinMatrixAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='pin', full_name='PinMatrixAck.pin', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=545,
  serialized_end=572,
)


_PINMATRIXCANCEL = descriptor.Descriptor(
  name='PinMatrixCancel',
  full_name='PinMatrixCancel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=574,
  serialized_end=591,
)


_GETENTROPY = descriptor.Descriptor(
  name='GetEntropy',
  full_name='GetEntropy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='size', full_name='GetEntropy.size', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=593,
  serialized_end=619,
)


_ENTROPY = descriptor.Descriptor(
  name='Entropy',
  full_name='Entropy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='entropy', full_name='Entropy.entropy', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=621,
  serialized_end=647,
)


_SETMAXFEEKB = descriptor.Descriptor(
  name='SetMaxFeeKb',
  full_name='SetMaxFeeKb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='maxfee_kb', full_name='SetMaxFeeKb.maxfee_kb', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=649,
  serialized_end=681,
)


_GETMASTERPUBLICKEY = descriptor.Descriptor(
  name='GetMasterPublicKey',
  full_name='GetMasterPublicKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=683,
  serialized_end=703,
)


_MASTERPUBLICKEY = descriptor.Descriptor(
  name='MasterPublicKey',
  full_name='MasterPublicKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='MasterPublicKey.key', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=705,
  serialized_end=735,
)


_GETADDRESS = descriptor.Descriptor(
  name='GetAddress',
  full_name='GetAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='address_n', full_name='GetAddress.address_n', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=737,
  serialized_end=768,
)


_ADDRESS = descriptor.Descriptor(
  name='Address',
  full_name='Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='address', full_name='Address.address', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=770,
  serialized_end=796,
)


_LOADDEVICE = descriptor.Descriptor(
  name='LoadDevice',
  full_name='LoadDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='seed', full_name='LoadDevice.seed', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pin', full_name='LoadDevice.pin', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=798,
  serialized_end=837,
)


_RESETDEVICE = descriptor.Descriptor(
  name='ResetDevice',
  full_name='ResetDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='random', full_name='ResetDevice.random', index=0,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=839,
  serialized_end=868,
)


_SIGNTX = descriptor.Descriptor(
  name='SignTx',
  full_name='SignTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='outputs_count', full_name='SignTx.outputs_count', index=0,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='inputs_count', full_name='SignTx.inputs_count', index=1,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=870,
  serialized_end=923,
)


_TXREQUEST = descriptor.Descriptor(
  name='TxRequest',
  full_name='TxRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='request_index', full_name='TxRequest.request_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='request_type', full_name='TxRequest.request_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='signed_index', full_name='TxRequest.signed_index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='signature', full_name='TxRequest.signature', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='serialized_tx', full_name='TxRequest.serialized_tx', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=926,
  serialized_end=1060,
)


_TXINPUT = descriptor.Descriptor(
  name='TxInput',
  full_name='TxInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='index', full_name='TxInput.index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='address_n', full_name='TxInput.address_n', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='amount', full_name='TxInput.amount', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='prev_hash', full_name='TxInput.prev_hash', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='prev_index', full_name='TxInput.prev_index', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='script_sig', full_name='TxInput.script_sig', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1062,
  serialized_end=1180,
)


_TXOUTPUT = descriptor.Descriptor(
  name='TxOutput',
  full_name='TxOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='index', full_name='TxOutput.index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='address', full_name='TxOutput.address', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='address_n', full_name='TxOutput.address_n', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='amount', full_name='TxOutput.amount', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='script_type', full_name='TxOutput.script_type', index=4,
      number=5, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='script_args', full_name='TxOutput.script_args', index=5,
      number=6, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1183,
  serialized_end=1315,
)

_TXREQUEST.fields_by_name['request_type'].enum_type = _REQUESTTYPE
_TXOUTPUT.fields_by_name['script_type'].enum_type = _SCRIPTTYPE
DESCRIPTOR.message_types_by_name['Initialize'] = _INITIALIZE
DESCRIPTOR.message_types_by_name['Features'] = _FEATURES
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['DebugLinkDecision'] = _DEBUGLINKDECISION
DESCRIPTOR.message_types_by_name['DebugLinkGetState'] = _DEBUGLINKGETSTATE
DESCRIPTOR.message_types_by_name['DebugLinkState'] = _DEBUGLINKSTATE
DESCRIPTOR.message_types_by_name['DebugLinkStop'] = _DEBUGLINKSTOP
DESCRIPTOR.message_types_by_name['Success'] = _SUCCESS
DESCRIPTOR.message_types_by_name['Failure'] = _FAILURE
DESCRIPTOR.message_types_by_name['GetUUID'] = _GETUUID
DESCRIPTOR.message_types_by_name['UUID'] = _UUID
DESCRIPTOR.message_types_by_name['ButtonRequest'] = _BUTTONREQUEST
DESCRIPTOR.message_types_by_name['ButtonAck'] = _BUTTONACK
DESCRIPTOR.message_types_by_name['ButtonCancel'] = _BUTTONCANCEL
DESCRIPTOR.message_types_by_name['PinMatrixRequest'] = _PINMATRIXREQUEST
DESCRIPTOR.message_types_by_name['PinMatrixAck'] = _PINMATRIXACK
DESCRIPTOR.message_types_by_name['PinMatrixCancel'] = _PINMATRIXCANCEL
DESCRIPTOR.message_types_by_name['GetEntropy'] = _GETENTROPY
DESCRIPTOR.message_types_by_name['Entropy'] = _ENTROPY
DESCRIPTOR.message_types_by_name['SetMaxFeeKb'] = _SETMAXFEEKB
DESCRIPTOR.message_types_by_name['GetMasterPublicKey'] = _GETMASTERPUBLICKEY
DESCRIPTOR.message_types_by_name['MasterPublicKey'] = _MASTERPUBLICKEY
DESCRIPTOR.message_types_by_name['GetAddress'] = _GETADDRESS
DESCRIPTOR.message_types_by_name['Address'] = _ADDRESS
DESCRIPTOR.message_types_by_name['LoadDevice'] = _LOADDEVICE
DESCRIPTOR.message_types_by_name['ResetDevice'] = _RESETDEVICE
DESCRIPTOR.message_types_by_name['SignTx'] = _SIGNTX
DESCRIPTOR.message_types_by_name['TxRequest'] = _TXREQUEST
DESCRIPTOR.message_types_by_name['TxInput'] = _TXINPUT
DESCRIPTOR.message_types_by_name['TxOutput'] = _TXOUTPUT

class Initialize(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INITIALIZE
  
  # @@protoc_insertion_point(class_scope:Initialize)

class Features(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FEATURES
  
  # @@protoc_insertion_point(class_scope:Features)

class Ping(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PING
  
  # @@protoc_insertion_point(class_scope:Ping)

class DebugLinkDecision(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEBUGLINKDECISION
  
  # @@protoc_insertion_point(class_scope:DebugLinkDecision)

class DebugLinkGetState(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEBUGLINKGETSTATE
  
  # @@protoc_insertion_point(class_scope:DebugLinkGetState)

class DebugLinkState(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEBUGLINKSTATE
  
  # @@protoc_insertion_point(class_scope:DebugLinkState)

class DebugLinkStop(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEBUGLINKSTOP
  
  # @@protoc_insertion_point(class_scope:DebugLinkStop)

class Success(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUCCESS
  
  # @@protoc_insertion_point(class_scope:Success)

class Failure(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FAILURE
  
  # @@protoc_insertion_point(class_scope:Failure)

class GetUUID(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETUUID
  
  # @@protoc_insertion_point(class_scope:GetUUID)

class UUID(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UUID
  
  # @@protoc_insertion_point(class_scope:UUID)

class ButtonRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUTTONREQUEST
  
  # @@protoc_insertion_point(class_scope:ButtonRequest)

class ButtonAck(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUTTONACK
  
  # @@protoc_insertion_point(class_scope:ButtonAck)

class ButtonCancel(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUTTONCANCEL
  
  # @@protoc_insertion_point(class_scope:ButtonCancel)

class PinMatrixRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PINMATRIXREQUEST
  
  # @@protoc_insertion_point(class_scope:PinMatrixRequest)

class PinMatrixAck(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PINMATRIXACK
  
  # @@protoc_insertion_point(class_scope:PinMatrixAck)

class PinMatrixCancel(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PINMATRIXCANCEL
  
  # @@protoc_insertion_point(class_scope:PinMatrixCancel)

class GetEntropy(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETENTROPY
  
  # @@protoc_insertion_point(class_scope:GetEntropy)

class Entropy(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENTROPY
  
  # @@protoc_insertion_point(class_scope:Entropy)

class SetMaxFeeKb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SETMAXFEEKB
  
  # @@protoc_insertion_point(class_scope:SetMaxFeeKb)

class GetMasterPublicKey(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETMASTERPUBLICKEY
  
  # @@protoc_insertion_point(class_scope:GetMasterPublicKey)

class MasterPublicKey(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MASTERPUBLICKEY
  
  # @@protoc_insertion_point(class_scope:MasterPublicKey)

class GetAddress(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETADDRESS
  
  # @@protoc_insertion_point(class_scope:GetAddress)

class Address(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADDRESS
  
  # @@protoc_insertion_point(class_scope:Address)

class LoadDevice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOADDEVICE
  
  # @@protoc_insertion_point(class_scope:LoadDevice)

class ResetDevice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESETDEVICE
  
  # @@protoc_insertion_point(class_scope:ResetDevice)

class SignTx(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SIGNTX
  
  # @@protoc_insertion_point(class_scope:SignTx)

class TxRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TXREQUEST
  
  # @@protoc_insertion_point(class_scope:TxRequest)

class TxInput(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TXINPUT
  
  # @@protoc_insertion_point(class_scope:TxInput)

class TxOutput(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TXOUTPUT
  
  # @@protoc_insertion_point(class_scope:TxOutput)

# @@protoc_insertion_point(module_scope)
