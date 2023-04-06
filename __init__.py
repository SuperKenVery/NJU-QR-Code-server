from .qr_code_server import server

create_app=server.create_app

__all__=['server','create_app']