@echo off
echo === Adversarial AI - Local Startup ===

echo.
echo [1/2] Starting backend...
cd backend
pip install -r requirements.txt
start "AdversarialAI-Backend" cmd /k "python main.py"
cd ..

timeout /t 3 /nobreak >nul

echo.
echo [2/2] Starting frontend...
cd frontend
call npm install
start "AdversarialAI-Frontend" cmd /k "npm run dev"
cd ..

echo.
echo Servers starting...
echo   API:       http://localhost:8000
echo   API Docs:  http://localhost:8000/docs
echo   Dashboard: http://localhost:3000
echo.
pause
