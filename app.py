def hello(environ, start_response):
	data = b"<h1>Hello</h1>, World!\n"
	start_response("200 OK", [
			("Content-Type", "text/plain"),
			("Content-Length", str(len(data)))
	])
	return iter([data])
