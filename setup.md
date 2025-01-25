-- BACKEND --
Before executing the backend Python script (main.py):

1. .\server > .\venv\Scripts\activate (activates venv: virtual environment)
2. pip install -r .\requirements.txt (makes sure all dependencies in requirements.txt are present in venv)

Include all required dependencies / libraries in requirements.txt

If VSCode does not detect venv:

1. Ctrl + Shift + P
2. Search "Python: Select Interpreter"
3. "Enter interpreter path..." -> "Find..."
4. Select ./server/venv/Scripts/python

To run Uvicorn server:

1. (venv) .\server > python .\main.py

To test:

1. GET endpoint: go to localhost:8000/[location specified in @app.get]
2. POST endpoint: use the REST Client extension, write a .http file, see format in example file

-- FRONTEND --
To setup frontend:

1. Make sure Node.js is installed (may require restart)
2. . > npm create vite@latest client --template react
3. Select React, then JS in terminal
4. .\client\ > npm install
5. npm install axios

To connect frontend with backend:

1. mkdir .\src\components
2. touch .\src\api.js
3. See code in api.js: to change backend, simply change address indicated in api.js
4. Setup relevant components file calling the API (see examples)

To run frontend:

1. .\client > npm run dev
2. Make sure displayed port matches ports in origins in backend main.py
3. Reload backend server if needed
