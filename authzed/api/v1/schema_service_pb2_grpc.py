# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from authzed.api.v1 import schema_service_pb2 as authzed_dot_api_dot_v1_dot_schema__service__pb2


class SchemaServiceStub(object):
    """SchemaService implements operations on a Permissions System's Schema.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReadSchema = channel.unary_unary(
                '/authzed.api.v1.SchemaService/ReadSchema',
                request_serializer=authzed_dot_api_dot_v1_dot_schema__service__pb2.ReadSchemaRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_schema__service__pb2.ReadSchemaResponse.FromString,
                )
        self.WriteSchema = channel.unary_unary(
                '/authzed.api.v1.SchemaService/WriteSchema',
                request_serializer=authzed_dot_api_dot_v1_dot_schema__service__pb2.WriteSchemaRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_schema__service__pb2.WriteSchemaResponse.FromString,
                )


class SchemaServiceServicer(object):
    """SchemaService implements operations on a Permissions System's Schema.
    """

    def ReadSchema(self, request, context):
        """Read returns the current Object Definitions for a Permissions System.

        Errors include:
        - INVALID_ARGUMENT: a provided value has failed to semantically validate
        - NOT_FOUND: no schema has been defined
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteSchema(self, request, context):
        """Write overwrites the current Object Definitions for a Permissions System.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SchemaServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReadSchema': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadSchema,
                    request_deserializer=authzed_dot_api_dot_v1_dot_schema__service__pb2.ReadSchemaRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_schema__service__pb2.ReadSchemaResponse.SerializeToString,
            ),
            'WriteSchema': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteSchema,
                    request_deserializer=authzed_dot_api_dot_v1_dot_schema__service__pb2.WriteSchemaRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_schema__service__pb2.WriteSchemaResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'authzed.api.v1.SchemaService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SchemaService(object):
    """SchemaService implements operations on a Permissions System's Schema.
    """

    @staticmethod
    def ReadSchema(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.SchemaService/ReadSchema',
            authzed_dot_api_dot_v1_dot_schema__service__pb2.ReadSchemaRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_schema__service__pb2.ReadSchemaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteSchema(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.SchemaService/WriteSchema',
            authzed_dot_api_dot_v1_dot_schema__service__pb2.WriteSchemaRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_schema__service__pb2.WriteSchemaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
