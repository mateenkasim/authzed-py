"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Metadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    METADATA_MESSAGE_FIELD_NUMBER: builtins.int

    @property
    def metadata_message(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]: ...

    def __init__(self,
        *,
        metadata_message : typing.Optional[typing.Iterable[google.protobuf.any_pb2.Any]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"metadata_message",b"metadata_message"]) -> None: ...
global___Metadata = Metadata

class NamespaceDefinition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    name: typing.Text = ...

    @property
    def relation(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Relation]: ...

    @property
    def metadata(self) -> global___Metadata: ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        relation : typing.Optional[typing.Iterable[global___Relation]] = ...,
        metadata : typing.Optional[global___Metadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"metadata",b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"metadata",b"metadata",u"name",b"name",u"relation",b"relation"]) -> None: ...
global___NamespaceDefinition = NamespaceDefinition

class Relation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    USERSET_REWRITE_FIELD_NUMBER: builtins.int
    TYPE_INFORMATION_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    name: typing.Text = ...

    @property
    def userset_rewrite(self) -> global___UsersetRewrite: ...

    @property
    def type_information(self) -> global___TypeInformation: ...

    @property
    def metadata(self) -> global___Metadata: ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        userset_rewrite : typing.Optional[global___UsersetRewrite] = ...,
        type_information : typing.Optional[global___TypeInformation] = ...,
        metadata : typing.Optional[global___Metadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"metadata",b"metadata",u"type_information",b"type_information",u"userset_rewrite",b"userset_rewrite"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"metadata",b"metadata",u"name",b"name",u"type_information",b"type_information",u"userset_rewrite",b"userset_rewrite"]) -> None: ...
global___Relation = Relation

class TypeInformation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ALLOWED_DIRECT_RELATIONS_FIELD_NUMBER: builtins.int

    @property
    def allowed_direct_relations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AllowedRelation]: ...

    def __init__(self,
        *,
        allowed_direct_relations : typing.Optional[typing.Iterable[global___AllowedRelation]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"allowed_direct_relations",b"allowed_direct_relations"]) -> None: ...
global___TypeInformation = TypeInformation

class AllowedRelation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class PublicWildcard(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

        def __init__(self,
            ) -> None: ...

    NAMESPACE_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    PUBLIC_WILDCARD_FIELD_NUMBER: builtins.int
    namespace: typing.Text = ...
    relation: typing.Text = ...

    @property
    def public_wildcard(self) -> global___AllowedRelation.PublicWildcard: ...

    def __init__(self,
        *,
        namespace : typing.Text = ...,
        relation : typing.Text = ...,
        public_wildcard : typing.Optional[global___AllowedRelation.PublicWildcard] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"public_wildcard",b"public_wildcard",u"relation",b"relation",u"relation_or_wildcard",b"relation_or_wildcard"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"namespace",b"namespace",u"public_wildcard",b"public_wildcard",u"relation",b"relation",u"relation_or_wildcard",b"relation_or_wildcard"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"relation_or_wildcard",b"relation_or_wildcard"]) -> typing.Optional[typing_extensions.Literal["relation","public_wildcard"]]: ...
global___AllowedRelation = AllowedRelation

