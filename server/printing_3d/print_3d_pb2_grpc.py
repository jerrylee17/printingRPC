# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import print_3d_pb2 as print__3d__pb2


class Printer3dStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Handle3dPrint = channel.unary_unary(
        '/Printer3d/Handle3dPrint',
        request_serializer=print__3d__pb2.Print3dRequest.SerializeToString,
        response_deserializer=print__3d__pb2.Print3dResponse.FromString,
        )


class Printer3dServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Handle3dPrint(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_Printer3dServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Handle3dPrint': grpc.unary_unary_rpc_method_handler(
          servicer.Handle3dPrint,
          request_deserializer=print__3d__pb2.Print3dRequest.FromString,
          response_serializer=print__3d__pb2.Print3dResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Printer3d', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))