from qlikme import app

if __name__ == '__main__':
    app.run(debug=True, 
            host='0.0.0.0',
            ssl_context=('certs/server.csr', 'certs/server.key'))
