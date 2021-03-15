from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from recommendationsBook_pb2 import (
    RecommendationBookRequest,
    BookRecommendation,
    RecommendationBookResponse,
    BookNameRequest,
    BookCategoryRequest,
    
)
import recommendationsBook_pb2_grpc

books_by_category = {
    BookCategory.MYSTERY: [
        BookRecommendation(id=1, title="The Maltese Falcon"),
        BookRecommendation(id=2, title="Murder on the Orient Express"),
        BookRecommendation(id=3, title="The Hound of the Baskervilles"),
    ],
    BookCategory.SCIENCE_FICTION: [
        BookRecommendation(id=4, title="The Hitchhiker's Guide To The Galaxy"),
        BookRecommendation(id=5, title="Ender's Game"),
        BookRecommendation(id=6, title="The Dune Chronicles"),
    ],
    BookCategory.SELF_HELP: [
        BookRecommendation(
            id=7, title="The 7 Habits of Highly Effective People"
        ),
        BookRecommendation(
            id=8, title="How to Win Friends and Influence People"
        ),
        BookRecommendation(id=9, title="Man’s Search for Meaning"),
    ],
}

# Acesso ah base de dados


class BookService(recommendationsBook_pb2_grpc.RecommendationsBookServicer):
    def RecommendBook(self, request, context):
        
        books_to_recommend_by_criteria = {}
        
        for x in request.criteria:
            books_with_criteria = books_database[x]
            num_results = min(request.max_results, len(books_to_recommend))
            books_to_recommend = random.sample(books_with_criteria, num_results)
            books_to_recommend_by_criteria[x] = books_to_recommend

        return RecommendationResponse(recommendations=books_to_recommend_by_criteria)
        
    def SearchByName(self, request, context):
        if request.category not in books_by_category:
            raise NotFound("Category not found")

        books_for_category = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(books_for_category, num_results)

        return RecommendationResponse(recommendations=books_to_recommend)
        
    def SearchByCategory(self, request, context):
        if request.category not in books_by_category:
            raise NotFound("Category not found")

        books_for_category = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(books_for_category, num_results)

        return RecommendationResponse(recommendations=books_to_recommend)
        
    def GetBookById(self, request, context):
        
     
    def GetBookByCategory(self, request, context):
        


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(), server
    )

    with open("server.key", "rb") as fp:
        server_key = fp.read()
    with open("server.pem", "rb") as fp:
        server_cert = fp.read()
    with open("ca.pem", "rb") as fp:
        ca_cert = fp.read()

    creds = grpc.ssl_server_credentials(
        [(server_key, server_cert)],
        root_certificates=ca_cert,
        require_client_auth=True,
    )
    server.add_secure_port("[::]:443", creds)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
