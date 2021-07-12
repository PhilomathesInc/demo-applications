# Minimal Python Application

This is a tiny demo application in Python using the Flask web framework. It exposes a web server listening on port 8080 which responds to the following routes:

| Route           | HTTP response status codes | Response Body     |
|-----------------|----------------------------|-------------------|
| `/healthz`      | 200                        | `{"status":"ok"}` |
| `/errorz`       | 500                        |                   |
| Any other route | 404                        |                   |
