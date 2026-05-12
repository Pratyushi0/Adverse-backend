#!/usr/bin/env bash
set -e

echo "=== Adversarial AI — Local Startup ==="

# Backend
echo ""
echo "[1/2] Starting backend..."
cd backend
pip install -r requirements.txt -q
python main.py &
BACKEND_PID=$!
echo "  Backend PID: $BACKEND_PID"

# Wait for backend
sleep 2

# Frontend
echo ""
echo "[2/2] Starting frontend..."
cd ../frontend
npm install --silent
npm run dev &
FE_PID=$!
echo "  Frontend PID: $FE_PID"

echo ""
echo "✅ Running!"
echo "   API:       http://localhost:8000"
echo "   API Docs:  http://localhost:8000/docs"
echo "   Dashboard: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop both servers."

trap "kill $BACKEND_PID $FE_PID 2>/dev/null; echo 'Stopped.'" EXIT
wait
