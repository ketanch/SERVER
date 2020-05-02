This folder has 2 python files server.py and client.py making a server-client model.

SERVER.PY:
This program sets up a http web server using Flask framework. It accepts a json object of the format:
{"data":<value to be encoded>}
and returns its correspnding sha256 hash in the json format:
{"hash":<sha256 of given data>}
To start the server simply run:
  
python server.py

CLIENT.PY:
This program uses the requests module to make a POST request to above mentioned server. To run the client use:

python client.py <url> <data-to-be-encoded>
