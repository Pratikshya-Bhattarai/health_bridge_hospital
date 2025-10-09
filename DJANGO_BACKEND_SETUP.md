# 🏥 HealthBridge Hospital - Django Backend Setup

## 📋 **Overview**

This is a comprehensive Django REST API backend for HealthBridge Hospital with Supabase integration, featuring a complete appointment booking system, user management, and medical records.

## 🚀 **Quick Start**

### **Automated Setup**
```bash
# Run the automated setup script
python setup_django.py
```

### **Manual Setup**
```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy environment file
copy env.example .env

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Start server
python manage.py runserver
```

## 🔧 **Configuration**

### **Environment Variables**
Create `.env` file in backend directory:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Supabase Configuration
SUPABASE_URL=https://afneskhznrmtouqgrbla.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFmbmVza2h6bnJtdG91cWdyYmxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk4NTIyOTIsImV4cCI6MjA3NTQyODI5Mn0.8ipDAk5FuyyiRG_OkyQTtFOisOdyy9vPhx1cLPGQzdw

# Database (Supabase PostgreSQL)
DATABASE_URL=postgresql://postgres:your-password@db.afneskhznrmtouqgrbla.supabase.co:5432/postgres

# JWT Settings
JWT_SECRET_KEY=your-jwt-secret-key
JWT_ACCESS_TOKEN_LIFETIME=60
JWT_REFRESH_TOKEN_LIFETIME=1440

# Email Configuration
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## 🌐 **API Endpoints**

### **Base URL**
```
http://localhost:8000/api/v1/
```

### **Authentication Endpoints**

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

### **Appointment Endpoints**

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
    ]
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
    "average_rating": 4.2
}
```

### **Doctor Endpoints**

#### **List Doctors**
```http
GET /api/v1/doctors/
```

#### **Get Doctor Details**
```http
GET /api/v1/doctors/{id}/
```

### **Service Endpoints**

#### **List Services**
```http
GET /api/v1/services/
```

#### **Get Service Details**
```http
GET /api/v1/services/{id}/
```

## 🔐 **Authentication**

The API uses JWT (JSON Web Token) authentication:

1. **Register/Login** to get access and refresh tokens
2. **Include the access token** in the Authorization header:
   ```
   Authorization: Bearer your-access-token
   ```
3. **Refresh tokens** when they expire using the refresh endpoint

## 📊 **Database Models**

### **User Model**
- Custom user model with user types (Patient, Doctor, Admin, Staff)
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

### **Service Model**
- Medical services catalog
- Pricing and duration information

### **Additional Models**
- Appointment reminders
- Feedback and ratings
- Documents and payments
- Notifications

## 🚀 **Features**

### **Core Features**
- ✅ **User Registration & Authentication** (JWT)
- ✅ **Appointment Booking System**
- ✅ **Doctor Management**
- ✅ **Service Catalog**
- ✅ **Patient Records**
- ✅ **Payment Tracking**
- ✅ **Appointment Reminders**
- ✅ **Feedback System**

### **Advanced Features**
- ✅ **Role-based Access Control**
- ✅ **File Upload Support**
- ✅ **Email Notifications**
- ✅ **API Documentation**
- ✅ **Data Validation**
- ✅ **Error Handling**
- ✅ **Pagination & Filtering**
- ✅ **Search Functionality**

## 📚 **API Documentation**

Interactive API documentation is available at:
- **Swagger UI**: `http://localhost:8000/api/docs/`
- **ReDoc**: `http://localhost:8000/api/redoc/`

## 🧪 **Testing**

### **Test the API**
```bash
# Test registration
curl -X POST http://localhost:8000/api/v1/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "testpass123", "password_confirm": "testpass123", "user_type": "patient"}'

# Test appointment creation
curl -X POST http://localhost:8000/api/v1/appointments/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"doctor": 1, "service": 1, "appointment_date": "2024-01-15", "appointment_time": "10:00:00"}'
```

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
// Example: Create appointment
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

Your Django backend is now ready with:
- ✅ **Complete API** for appointment booking
- ✅ **Supabase Integration** for database
- ✅ **JWT Authentication** for security
- ✅ **Comprehensive Documentation** for easy use
- ✅ **Production-ready** code with proper error handling

**Your HealthBridge Hospital backend is ready to serve patients!** 🏥
