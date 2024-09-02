# peer_server.py
import grpc
from concurrent import futures
import threading

# Importa los archivos generados por el proto
import peer_service_pb2
import peer_service_pb2_grpc

class PeerService(peer_service_pb2_grpc.PeerServiceServicer):
    def __init__(self):
        self.peers = []
        self.files = {}
        self.lock = threading.Lock()  # Para manejo concurrente

    def RegisterPeer(self, request, context):
        with self.lock:
            self.peers.append({
                'peer_id': request.peer_id,
                'ip': request.ip,
                'port': request.port
            })
        return peer_service_pb2.RegisterResponse(success=True, message="Peer registered successfully.")

    def SearchFile(self, request, context):
        with self.lock:
            results = []
            for peer, files in self.files.items():
                for file in files:
                    if request.query in file:
                        results.append(f"{peer}/{file}")
        return peer_service_pb2.SearchResponse(file_urls=results)

    def DownloadFile(self, request, context):
        with self.lock:
            file_content = self.files.get(request.file_name, None)
        if file_content:
            return peer_service_pb2.FileResponse(file_content=file_content)
        else:
            context.set_details('File not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return peer_service_pb2.FileResponse()

    def UploadFile(self, request, context):
        with self.lock:
            self.files[request.file_name] = request.file_content
        return peer_service_pb2.UploadResponse(success=True, message="File uploaded successfully.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    peer_service_pb2_grpc.add_PeerServiceServicer_to_server(PeerService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
