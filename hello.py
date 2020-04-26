def app(environ, start_response):
    body = '[bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]'
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return body
    
    
    #gunicorn --bind='0.0.0.0:8080' hello:test