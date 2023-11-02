import grpc
import calculator_pb2
import calculator_pb2_grpc

def run_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    # Call the Square method
    number = 5
    request = calculator_pb2.RpcInput(number=number)
    response = stub.Square(request)
    print(f"Square of {number} is: {response.result}")

    # Call the Add method
    number1 = 10
    request = calculator_pb2.RpcInput(number=number1)
    response = stub.Add(request)
    print(f"{number1} + 3 = {response.result}")

    # Call the Subtract method
    number1 = 10
    request = calculator_pb2.RpcInput(number=3)
    response = stub.Subtract(request)
    print(f"{number1} - 3 = {response.result}")

    # Call the Multiply method
    number1 = 7
    request = calculator_pb2.RpcInput(number=2)
    response = stub.Multiply(request)
    print(f"{number1} * 2 = {response.result}")

if __name__ == "__main__":
    run_client()
