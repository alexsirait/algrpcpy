import grpc
from concurrent import futures
import mysql.connector
import barang_pb2
import barang_pb2_grpc

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="mahasiswa"
    )

class BarangServiceServicer(barang_pb2_grpc.BarangServiceServicer):
    def CreateBarang(self, request, context):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tbl_barang (barang, harga) VALUES (%s, %s)",
                       (request.barang, request.harga))
        conn.commit()
        cursor.close()
        conn.close()
        return barang_pb2.BarangResponse(message="Barang created successfully")

    def GetBarang(self, request, context):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_barang WHERE id = %s", (request.id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row:
            return barang_pb2.BarangResponse(
                message="Barang found",
                barang=barang_pb2.Barang(
                    id=row['id'],
                    barang=row['barang'],
                    harga=row['harga']
                )
            )
        return barang_pb2.BarangResponse(message="Barang not found")

    def UpdateBarang(self, request, context):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tbl_barang SET barang = %s, harga = %s WHERE id = %s",
                       (request.barang, request.harga, request.id))
        conn.commit()
        cursor.close()
        conn.close()
        return barang_pb2.BarangResponse(message="Barang updated successfully")

    def DeleteBarang(self, request, context):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_barang WHERE id = %s", (request.id,))
        conn.commit()
        cursor.close()
        conn.close()
        return barang_pb2.BarangResponse(message="Barang deleted successfully")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    barang_pb2_grpc.add_BarangServiceServicer_to_server(BarangServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started, listening on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
