-- SETTING UP THE BACKEND --
1. cd .\server\
2. python -m venv venv
3. .\venv\Scripts\activate

    Double-check venv:
    1. Ctrl + Shift + P
    2. Search "Python: Select Interpreter"
    3. "Enter interpreter path..." -> "Find..."
    4. Select server -> venv -> Scripts -> python

4. pip install -r .\requirements.txt
5. python .\main.py
6. go to localhost:8000

-- SETTING UP THE FRONTEND --
1. create new Terminal
2. cd .\frontend\
3. npm install
4. npm install axios @emotion/react @emotion/styled @mui/material vite
5. npm run dev
6. go to localhost:5173