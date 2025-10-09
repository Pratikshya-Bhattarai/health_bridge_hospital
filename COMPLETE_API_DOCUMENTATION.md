# 🏥 HealthBridge Hospital - Complete API Documentation

## 📋 **Overview**

This is the complete API documentation for HealthBridge Hospital's Django backend with Supabase integration. The API provides comprehensive functionality for appointment booking, user management, doctor profiles, and medical services.

## 🚀 **Quick Start**

### **Run Everything Automatically**
```bash
# Double-click this file to run both frontend and backend
RUN_EVERYTHING.bat
```

### **Manual Setup**
```bash
# Frontend
npm install
npm run dev

# Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python setup_django.py
python manage.py runserver
```

## 🌐 **API Base URL**
```
http://localhost:8000/api/v1/
```

## 🔐 **Authentication**

The API uses JWT (JSON Web Token) authentication. Include the access token in the Authorization header:

```
Authorization: Bearer your-access-token
```

## 📚 **API Endpoints**

### **1. Authentication Endpoints**

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
    "first_name": "John",
    "last_name": "Doe",
    "phone_number": "+9779801234567",
    "date_of_birth": "1990-01-01",
    "gender": "male",
    "address": "Kathmandu, Nepal",
    "emergency_contact": "+9779807654321",
    "emergency_contact_name": "Jane Doe"
}
```

**Response:**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user": {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "user_type": "patient",
        "full_name": "John Doe"
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
Authorization: Bearer your-access-token
```

#### **Update User Profile**
```http
PUT /api/v1/auth/profile/update/
Authorization: Bearer your-access-token
```

### **2. Appointment Booking Endpoints**

#### **Create Appointment**
```http
POST /api/v1/appointments/
Authorization: Bearer your-access-token
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
    "notes": "Patient prefers morning appointment",
    "special_requirements": "Wheelchair accessible"
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
Authorization: Bearer your-access-token
```

**Query Parameters:**
- `status`: Filter by status (pending, confirmed, completed, cancelled)
- `doctor`: Filter by doctor ID
- `service`: Filter by service ID
- `appointment_date`: Filter by date
- `urgency`: Filter by urgency level
- `search`: Search in symptoms, notes, doctor name, service name

#### **Get Appointment Details**
```http
GET /api/v1/appointments/{id}/
Authorization: Bearer your-access-token
```

#### **Update Appointment**
```http
PUT /api/v1/appointments/{id}/
Authorization: Bearer your-access-token
```

#### **Cancel Appointment**
```http
POST /api/v1/appointments/{id}/cancel/
Authorization: Bearer your-access-token
```

#### **Confirm Appointment**
```http
POST /api/v1/appointments/{id}/confirm/
Authorization: Bearer your-access-token
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
    ],
    "schedule": {
        "start_time": "09:00",
        "end_time": "17:00",
        "max_appointments": 10
    }
}
```

#### **Get Appointment Statistics**
```http
GET /api/v1/appointments/stats/
Authorization: Bearer your-access-token
```

**Response:**
```json
{
    "total_appointments": 25,
    "pending_appointments": 5,
    "confirmed_appointments": 15,
    "completed_appointments": 3,
    "cancelled_appointments": 2,
    "total_revenue": "37500.00",
    "average_rating": 4.2,
    "today_appointments": 3,
    "upcoming_appointments": 8
}
```

### **3. Doctor Endpoints**

#### **List Doctors**
```http
GET /api/v1/doctors/
```

**Query Parameters:**
- `specialty`: Filter by specialty
- `is_available`: Filter by availability
- `experience_years`: Filter by experience
- `search`: Search by name, specialty, qualification
- `ordering`: Order by name, experience_years, consultation_fee, average_rating

#### **Get Doctor Details**
```http
GET /api/v1/doctors/{id}/
```

#### **Get Doctor Availability**
```http
GET /api/v1/doctors/{doctor_id}/availability/{date}/
```

#### **Get Doctor Statistics**
```http
GET /api/v1/doctors/{doctor_id}/stats/
Authorization: Bearer your-access-token
```

#### **Search Doctors**
```http
GET /api/v1/doctors/search/
```

**Query Parameters:**
- `q`: Search query
- `specialty`: Filter by specialty
- `min_rating`: Minimum rating
- `max_fee`: Maximum consultation fee

#### **Get Featured Doctors**
```http
GET /api/v1/doctors/featured/
```

#### **Get Doctor Specialties**
```http
GET /api/v1/doctors/specialties/
```

### **4. Service Endpoints**

#### **List Services**
```http
GET /api/v1/services/
```

**Query Parameters:**
- `service_type`: Filter by service type
- `is_available`: Filter by availability
- `requires_appointment`: Filter by appointment requirement
- `search`: Search by name, description, tags
- `ordering`: Order by name, base_price, duration_minutes

#### **Get Service Details**
```http
GET /api/v1/services/{id}/
```

#### **Get Service Categories**
```http
GET /api/v1/services/categories/
```

#### **Get Service Packages**
```http
GET /api/v1/services/packages/
```

#### **Get Popular Services**
```http
GET /api/v1/services/popular/
```

