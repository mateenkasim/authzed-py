"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import authzed.api.v1.core_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _LookupPermissionship:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _LookupPermissionshipEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_LookupPermissionship.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    LOOKUP_PERMISSIONSHIP_UNSPECIFIED: _LookupPermissionship.ValueType  # 0
    LOOKUP_PERMISSIONSHIP_HAS_PERMISSION: _LookupPermissionship.ValueType  # 1
    LOOKUP_PERMISSIONSHIP_CONDITIONAL_PERMISSION: _LookupPermissionship.ValueType  # 2

class LookupPermissionship(_LookupPermissionship, metaclass=_LookupPermissionshipEnumTypeWrapper):
    """LookupPermissionship represents whether a Lookup response was partially evaluated or not"""

LOOKUP_PERMISSIONSHIP_UNSPECIFIED: LookupPermissionship.ValueType  # 0
LOOKUP_PERMISSIONSHIP_HAS_PERMISSION: LookupPermissionship.ValueType  # 1
LOOKUP_PERMISSIONSHIP_CONDITIONAL_PERMISSION: LookupPermissionship.ValueType  # 2
global___LookupPermissionship = LookupPermissionship

class Consistency(google.protobuf.message.Message):
    """Consistency will define how a request is handled by the backend.
    By defining a consistency requirement, and a token at which those
    requirements should be applied, where applicable.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MINIMIZE_LATENCY_FIELD_NUMBER: builtins.int
    AT_LEAST_AS_FRESH_FIELD_NUMBER: builtins.int
    AT_EXACT_SNAPSHOT_FIELD_NUMBER: builtins.int
    FULLY_CONSISTENT_FIELD_NUMBER: builtins.int
    minimize_latency: builtins.bool
    """minimize_latency indicates that the latency for the call should be
    minimized by having the system select the fastest snapshot available.
    """
    @property
    def at_least_as_fresh(self) -> authzed.api.v1.core_pb2.ZedToken:
        """at_least_as_fresh indicates that all data used in the API call must be
        *at least as fresh* as that found in the ZedToken; more recent data might
        be used if available or faster.
        """
    @property
    def at_exact_snapshot(self) -> authzed.api.v1.core_pb2.ZedToken:
        """at_exact_snapshot indicates that all data used in the API call must be
        *at the given* snapshot in time; if the snapshot is no longer available,
        an error will be returned to the caller.
        """
    fully_consistent: builtins.bool
    """fully_consistent indicates that all data used in the API call *must* be
    at the most recent snapshot found.

    NOTE: using this method can be *quite slow*, so unless there is a need to
    do so, it is recommended to use `at_least_as_fresh` with a stored
    ZedToken.
    """
    def __init__(
        self,
        *,
        minimize_latency: builtins.bool = ...,
        at_least_as_fresh: authzed.api.v1.core_pb2.ZedToken | None = ...,
        at_exact_snapshot: authzed.api.v1.core_pb2.ZedToken | None = ...,
        fully_consistent: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["at_exact_snapshot", b"at_exact_snapshot", "at_least_as_fresh", b"at_least_as_fresh", "fully_consistent", b"fully_consistent", "minimize_latency", b"minimize_latency", "requirement", b"requirement"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["at_exact_snapshot", b"at_exact_snapshot", "at_least_as_fresh", b"at_least_as_fresh", "fully_consistent", b"fully_consistent", "minimize_latency", b"minimize_latency", "requirement", b"requirement"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["requirement", b"requirement"]) -> typing_extensions.Literal["minimize_latency", "at_least_as_fresh", "at_exact_snapshot", "fully_consistent"] | None: ...

global___Consistency = Consistency

class RelationshipFilter(google.protobuf.message.Message):
    """RelationshipFilter is a collection of filters which when applied to a
    relationship will return relationships that have exactly matching fields.

    resource_type is required. All other fields are optional and if left
    unspecified will not filter relationships.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_TYPE_FIELD_NUMBER: builtins.int
    OPTIONAL_RESOURCE_ID_FIELD_NUMBER: builtins.int
    OPTIONAL_RELATION_FIELD_NUMBER: builtins.int
    OPTIONAL_SUBJECT_FILTER_FIELD_NUMBER: builtins.int
    resource_type: builtins.str
    optional_resource_id: builtins.str
    optional_relation: builtins.str
    @property
    def optional_subject_filter(self) -> global___SubjectFilter: ...
    def __init__(
        self,
        *,
        resource_type: builtins.str = ...,
        optional_resource_id: builtins.str = ...,
        optional_relation: builtins.str = ...,
        optional_subject_filter: global___SubjectFilter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["optional_subject_filter", b"optional_subject_filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["optional_relation", b"optional_relation", "optional_resource_id", b"optional_resource_id", "optional_subject_filter", b"optional_subject_filter", "resource_type", b"resource_type"]) -> None: ...

global___RelationshipFilter = RelationshipFilter

class SubjectFilter(google.protobuf.message.Message):
    """SubjectFilter specifies a filter on the subject of a relationship.

    subject_type is required and all other fields are optional, and will not
    impose any additional requirements if left unspecified.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class RelationFilter(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        RELATION_FIELD_NUMBER: builtins.int
        relation: builtins.str
        def __init__(
            self,
            *,
            relation: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["relation", b"relation"]) -> None: ...

    SUBJECT_TYPE_FIELD_NUMBER: builtins.int
    OPTIONAL_SUBJECT_ID_FIELD_NUMBER: builtins.int
    OPTIONAL_RELATION_FIELD_NUMBER: builtins.int
    subject_type: builtins.str
    optional_subject_id: builtins.str
    @property
    def optional_relation(self) -> global___SubjectFilter.RelationFilter: ...
    def __init__(
        self,
        *,
        subject_type: builtins.str = ...,
        optional_subject_id: builtins.str = ...,
        optional_relation: global___SubjectFilter.RelationFilter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["optional_relation", b"optional_relation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["optional_relation", b"optional_relation", "optional_subject_id", b"optional_subject_id", "subject_type", b"subject_type"]) -> None: ...

global___SubjectFilter = SubjectFilter

class ReadRelationshipsRequest(google.protobuf.message.Message):
    """ReadRelationshipsRequest specifies one or more filters used to read matching
    relationships within the system.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONSISTENCY_FIELD_NUMBER: builtins.int
    RELATIONSHIP_FILTER_FIELD_NUMBER: builtins.int
    @property
    def consistency(self) -> global___Consistency: ...
    @property
    def relationship_filter(self) -> global___RelationshipFilter: ...
    def __init__(
        self,
        *,
        consistency: global___Consistency | None = ...,
        relationship_filter: global___RelationshipFilter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["consistency", b"consistency", "relationship_filter", b"relationship_filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["consistency", b"consistency", "relationship_filter", b"relationship_filter"]) -> None: ...

global___ReadRelationshipsRequest = ReadRelationshipsRequest

class ReadRelationshipsResponse(google.protobuf.message.Message):
    """ReadRelationshipsResponse contains a Relationship found that matches the
    specified relationship filter(s). A instance of this response message will
    be streamed to the client for each relationship found.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    READ_AT_FIELD_NUMBER: builtins.int
    RELATIONSHIP_FIELD_NUMBER: builtins.int
    @property
    def read_at(self) -> authzed.api.v1.core_pb2.ZedToken: ...
    @property
    def relationship(self) -> authzed.api.v1.core_pb2.Relationship: ...
    def __init__(
        self,
        *,
        read_at: authzed.api.v1.core_pb2.ZedToken | None = ...,
        relationship: authzed.api.v1.core_pb2.Relationship | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["read_at", b"read_at", "relationship", b"relationship"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["read_at", b"read_at", "relationship", b"relationship"]) -> None: ...

global___ReadRelationshipsResponse = ReadRelationshipsResponse

class Precondition(google.protobuf.message.Message):
    """Precondition specifies how and the existence or absence of certain
    relationships as expressed through the accompanying filter should affect
    whether or not the operation proceeds.

    MUST_NOT_MATCH will fail the parent request if any relationships match the
    relationships filter.
    MUST_MATCH will fail the parent request if there are no
    relationships that match the filter.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Operation:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _OperationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Precondition._Operation.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        OPERATION_UNSPECIFIED: Precondition._Operation.ValueType  # 0
        OPERATION_MUST_NOT_MATCH: Precondition._Operation.ValueType  # 1
        OPERATION_MUST_MATCH: Precondition._Operation.ValueType  # 2

    class Operation(_Operation, metaclass=_OperationEnumTypeWrapper): ...
    OPERATION_UNSPECIFIED: Precondition.Operation.ValueType  # 0
    OPERATION_MUST_NOT_MATCH: Precondition.Operation.ValueType  # 1
    OPERATION_MUST_MATCH: Precondition.Operation.ValueType  # 2

    OPERATION_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    operation: global___Precondition.Operation.ValueType
    @property
    def filter(self) -> global___RelationshipFilter: ...
    def __init__(
        self,
        *,
        operation: global___Precondition.Operation.ValueType = ...,
        filter: global___RelationshipFilter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter", b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter", "operation", b"operation"]) -> None: ...

global___Precondition = Precondition

class WriteRelationshipsRequest(google.protobuf.message.Message):
    """WriteRelationshipsRequest contains a list of Relationship mutations that
    should be applied to the service. If the optional_preconditions parameter
    is included, all of the specified preconditions must also be satisfied before
    the write will be committed.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UPDATES_FIELD_NUMBER: builtins.int
    OPTIONAL_PRECONDITIONS_FIELD_NUMBER: builtins.int
    @property
    def updates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[authzed.api.v1.core_pb2.RelationshipUpdate]: ...
    @property
    def optional_preconditions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Precondition]:
        """To be bounded by configuration"""
    def __init__(
        self,
        *,
        updates: collections.abc.Iterable[authzed.api.v1.core_pb2.RelationshipUpdate] | None = ...,
        optional_preconditions: collections.abc.Iterable[global___Precondition] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["optional_preconditions", b"optional_preconditions", "updates", b"updates"]) -> None: ...

global___WriteRelationshipsRequest = WriteRelationshipsRequest

class WriteRelationshipsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WRITTEN_AT_FIELD_NUMBER: builtins.int
    @property
    def written_at(self) -> authzed.api.v1.core_pb2.ZedToken: ...
    def __init__(
        self,
        *,
        written_at: authzed.api.v1.core_pb2.ZedToken | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["written_at", b"written_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["written_at", b"written_at"]) -> None: ...

global___WriteRelationshipsResponse = WriteRelationshipsResponse

class DeleteRelationshipsRequest(google.protobuf.message.Message):
    """DeleteRelationshipsRequest specifies which Relationships should be deleted,
    requesting the delete of *ALL* relationships that match the specified
    filters. If the optional_preconditions parameter is included, all of the
    specified preconditions must also be satisfied before the delete will be
    executed.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RELATIONSHIP_FILTER_FIELD_NUMBER: builtins.int
    OPTIONAL_PRECONDITIONS_FIELD_NUMBER: builtins.int
    @property
    def relationship_filter(self) -> global___RelationshipFilter: ...
    @property
    def optional_preconditions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Precondition]:
        """To be bounded by configuration"""
    def __init__(
        self,
        *,
        relationship_filter: global___RelationshipFilter | None = ...,
        optional_preconditions: collections.abc.Iterable[global___Precondition] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["relationship_filter", b"relationship_filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["optional_preconditions", b"optional_preconditions", "relationship_filter", b"relationship_filter"]) -> None: ...

global___DeleteRelationshipsRequest = DeleteRelationshipsRequest

class DeleteRelationshipsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELETED_AT_FIELD_NUMBER: builtins.int
    @property
    def deleted_at(self) -> authzed.api.v1.core_pb2.ZedToken: ...
    def __init__(
        self,
        *,
        deleted_at: authzed.api.v1.core_pb2.ZedToken | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["deleted_at", b"deleted_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deleted_at", b"deleted_at"]) -> None: ...

global___DeleteRelationshipsResponse = DeleteRelationshipsResponse

class CheckPermissionRequest(google.protobuf.message.Message):
    """CheckPermissionRequest issues a check on whether a subject has a permission
    or is a member of a relation, on a specific resource.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONSISTENCY_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    SUBJECT_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    @property
    def consistency(self) -> global___Consistency: ...
    @property
    def resource(self) -> authzed.api.v1.core_pb2.ObjectReference:
        """resource is the resource on which to check the permission or relation."""
    permission: builtins.str
    """permission is the name of the permission (or relation) on which to execute
    the check.
    """
    @property
    def subject(self) -> authzed.api.v1.core_pb2.SubjectReference:
        """subject is the subject that will be checked for the permission or relation."""
    @property
    def context(self) -> google.protobuf.struct_pb2.Struct:
        """context consists of named values that are injected into the caveat evaluation context *"""
    def __init__(
        self,
        *,
        consistency: global___Consistency | None = ...,
        resource: authzed.api.v1.core_pb2.ObjectReference | None = ...,
        permission: builtins.str = ...,
        subject: authzed.api.v1.core_pb2.SubjectReference | None = ...,
        context: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["consistency", b"consistency", "context", b"context", "resource", b"resource", "subject", b"subject"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["consistency", b"consistency", "context", b"context", "permission", b"permission", "resource", b"resource", "subject", b"subject"]) -> None: ...

global___CheckPermissionRequest = CheckPermissionRequest

class PartialCaveatInfo(google.protobuf.message.Message):
    """PartialCaveatInfo carries information necessary for the client to take action
    in the event a response contains a partially evaluated caveat
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MISSING_REQUIRED_CONTEXT_FIELD_NUMBER: builtins.int
    @property
    def missing_required_context(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """missing_required_context is a list of one or more fields that were missing and prevented caveats
        from being fully evaluated
        """
    def __init__(
        self,
        *,
        missing_required_context: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["missing_required_context", b"missing_required_context"]) -> None: ...

global___PartialCaveatInfo = PartialCaveatInfo

class CheckPermissionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Permissionship:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _PermissionshipEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CheckPermissionResponse._Permissionship.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        PERMISSIONSHIP_UNSPECIFIED: CheckPermissionResponse._Permissionship.ValueType  # 0
        PERMISSIONSHIP_NO_PERMISSION: CheckPermissionResponse._Permissionship.ValueType  # 1
        PERMISSIONSHIP_HAS_PERMISSION: CheckPermissionResponse._Permissionship.ValueType  # 2
        PERMISSIONSHIP_CONDITIONAL_PERMISSION: CheckPermissionResponse._Permissionship.ValueType  # 3

    class Permissionship(_Permissionship, metaclass=_PermissionshipEnumTypeWrapper): ...
    PERMISSIONSHIP_UNSPECIFIED: CheckPermissionResponse.Permissionship.ValueType  # 0
    PERMISSIONSHIP_NO_PERMISSION: CheckPermissionResponse.Permissionship.ValueType  # 1
    PERMISSIONSHIP_HAS_PERMISSION: CheckPermissionResponse.Permissionship.ValueType  # 2
    PERMISSIONSHIP_CONDITIONAL_PERMISSION: CheckPermissionResponse.Permissionship.ValueType  # 3

    CHECKED_AT_FIELD_NUMBER: builtins.int
    PERMISSIONSHIP_FIELD_NUMBER: builtins.int
    PARTIAL_CAVEAT_INFO_FIELD_NUMBER: builtins.int
    @property
    def checked_at(self) -> authzed.api.v1.core_pb2.ZedToken: ...
    permissionship: global___CheckPermissionResponse.Permissionship.ValueType
    """Permissionship communicates whether or not the subject has the requested
    permission or has a relationship with the given resource, over the given
    relation.

    This value will be authzed.api.v1.PERMISSIONSHIP_HAS_PERMISSION if the
    requested subject is a member of the computed permission set or there
    exists a relationship with the requested relation from the given resource
    to the given subject.
    """
    @property
    def partial_caveat_info(self) -> global___PartialCaveatInfo:
        """partial_caveat_info holds information of a partially-evaluated caveated response"""
    def __init__(
        self,
        *,
        checked_at: authzed.api.v1.core_pb2.ZedToken | None = ...,
        permissionship: global___CheckPermissionResponse.Permissionship.ValueType = ...,
        partial_caveat_info: global___PartialCaveatInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["checked_at", b"checked_at", "partial_caveat_info", b"partial_caveat_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["checked_at", b"checked_at", "partial_caveat_info", b"partial_caveat_info", "permissionship", b"permissionship"]) -> None: ...

global___CheckPermissionResponse = CheckPermissionResponse

class ExpandPermissionTreeRequest(google.protobuf.message.Message):
    """ExpandPermissionTreeRequest returns a tree representing the expansion of all
    relationships found accessible from a permission or relation on a particular
    resource.

    ExpandPermissionTreeRequest is typically used to determine the full set of
    subjects with a permission, along with the relationships that grant said
    access.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONSISTENCY_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    @property
    def consistency(self) -> global___Consistency: ...
    @property
    def resource(self) -> authzed.api.v1.core_pb2.ObjectReference:
        """resource is the resource over which to run the expansion."""
    permission: builtins.str
    """permission is the name of the permission or relation over which to run the
    expansion for the resource.
    """
    def __init__(
        self,
        *,
        consistency: global___Consistency | None = ...,
        resource: authzed.api.v1.core_pb2.ObjectReference | None = ...,
        permission: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["consistency", b"consistency", "resource", b"resource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["consistency", b"consistency", "permission", b"permission", "resource", b"resource"]) -> None: ...

global___ExpandPermissionTreeRequest = ExpandPermissionTreeRequest

class ExpandPermissionTreeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXPANDED_AT_FIELD_NUMBER: builtins.int
    TREE_ROOT_FIELD_NUMBER: builtins.int
    @property
    def expanded_at(self) -> authzed.api.v1.core_pb2.ZedToken: ...
    @property
    def tree_root(self) -> authzed.api.v1.core_pb2.PermissionRelationshipTree:
        """tree_root is a tree structure whose leaf nodes are subjects, and
        intermediate nodes represent the various operations (union, intersection,
        exclusion) to reach those subjects.
        """
    def __init__(
        self,
        *,
        expanded_at: authzed.api.v1.core_pb2.ZedToken | None = ...,
        tree_root: authzed.api.v1.core_pb2.PermissionRelationshipTree | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expanded_at", b"expanded_at", "tree_root", b"tree_root"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["expanded_at", b"expanded_at", "tree_root", b"tree_root"]) -> None: ...

global___ExpandPermissionTreeResponse = ExpandPermissionTreeResponse

class LookupResourcesRequest(google.protobuf.message.Message):
    """LookupResourcesRequest performs a lookup of all resources of a particular
    kind on which the subject has the specified permission or the relation in
    which the subject exists, streaming back the IDs of those resources.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONSISTENCY_FIELD_NUMBER: builtins.int
    RESOURCE_OBJECT_TYPE_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    SUBJECT_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    @property
    def consistency(self) -> global___Consistency: ...
    resource_object_type: builtins.str
    """resource_object_type is the type of resource object for which the IDs will
    be returned.
    """
    permission: builtins.str
    """permission is the name of the permission or relation for which the subject
    must Check.
    """
    @property
    def subject(self) -> authzed.api.v1.core_pb2.SubjectReference:
        """subject is the subject with access to the resources."""
    @property
    def context(self) -> google.protobuf.struct_pb2.Struct:
        """context consists of named values that are injected into the caveat evaluation context *"""
    def __init__(
        self,
        *,
        consistency: global___Consistency | None = ...,
        resource_object_type: builtins.str = ...,
        permission: builtins.str = ...,
        subject: authzed.api.v1.core_pb2.SubjectReference | None = ...,
        context: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["consistency", b"consistency", "context", b"context", "subject", b"subject"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["consistency", b"consistency", "context", b"context", "permission", b"permission", "resource_object_type", b"resource_object_type", "subject", b"subject"]) -> None: ...

global___LookupResourcesRequest = LookupResourcesRequest

class LookupResourcesResponse(google.protobuf.message.Message):
    """LookupResourcesResponse contains a single matching resource object ID for the
    requested object type, permission, and subject.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOOKED_UP_AT_FIELD_NUMBER: builtins.int
    RESOURCE_OBJECT_ID_FIELD_NUMBER: builtins.int
    PERMISSIONSHIP_FIELD_NUMBER: builtins.int
    PARTIAL_CAVEAT_INFO_FIELD_NUMBER: builtins.int
    @property
    def looked_up_at(self) -> authzed.api.v1.core_pb2.ZedToken: ...
    resource_object_id: builtins.str
    permissionship: global___LookupPermissionship.ValueType
    """permissionship indicates whether the response was partially evaluated or not"""
    @property
    def partial_caveat_info(self) -> global___PartialCaveatInfo:
        """partial_caveat_info holds information of a partially-evaluated caveated response"""
    def __init__(
        self,
        *,
        looked_up_at: authzed.api.v1.core_pb2.ZedToken | None = ...,
        resource_object_id: builtins.str = ...,
        permissionship: global___LookupPermissionship.ValueType = ...,
        partial_caveat_info: global___PartialCaveatInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["looked_up_at", b"looked_up_at", "partial_caveat_info", b"partial_caveat_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["looked_up_at", b"looked_up_at", "partial_caveat_info", b"partial_caveat_info", "permissionship", b"permissionship", "resource_object_id", b"resource_object_id"]) -> None: ...

global___LookupResourcesResponse = LookupResourcesResponse

class LookupSubjectsRequest(google.protobuf.message.Message):
    """LookupSubjectsRequest performs a lookup of all subjects of a particular
    kind for which the subject has the specified permission or the relation in
    which the subject exists, streaming back the IDs of those subjects.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONSISTENCY_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    SUBJECT_OBJECT_TYPE_FIELD_NUMBER: builtins.int
    OPTIONAL_SUBJECT_RELATION_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    @property
    def consistency(self) -> global___Consistency: ...
    @property
    def resource(self) -> authzed.api.v1.core_pb2.ObjectReference:
        """resource is the resource for which all matching subjects for the permission
        or relation will be returned.
        """
    permission: builtins.str
    """permission is the name of the permission (or relation) for which to find
    the subjects.
    """
    subject_object_type: builtins.str
    """subject_object_type is the type of subject object for which the IDs will
    be returned.
    """
    optional_subject_relation: builtins.str
    """optional_subject_relation is the optional relation for the subject."""
    @property
    def context(self) -> google.protobuf.struct_pb2.Struct:
        """context consists of named values that are injected into the caveat evaluation context *"""
    def __init__(
        self,
        *,
        consistency: global___Consistency | None = ...,
        resource: authzed.api.v1.core_pb2.ObjectReference | None = ...,
        permission: builtins.str = ...,
        subject_object_type: builtins.str = ...,
        optional_subject_relation: builtins.str = ...,
        context: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["consistency", b"consistency", "context", b"context", "resource", b"resource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["consistency", b"consistency", "context", b"context", "optional_subject_relation", b"optional_subject_relation", "permission", b"permission", "resource", b"resource", "subject_object_type", b"subject_object_type"]) -> None: ...

global___LookupSubjectsRequest = LookupSubjectsRequest

class LookupSubjectsResponse(google.protobuf.message.Message):
    """LookupSubjectsResponse contains a single matching subject object ID for the
    requested subject object type on the permission or relation.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOOKED_UP_AT_FIELD_NUMBER: builtins.int
    SUBJECT_OBJECT_ID_FIELD_NUMBER: builtins.int
    EXCLUDED_SUBJECT_IDS_FIELD_NUMBER: builtins.int
    PERMISSIONSHIP_FIELD_NUMBER: builtins.int
    PARTIAL_CAVEAT_INFO_FIELD_NUMBER: builtins.int
    SUBJECT_FIELD_NUMBER: builtins.int
    EXCLUDED_SUBJECTS_FIELD_NUMBER: builtins.int
    @property
    def looked_up_at(self) -> authzed.api.v1.core_pb2.ZedToken: ...
    subject_object_id: builtins.str
    """subject_object_id is the Object ID of the subject found. May be a `*` if
    a wildcard was found.
    deprecated: use `subject`
    """
    @property
    def excluded_subject_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """excluded_subject_ids are the Object IDs of the subjects excluded. This list
        will only contain object IDs if `subject_object_id` is a wildcard (`*`) and
        will only be populated if exclusions exist from the wildcard.
        deprecated: use `excluded_subjects`
        """
    permissionship: global___LookupPermissionship.ValueType
    """permissionship indicates whether the response was partially evaluated or not
    deprecated: use `subject.permissionship`
    """
    @property
    def partial_caveat_info(self) -> global___PartialCaveatInfo:
        """partial_caveat_info holds information of a partially-evaluated caveated response
        deprecated: use `subject.partial_caveat_info`
        """
    @property
    def subject(self) -> global___ResolvedSubject:
        """subject is the subject found, along with its permissionship."""
    @property
    def excluded_subjects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ResolvedSubject]:
        """excluded_subjects are the subjects excluded. This list
        will only contain subjects if `subject.subject_object_id` is a wildcard (`*`) and
        will only be populated if exclusions exist from the wildcard.
        """
    def __init__(
        self,
        *,
        looked_up_at: authzed.api.v1.core_pb2.ZedToken | None = ...,
        subject_object_id: builtins.str = ...,
        excluded_subject_ids: collections.abc.Iterable[builtins.str] | None = ...,
        permissionship: global___LookupPermissionship.ValueType = ...,
        partial_caveat_info: global___PartialCaveatInfo | None = ...,
        subject: global___ResolvedSubject | None = ...,
        excluded_subjects: collections.abc.Iterable[global___ResolvedSubject] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["looked_up_at", b"looked_up_at", "partial_caveat_info", b"partial_caveat_info", "subject", b"subject"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["excluded_subject_ids", b"excluded_subject_ids", "excluded_subjects", b"excluded_subjects", "looked_up_at", b"looked_up_at", "partial_caveat_info", b"partial_caveat_info", "permissionship", b"permissionship", "subject", b"subject", "subject_object_id", b"subject_object_id"]) -> None: ...

global___LookupSubjectsResponse = LookupSubjectsResponse

class ResolvedSubject(google.protobuf.message.Message):
    """ResolvedSubject is a single subject resolved within LookupSubjects."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBJECT_OBJECT_ID_FIELD_NUMBER: builtins.int
    PERMISSIONSHIP_FIELD_NUMBER: builtins.int
    PARTIAL_CAVEAT_INFO_FIELD_NUMBER: builtins.int
    subject_object_id: builtins.str
    """subject_object_id is the Object ID of the subject found. May be a `*` if
    a wildcard was found.
    """
    permissionship: global___LookupPermissionship.ValueType
    """permissionship indicates whether the response was partially evaluated or not"""
    @property
    def partial_caveat_info(self) -> global___PartialCaveatInfo:
        """partial_caveat_info holds information of a partially-evaluated caveated response"""
    def __init__(
        self,
        *,
        subject_object_id: builtins.str = ...,
        permissionship: global___LookupPermissionship.ValueType = ...,
        partial_caveat_info: global___PartialCaveatInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["partial_caveat_info", b"partial_caveat_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["partial_caveat_info", b"partial_caveat_info", "permissionship", b"permissionship", "subject_object_id", b"subject_object_id"]) -> None: ...

global___ResolvedSubject = ResolvedSubject
