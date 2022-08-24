"""The Python implementation of the GRPC western_movies.WesternMovies client."""

from __future__ import print_function

import logging

import grpc
import western_movies_pb2 as pb2
import western_movies_pb2_grpc as pb2_grpc

def run():
  with grpc.insecure_channel('localhost:50051') as channel:
    stub = pb2_grpc.WesternMoviesStub(channel)
    request = pb2.NameRequest(name='The Good, The Bad And The Ugly')
    response = stub.GetByName(request)
  print("Western client received: \n\n" + str(response))


if __name__ == '__main__':
    logging.basicConfig()
    run()
