# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: actor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='actor.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x61\x63tor.proto\"\x87\x03\n\x05\x41\x63tor\x12\x18\n\x10\x61\x63tor_public_key\x18\x01 \x01(\t\x12\x1a\n\x12manager_public_key\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x1e\n\x04role\x18\x04 \x01(\x0e\x32\x10.Actor.ActorRole\x12\x1f\n\x07profile\x18\x05 \x03(\x0b\x32\x0e.Actor.Profile\x12\x11\n\ttimestamp\x18\x07 \x01(\x04\x12\x16\n\x0etransaction_id\x18\x08 \x01(\t\x1a\x66\n\x07Profile\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\"\n\x06status\x18\x02 \x01(\x0e\x32\x12.Actor.ActorStatus\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x12\x16\n\x0etransaction_id\x18\x04 \x01(\t\"4\n\tActorRole\x12\x0f\n\x0bINSTITUTION\x10\x00\x12\x0b\n\x07TEACHER\x10\x01\x12\t\n\x05OTHER\x10\x02\"2\n\x0b\x41\x63torStatus\x12\x0b\n\x07WAITING\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\n\n\x06REJECT\x10\x02\")\n\x0e\x41\x63torContainer\x12\x17\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x06.Actorb\x06proto3')
)



_ACTOR_ACTORROLE = _descriptor.EnumDescriptor(
  name='ActorRole',
  full_name='Actor.ActorRole',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INSTITUTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEACHER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=303,
  serialized_end=355,
)
_sym_db.RegisterEnumDescriptor(_ACTOR_ACTORROLE)

_ACTOR_ACTORSTATUS = _descriptor.EnumDescriptor(
  name='ActorStatus',
  full_name='Actor.ActorStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WAITING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=357,
  serialized_end=407,
)
_sym_db.RegisterEnumDescriptor(_ACTOR_ACTORSTATUS)


_ACTOR_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='Actor.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Actor.Profile.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='Actor.Profile.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Actor.Profile.timestamp', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='Actor.Profile.transaction_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=199,
  serialized_end=301,
)

_ACTOR = _descriptor.Descriptor(
  name='Actor',
  full_name='Actor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actor_public_key', full_name='Actor.actor_public_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manager_public_key', full_name='Actor.manager_public_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='Actor.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='Actor.role', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile', full_name='Actor.profile', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Actor.timestamp', index=5,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='Actor.transaction_id', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ACTOR_PROFILE, ],
  enum_types=[
    _ACTOR_ACTORROLE,
    _ACTOR_ACTORSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=407,
)


_ACTORCONTAINER = _descriptor.Descriptor(
  name='ActorContainer',
  full_name='ActorContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='ActorContainer.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=450,
)

_ACTOR_PROFILE.fields_by_name['status'].enum_type = _ACTOR_ACTORSTATUS
_ACTOR_PROFILE.containing_type = _ACTOR
_ACTOR.fields_by_name['role'].enum_type = _ACTOR_ACTORROLE
_ACTOR.fields_by_name['profile'].message_type = _ACTOR_PROFILE
_ACTOR_ACTORROLE.containing_type = _ACTOR
_ACTOR_ACTORSTATUS.containing_type = _ACTOR
_ACTORCONTAINER.fields_by_name['entries'].message_type = _ACTOR
DESCRIPTOR.message_types_by_name['Actor'] = _ACTOR
DESCRIPTOR.message_types_by_name['ActorContainer'] = _ACTORCONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Actor = _reflection.GeneratedProtocolMessageType('Actor', (_message.Message,), dict(

  Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), dict(
    DESCRIPTOR = _ACTOR_PROFILE,
    __module__ = 'actor_pb2'
    # @@protoc_insertion_point(class_scope:Actor.Profile)
    ))
  ,
  DESCRIPTOR = _ACTOR,
  __module__ = 'actor_pb2'
  # @@protoc_insertion_point(class_scope:Actor)
  ))
_sym_db.RegisterMessage(Actor)
_sym_db.RegisterMessage(Actor.Profile)

ActorContainer = _reflection.GeneratedProtocolMessageType('ActorContainer', (_message.Message,), dict(
  DESCRIPTOR = _ACTORCONTAINER,
  __module__ = 'actor_pb2'
  # @@protoc_insertion_point(class_scope:ActorContainer)
  ))
_sym_db.RegisterMessage(ActorContainer)


# @@protoc_insertion_point(module_scope)
