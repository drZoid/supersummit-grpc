"""The Python implementation of the GRPC western_movies.WesternMovies client."""

from __future__ import print_function

import logging

import grpc
import western_movies_pb2
import western_movies_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = western_movies_pb2_grpc.WesternMoviesStub(channel)
        response = stub.GetByName(western_movies_pb2.NameRequest(name='The Good, The Bad And The Ugly'))
    print("Western client received: \n" + str(response))


if __name__ == '__main__':
    logging.basicConfig()
    run()
