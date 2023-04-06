import qr_code_server.server as server

def main():
    server.app.run(host='0.0.0.0',port=80,debug=False)

main()