"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import typing

from .watchresources_service_pb2 import *
class WatchResourcesServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    WatchResources:grpc.UnaryStreamMultiCallable[
        global___WatchResourcesRequest,
        global___WatchResourcesResponse] = ...


class WatchResourcesServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def WatchResources(self,
        request: global___WatchResourcesRequest,
        context: grpc.ServicerContext,
    ) -> typing.Iterator[global___WatchResourcesResponse]: ...


def add_WatchResourcesServiceServicer_to_server(servicer: WatchResourcesServiceServicer, server: grpc.Server) -> None: ...
