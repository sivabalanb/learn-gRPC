import grpc
import calculator_pb2
import calculator_pb2_grpc
from concurrent import futures

class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def Square(self, request, context):
        result = request.number * request.number
        return calculator_pb2.RpcOutput(result=result)

    def Add(self, request, context):
        result = request.number1 + request.number
        return calculator_pb2.RpcOutput(result=result)

    def Subtract(self, request, context):
        result = request.number1 - request.number
        return calculator_pb2.RpcOutput(result=result)

    def Multiply(self, request, context):
        result = request.number1 * request.number
        return calculator_pb2.RpcOutput(result=result)

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    run_server()
