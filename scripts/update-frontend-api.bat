@echo off
REM HealthBridge Hospital - Update Frontend API Configuration
REM This script updates the frontend to use the PythonAnywhere backend

echo 🚀 Updating Frontend API Configuration
echo ======================================

REM Check if we're in the right directory
if not exist "lib\api.ts" (
    echo [ERROR] Please run this script from the project root directory
    pause
    exit /b 1
)

echo [INFO] Updating API configuration for PythonAnywhere...

REM Update lib/api.ts
echo [INFO] Updating lib/api.ts...
(
echo // HealthBridge Hospital API Configuration
echo // Updated for PythonAnywhere deployment
echo.
echo const API_BASE_URL = process.env.NODE_ENV === 'production' 
echo   ? 'https://bepratikshya.pythonanywhere.com/api'
echo   : 'http://localhost:8000/api'
echo.
echo export { API_BASE_URL }
echo.
echo // API Endpoints
echo export const API_ENDPOINTS = {
echo   APPOINTMENTS: `${API_BASE_URL}/appointments/`,
echo   DOCTORS: `${API_BASE_URL}/doctors/`,
echo   PATIENTS: `${API_BASE_URL}/patients/`,
echo   SERVICES: `${API_BASE_URL}/services/`,
echo   AUTH: `${API_BASE_URL}/auth/`,
echo   ADMIN: `${API_BASE_URL}/admin/`,
echo } as const
echo.
echo // API Helper Functions
echo export const apiRequest = async (endpoint: string, options: RequestInit = {}) => {
echo   const url = `${API_BASE_URL}${endpoint}`
echo   const response = await fetch(url, {
echo     headers: {
echo       'Content-Type': 'application/json',
echo       ...options.headers,
echo     },
echo     ...options,
echo   })
echo.
echo   if (!response.ok) {
echo     throw new Error(`API request failed: ${response.status} ${response.statusText}`)
echo   }
echo.
echo   return response.json()
echo }
) > lib\api.ts

echo [INFO] ✅ API configuration updated successfully!
echo.
echo [INFO] 📋 Updated configuration:
echo   - Production API: https://bepratikshya.pythonanywhere.com/api
echo   - Development API: http://localhost:8000/api
echo.
echo [INFO] 🔄 Next steps:
echo   1. Test your frontend locally
echo   2. Deploy to Vercel
echo   3. Verify API connections
echo.
echo [INFO] 🎉 Frontend is now configured for PythonAnywhere backend!

pause