class UsersetRewrite(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UNION_FIELD_NUMBER: builtins.int
    INTERSECTION_FIELD_NUMBER: builtins.int
    EXCLUSION_FIELD_NUMBER: builtins.int

    @property
    def union(self) -> global___SetOperation: ...

    @property
    def intersection(self) -> global___SetOperation: ...

    @property
    def exclusion(self) -> global___SetOperation: ...

    def __init__(self,
        *,
        union : typing.Optional[global___SetOperation] = ...,
        intersection : typing.Optional[global___SetOperation] = ...,
        exclusion : typing.Optional[global___SetOperation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"exclusion",b"exclusion",u"intersection",b"intersection",u"rewrite_operation",b"rewrite_operation",u"union",b"union"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"exclusion",b"exclusion",u"intersection",b"intersection",u"rewrite_operation",b"rewrite_operation",u"union",b"union"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"rewrite_operation",b"rewrite_operation"]) -> typing.Optional[typing_extensions.Literal["union","intersection","exclusion"]]: ...
global___UsersetRewrite = UsersetRewrite

class SetOperation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Child(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class This(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

            def __init__(self,
                ) -> None: ...

        _THIS_FIELD_NUMBER: builtins.int
        COMPUTED_USERSET_FIELD_NUMBER: builtins.int
        TUPLE_TO_USERSET_FIELD_NUMBER: builtins.int
        USERSET_REWRITE_FIELD_NUMBER: builtins.int

        @property
        def _this(self) -> global___SetOperation.Child.This: ...

        @property
        def computed_userset(self) -> global___ComputedUserset: ...

        @property
        def tuple_to_userset(self) -> global___TupleToUserset: ...

        @property
        def userset_rewrite(self) -> global___UsersetRewrite: ...

        def __init__(self,
            *,
            _this : typing.Optional[global___SetOperation.Child.This] = ...,
            computed_userset : typing.Optional[global___ComputedUserset] = ...,
            tuple_to_userset : typing.Optional[global___TupleToUserset] = ...,
            userset_rewrite : typing.Optional[global___UsersetRewrite] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"_this",b"_this",u"child_type",b"child_type",u"computed_userset",b"computed_userset",u"tuple_to_userset",b"tuple_to_userset",u"userset_rewrite",b"userset_rewrite"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"_this",b"_this",u"child_type",b"child_type",u"computed_userset",b"computed_userset",u"tuple_to_userset",b"tuple_to_userset",u"userset_rewrite",b"userset_rewrite"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal[u"child_type",b"child_type"]) -> typing.Optional[typing_extensions.Literal["_this","computed_userset","tuple_to_userset","userset_rewrite"]]: ...

    CHILD_FIELD_NUMBER: builtins.int

    @property
    def child(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SetOperation.Child]: ...

    def __init__(self,
        *,
        child : typing.Optional[typing.Iterable[global___SetOperation.Child]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"child",b"child"]) -> None: ...
global___SetOperation = SetOperation

class TupleToUserset(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Tupleset(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        RELATION_FIELD_NUMBER: builtins.int
        relation: typing.Text = ...

        def __init__(self,
            *,
            relation : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"relation",b"relation"]) -> None: ...

    TUPLESET_FIELD_NUMBER: builtins.int
    COMPUTED_USERSET_FIELD_NUMBER: builtins.int

    @property
    def tupleset(self) -> global___TupleToUserset.Tupleset: ...

    @property
    def computed_userset(self) -> global___ComputedUserset: ...

    def __init__(self,
        *,
        tupleset : typing.Optional[global___TupleToUserset.Tupleset] = ...,
        computed_userset : typing.Optional[global___ComputedUserset] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"computed_userset",b"computed_userset",u"tupleset",b"tupleset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"computed_userset",b"computed_userset",u"tupleset",b"tupleset"]) -> None: ...
global___TupleToUserset = TupleToUserset

class ComputedUserset(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Object(metaclass=_Object):
        V = typing.NewType('V', builtins.int)

    TUPLE_OBJECT = ComputedUserset.Object.V(0)
    TUPLE_USERSET_OBJECT = ComputedUserset.Object.V(1)

    class _Object(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Object.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TUPLE_OBJECT = ComputedUserset.Object.V(0)
        TUPLE_USERSET_OBJECT = ComputedUserset.Object.V(1)

    OBJECT_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    object: global___ComputedUserset.Object.V = ...
    relation: typing.Text = ...

    def __init__(self,
        *,
        object : global___ComputedUserset.Object.V = ...,
        relation : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"object",b"object",u"relation",b"relation"]) -> None: ...
global___ComputedUserset = ComputedUserset
