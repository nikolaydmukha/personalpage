# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc


import protos.pilling.rpc.protos.client_pb2 as client__pb2


class ClientStub(object):
  """Client credentials service 
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Auth = channel.unary_unary(
        '/Client/Auth',
        request_serializer=client__pb2.AuthRequest.SerializeToString,
        response_deserializer=client__pb2.AuthReply.FromString,
        )
    self.Search = channel.unary_unary(
        '/Client/Search',
        request_serializer=client__pb2.SearchRequest.SerializeToString,
        response_deserializer=client__pb2.SearchReply.FromString,
        )


class ClientServicer(object):
  """Client credentials service 
  """

  def Auth(self, request, context):
    """Auth client 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Search(self, request, context):
    """Search for a client 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClientServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Auth': grpc.unary_unary_rpc_method_handler(
          servicer.Auth,
          request_deserializer=client__pb2.AuthRequest.FromString,
          response_serializer=client__pb2.AuthReply.SerializeToString,
      ),
      'Search': grpc.unary_unary_rpc_method_handler(
          servicer.Search,
          request_deserializer=client__pb2.SearchRequest.FromString,
          response_serializer=client__pb2.SearchReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Client', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
