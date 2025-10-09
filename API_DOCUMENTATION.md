# 🏥 HealthBridge Hospital API Documentation

## 📋 **Overview**

The HealthBridge Hospital API provides comprehensive endpoints for managing appointments, doctors, patients, and services. Built with Django REST Framework and integrated with Supabase.

## 🔗 **Base URL**
```
http://localhost:8000/api/v1/
```

## 🔐 **Authentication**

The API uses Token-based authentication. Include the token in the Authorization header:

```
Authorization: Token your-token-here
```

## 📚 **API Endpoints**

### 🔑 **Authentication Endpoints**

#### **Register User**
```http
POST /api/v1/auth/register/
```

**Request Body:**
```json
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "password_confirm": "securepassword123",
    "user_type": "patient",
    "phone_number": "+9779801234567",
    "date_of_birth": "1990-01-01",
    "address": "Kathmandu, Nepal",
    "emergency_contact": "+9779807654321"
}
```

**Response:**
```json
{
    "token": "your-auth-token",
    "user": {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "user_type": "patient",
        "phone_number": "+9779801234567"
    },
    "message": "User registered successfully"
}
```

#### **Login User**
```http
POST /api/v1/auth/login/
```

**Request Body:**
```json
{
    "username": "john_doe",
    "password": "securepassword123"
}
```

#### **Get User Profile**
```http
GET /api/v1/auth/profile/
Authorization: Token your-token-here
```

#### **Update User Profile**
```http
PUT /api/v1/auth/profile/update/
Authorization: Token your-token-here
```

### 👨‍⚕️ **Doctors Endpoints**

#### **List All Doctors**
```http
GET /api/v1/doctors/
```

**Response:**
```json
[
    {
        "id": 1,
        "name": "Dr. Suman Shrestha",
        "specialty": "cardiology",
        "qualification": "MBBS, MD (Cardiology)",
        "experience_years": 15,
        "consultation_fee": "1500.00",
        "bio": "Expert in cardiology with 15+ years experience",
        "is_available": true
    }
]
```

#### **Get Doctor Details**
```http
GET /api/v1/doctors/{id}/
```

### 🩺 **Services Endpoints**

#### **List All Services**
```http
GET /api/v1/services/
```

**Response:**
```json
[
    {
        "id": 1,
        "name": "General Consultation",
        "description": "General health checkup and consultation",
        "base_price": "1000.00",
        "duration_minutes": 30,
        "is_active": true
    }
]
```

#### **Get Service Details**
```http
GET /api/v1/services/{id}/
```

### 📅 **Appointments Endpoints**

#### **Create Appointment**
```http
POST /api/v1/appointments/
Authorization: Token your-token-here
```

**Request Body:**
```json
{
    "doctor": 1,
    "service": 1,
    "appointment_date": "2024-01-15",
    "appointment_time": "10:00:00",
    "symptoms": "Chest pain and shortness of breath",
    "medical_history": "No significant medical history",
    "current_medications": "None",
    "allergies": "None known",
    "urgency": "urgent",
    "notes": "Patient prefers morning appointment"
}
```

**Response:**
```json
{
    "id": 1,
    "patient": 1,
    "doctor": 1,
    "service": 1,
    "appointment_date": "2024-01-15",
    "appointment_time": "10:00:00",
    "status": "pending",
    "urgency": "urgent",
    "consultation_fee": "1500.00",
    "total_cost": "1500.00",
    "created_at": "2024-01-10T10:30:00Z"
}
```

#### **List Appointments**
```http
GET /api/v1/appointments/
Authorization: Token your-token-here
```

**Query Parameters:**
- `status`: Filter by status (pending, confirmed, completed, cancelled)
- `doctor`: Filter by doctor ID
- `service`: Filter by service ID
- `appointment_date`: Filter by date
- `search`: Search in symptoms, notes, doctor name, service name

#### **Get Appointment Details**
```http
GET /api/v1/appointments/{id}/
Authorization: Token your-token-here
```

#### **Update Appointment**
```http
PUT /api/v1/appointments/{id}/
Authorization: Token your-token-here
```

#### **Cancel Appointment**
```http
POST /api/v1/appointments/{id}/cancel/
Authorization: Token your-token-here
```

#### **Confirm Appointment**
```http
POST /api/v1/appointments/{id}/confirm/
Authorization: Token your-token-here
```

#### **Get Available Time Slots**
```http
GET /api/v1/appointments/available-slots/{doctor_id}/{date}/
```

**Response:**
```json
{
    "doctor": "Dr. Suman Shrestha",
    "date": "2024-01-15",
    "available_slots": [
        "09:00",
        "09:30",
        "10:30",
        "11:00",
        "11:30"
    ]
}
```

#### **Get Appointment Statistics**
```http
GET /api/v1/appointments/stats/
Authorization: Token your-token-here
```

**Response:**
```json
{
    "total_appointments": 25,
    "pending_appointments": 5,
    "confirmed_appointments": 15,
    "completed_appointments": 3,
    "cancelled_appointments": 2,
    "total_revenue": "37500.00"
}
```

### 👥 **Patients Endpoints**

#### **List Patients** (Admin/Staff only)
```http
GET /api/v1/patients/
Authorization: Token your-token-here
```

#### **Get Patient Details**
```http
GET /api/v1/patients/{id}/
Authorization: Token your-token-here
```

## 🔧 **Error Handling**

The API returns standard HTTP status codes:

- `200 OK` - Request successful
- `201 Created` - Resource created successfully
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Permission denied
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

**Error Response Format:**
```json
{
    "error": "Error message",
    "details": "Additional error details"
}
```

## 📊 **API Documentation**

Interactive API documentation is available at:
- **Swagger UI**: `http://localhost:8000/api/docs/`
- **ReDoc**: `http://localhost:8000/api/redoc/`

## 🚀 **Getting Started**

1. **Start the backend server:**
   ```bash
   cd backend
   python manage.py runserver
   ```

2. **Access the API:**
   - Base URL: `http://localhost:8000/api/v1/`
   - Documentation: `http://localhost:8000/api/docs/`

3. **Test the API:**
   ```bash
   # Register a user
   curl -X POST http://localhost:8000/api/v1/auth/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "email": "test@example.com", "password": "testpass123", "password_confirm": "testpass123", "user_type": "patient"}'
   ```

## 🔒 **Security Features**

- Token-based authentication
- CORS protection
- Input validation
- SQL injection protection
- XSS protection
- Rate limiting (configurable)

## 📱 **Frontend Integration**

The API is designed to work seamlessly with the Next.js frontend:

```javascript
// Example: Create appointment
const createAppointment = async (appointmentData) => {
  const response = await fetch('http://localhost:8000/api/v1/appointments/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Token ${userToken}`
    },
    body: JSON.stringify(appointmentData)
  });
  
  return response.json();
};
```

## 🎯 **Use Cases**

1. **Patient Registration & Login**
2. **Doctor Profile Management**
3. **Service Catalog**
4. **Appointment Booking**
5. **Appointment Management**
6. **Time Slot Availability**
7. **Appointment Statistics**
8. **User Profile Management**

## 📞 **Support**

For API support or questions:
- **Email**: info@healthbridge.com.np
- **Phone**: +977 980-1234567
- **Documentation**: `http://localhost:8000/api/docs/`
