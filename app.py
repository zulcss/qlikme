from qlikme import app

if __name__ == '__main__':
    context = ('certs/server.crt', 'certs/server.key')
    app.run(debug=True, 
            host='0.0.0.0',
            ssl_context=context)
