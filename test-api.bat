@echo off
echo ========================================
echo    HealthBridge Hospital API Testing
echo ========================================
echo.

echo [1/4] Testing Frontend API (Simulated)
echo.
echo Testing appointment booking API...
echo.

echo POST /api/appointments
curl -X POST "http://localhost:3001/api/appointments" ^
  -H "Content-Type: application/json" ^
  -d "{\"firstName\":\"John\",\"lastName\":\"Doe\",\"email\":\"john.doe@example.com\",\"phone\":\"+9779801234567\",\"date\":\"2024-01-15\",\"time\":\"10:00 AM\",\"department\":\"Cardiology\",\"doctor\":\"Dr. Suman Shrestha\",\"message\":\"Chest pain and shortness of breath\"}"

echo.
echo.
echo [2/4] Testing Django Backend API (if running)
echo.
echo Testing Django backend on port 8000...
echo.

echo GET /api/doctors/
curl -X GET "http://localhost:8000/api/doctors/" -H "Content-Type: application/json"

echo.
echo.
echo GET /api/services/
curl -X GET "http://localhost:8000/api/services/" -H "Content-Type: application/json"

echo.
echo.
echo [3/4] Testing Available Slots
echo.
echo GET /api/appointments/available-slots/1/2024-01-15/
curl -X GET "http://localhost:8000/api/appointments/available-slots/1/2024-01-15/" -H "Content-Type: application/json"

echo.
echo.
echo [4/4] Testing Appointment Creation (Django)
echo.
echo POST /api/appointments/
curl -X POST "http://localhost:8000/api/appointments/" ^
  -H "Content-Type: application/json" ^
  -d "{\"patient\":1,\"doctor\":1,\"service\":1,\"appointment_date\":\"2024-01-15\",\"appointment_time\":\"10:00:00\",\"symptoms\":\"Chest pain\",\"notes\":\"Patient complains of chest pain\"}"

echo.
echo.
echo ========================================
echo    API Testing Complete
echo ========================================
echo.
echo Note: Django backend needs to be running on port 8000
echo Frontend API is simulated and working on port 3001
echo.
pause
