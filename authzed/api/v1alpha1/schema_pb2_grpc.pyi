"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import authzed.api.v1alpha1.schema_pb2
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class SchemaServiceStub:
    """SchemaService implements operations on a Permissions System's Schema."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    ReadSchema: grpc.UnaryUnaryMultiCallable[
        authzed.api.v1alpha1.schema_pb2.ReadSchemaRequest,
        authzed.api.v1alpha1.schema_pb2.ReadSchemaResponse,
    ]
    """Read returns the current Object Definitions for a Permissions System.

    Errors include:
    - INVALID_ARGUMENT: a provided value has failed to semantically validate
    - NOT_FOUND: one of the Object Definitions being requested does not exist
    """

    WriteSchema: grpc.UnaryUnaryMultiCallable[
        authzed.api.v1alpha1.schema_pb2.WriteSchemaRequest,
        authzed.api.v1alpha1.schema_pb2.WriteSchemaResponse,
    ]
    """Write overwrites the current Object Definitions for a Permissions System.

    Any Object Definitions that exist, but are not included will be deleted.
    """

class SchemaServiceAsyncStub:
    """SchemaService implements operations on a Permissions System's Schema."""

    ReadSchema: grpc.aio.UnaryUnaryMultiCallable[
        authzed.api.v1alpha1.schema_pb2.ReadSchemaRequest,
        authzed.api.v1alpha1.schema_pb2.ReadSchemaResponse,
    ]
    """Read returns the current Object Definitions for a Permissions System.

    Errors include:
    - INVALID_ARGUMENT: a provided value has failed to semantically validate
    - NOT_FOUND: one of the Object Definitions being requested does not exist
    """

    WriteSchema: grpc.aio.UnaryUnaryMultiCallable[
        authzed.api.v1alpha1.schema_pb2.WriteSchemaRequest,
        authzed.api.v1alpha1.schema_pb2.WriteSchemaResponse,
    ]
    """Write overwrites the current Object Definitions for a Permissions System.

    Any Object Definitions that exist, but are not included will be deleted.
    """

class SchemaServiceServicer(metaclass=abc.ABCMeta):
    """SchemaService implements operations on a Permissions System's Schema."""

    @abc.abstractmethod
    def ReadSchema(
        self,
        request: authzed.api.v1alpha1.schema_pb2.ReadSchemaRequest,
        context: _ServicerContext,
    ) -> typing.Union[authzed.api.v1alpha1.schema_pb2.ReadSchemaResponse, collections.abc.Awaitable[authzed.api.v1alpha1.schema_pb2.ReadSchemaResponse]]:
        """Read returns the current Object Definitions for a Permissions System.

        Errors include:
        - INVALID_ARGUMENT: a provided value has failed to semantically validate
        - NOT_FOUND: one of the Object Definitions being requested does not exist
        """

    @abc.abstractmethod
    def WriteSchema(
        self,
        request: authzed.api.v1alpha1.schema_pb2.WriteSchemaRequest,
        context: _ServicerContext,
    ) -> typing.Union[authzed.api.v1alpha1.schema_pb2.WriteSchemaResponse, collections.abc.Awaitable[authzed.api.v1alpha1.schema_pb2.WriteSchemaResponse]]:
        """Write overwrites the current Object Definitions for a Permissions System.

        Any Object Definitions that exist, but are not included will be deleted.
        """

def add_SchemaServiceServicer_to_server(servicer: SchemaServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