#### **Search Services**
```http
GET /api/v1/services/search/
```

### **5. Patient Endpoints**

#### **Get Patient Profile**
```http
GET /api/v1/patients/profile/
Authorization: Bearer your-access-token
```

#### **Get Patient Dashboard**
```http
GET /api/v1/patients/dashboard/
Authorization: Bearer your-access-token
```

**Response:**
```json
{
    "patient": {
        "id": 1,
        "user_name": "John Doe",
        "blood_type": "O+",
        "allergies": "None",
        "medical_conditions": "None"
    },
    "recent_appointments": [
        {
            "id": 1,
            "doctor_name": "Dr. Suman Shrestha",
            "service_name": "Cardiology Consultation",
            "appointment_date": "2024-01-15",
            "appointment_time": "10:00:00",
            "status": "confirmed"
        }
    ],
    "medical_records_count": 5,
    "upcoming_appointments": 2
}
```

#### **Get Medical Records**
```http
GET /api/v1/patients/medical-records/
Authorization: Bearer your-access-token
```

#### **Get Medical Record Details**
```http
GET /api/v1/patients/medical-records/{id}/
Authorization: Bearer your-access-token
```

### **6. Notification Endpoints**

#### **Get Notifications**
```http
GET /api/v1/notifications/
Authorization: Bearer your-access-token
```

#### **Get Notification Details**
```http
GET /api/v1/notifications/{id}/
Authorization: Bearer your-access-token
```

#### **Mark All Notifications as Read**
```http
POST /api/v1/notifications/mark-all-read/
Authorization: Bearer your-access-token
```

#### **Get Unread Count**
```http
GET /api/v1/notifications/unread-count/
Authorization: Bearer your-access-token
```

## 🧪 **Testing the API**

### **Test Registration**
```bash
curl -X POST http://localhost:8000/api/v1/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "password_confirm": "testpass123",
    "user_type": "patient",
    "first_name": "Test",
    "last_name": "User"
  }'
```

### **Test Login**
```bash
curl -X POST http://localhost:8000/api/v1/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }'
```

### **Test Appointment Creation**
```bash
curl -X POST http://localhost:8000/api/v1/appointments/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-access-token" \
  -d '{
    "doctor": 1,
    "service": 1,
    "appointment_date": "2024-01-15",
    "appointment_time": "10:00:00",
    "symptoms": "Chest pain",
    "urgency": "urgent"
  }'
```

## 📊 **Database Models**

### **User Model**
- Custom user model with roles (Patient, Doctor, Admin, Staff)
- Profile information and medical details
- Authentication and authorization

### **Appointment Model**
- Complete appointment booking system
- Medical information and notes
- Status tracking and payment information
- Integration with doctors and services

### **Doctor Model**
- Doctor profiles with specialties
- Qualifications and experience
- Consultation fees and availability
- Ratings and reviews

### **Service Model**
- Medical services catalog
- Pricing and duration information
- Service categories and packages

### **Additional Models**
- Appointment reminders
- Feedback and ratings
- Documents and payments
- Notifications
- Medical records

## 🔒 **Security Features**

- JWT Authentication
- Role-based permissions
- Input validation
- SQL injection protection
- XSS protection
- CORS configuration
- Rate limiting (configurable)

## 📱 **Frontend Integration**

The API is designed to work seamlessly with the Next.js frontend:

```javascript
// Example: Create appointment from frontend
const createAppointment = async (appointmentData) => {
  const response = await fetch('http://localhost:8000/api/v1/appointments/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${accessToken}`
    },
    body: JSON.stringify(appointmentData)
  });
  
  return response.json();
};

// Example: Get available time slots
const getAvailableSlots = async (doctorId, date) => {
  const response = await fetch(`http://localhost:8000/api/v1/appointments/available-slots/${doctorId}/${date}/`);
  return response.json();
};

// Example: List appointments
const getAppointments = async (filters = {}) => {
  const queryParams = new URLSearchParams(filters);
  const response = await fetch(`http://localhost:8000/api/v1/appointments/?${queryParams}`, {
    headers: {
      'Authorization': `Bearer ${accessToken}`
    }
  });
  return response.json();
};
```

## 🎯 **Use Cases**

1. **Patient Registration & Login**
2. **Appointment Booking**
3. **Doctor Profile Management**
4. **Service Catalog Browsing**
5. **Appointment Management**
6. **Payment Processing**
7. **Feedback Collection**
8. **Admin Dashboard**

## 📞 **Support**

For API support or questions:
- **Email**: info@healthbridge.com.np
- **Phone**: +977 980-1234567
- **Documentation**: `http://localhost:8000/api/docs/`

## 🎉 **Success!**

Your complete HealthBridge Hospital system is now ready with:
- ✅ **Complete Django Backend** with Supabase integration
- ✅ **Comprehensive Booking API** with all features
- ✅ **JWT Authentication** for security
- ✅ **Complete Documentation** for easy integration
- ✅ **Production-ready** code with proper error handling
- ✅ **Automated Setup Scripts** for easy deployment

**Your HealthBridge Hospital system is ready to serve patients!** 🏥
