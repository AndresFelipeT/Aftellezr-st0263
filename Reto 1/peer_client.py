# peer_client.py
import grpc
import peer_service_pb2
import peer_service_pb2_grpc

def run_client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = peer_service_pb2_grpc.PeerServiceStub(channel)

        # Registro de un nuevo peer
        response = stub.RegisterPeer(peer_service_pb2.RegisterRequest(peer_id="peer1", ip="127.0.0.1", port=50051))
        print("RegisterPeer response: ", response.message)

        # Subir un archivo
        with open('example.txt', 'rb') as f:
            file_content = f.read()
        response = stub.UploadFile(peer_service_pb2.UploadRequest(file_name="example.txt", file_content=file_content))
        print("UploadFile response: ", response.message)

        # Buscar un archivo
        response = stub.SearchFile(peer_service_pb2.SearchRequest(query="example"))
        print("SearchFile response: ", response.file_urls)

        # Descargar un archivo
        response = stub.DownloadFile(peer_service_pb2.DownloadRequest(file_name="example.txt"))
        with open('downloaded_example.txt', 'wb') as f:
            f.write(response.file_content)
        print("File downloaded successfully.")

if __name__ == '__main__':
    run_client()

