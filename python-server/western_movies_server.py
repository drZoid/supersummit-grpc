"""The Python implementation of the GRPC western_movies.WesternMovies server."""

from concurrent import futures
import logging

import grpc
import western_movies_pb2
import western_movies_pb2_grpc


class WesternMovies(western_movies_pb2_grpc.WesternMoviesServicer):

    def GetByName(self, request, context):
        return western_movies_pb2.MovieResponse(year='1966', topCast='Clint Eastwood', overview='Best Western Ever!')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    western_movies_pb2_grpc.add_WesternMoviesServicer_to_server(WesternMovies(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
