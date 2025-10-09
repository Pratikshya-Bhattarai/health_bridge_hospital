# 🏥 HealthBridge Hospital - Complete Setup Guide

## 🎯 **Project Overview**

This is a complete healthcare management system with:
- **Frontend**: Next.js 14+ with TypeScript and Tailwind CSS
- **Backend**: Django REST API with Supabase integration
- **Features**: Appointment booking, doctor management, patient records

## 🚀 **Quick Start (Automated)**

### **Option 1: Run Everything Automatically**
```bash
# Double-click this file to run everything
run-all.bat
```

This will:
- ✅ Check Node.js and Python installation
- ✅ Install all dependencies
- ✅ Set up both frontend and backend
- ✅ Start both servers automatically
- ✅ Open your website in browser

### **Option 2: Run Frontend Only**
```bash
# Double-click this file
run-frontend.bat
```

### **Option 3: Run Backend Only**
```bash
# Double-click this file
run-backend.bat
```

## 📋 **Manual Setup (Step by Step)**

### **Prerequisites**
1. **Node.js** (18+) - [Download here](https://nodejs.org/)
2. **Python** (3.8+) - [Download here](https://python.org/)
3. **Git** - [Download here](https://git-scm.com/)

### **Frontend Setup**
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Open http://localhost:3000
```

### **Backend Setup**
```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
copy env.example .env

# Setup Django
python setup_django.py

# Start server
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

# Database
DATABASE_URL=postgresql://postgres:password@localhost:5432/healthbridge
```

## 🌐 **Access Points**

### **Frontend (Next.js)**
- **Website**: http://localhost:3000
- **Features**: Responsive design, animations, SEO optimized

### **Backend (Django)**
- **API Base**: http://localhost:8000/api/v1/
- **Admin Panel**: http://localhost:8000/admin/
- **API Docs**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/

### **Default Login**
- **Username**: admin
- **Password**: admin123

## 📚 **API Endpoints**

### **Authentication**
- `POST /api/v1/auth/register/` - Register user
- `POST /api/v1/auth/login/` - Login user
- `GET /api/v1/auth/profile/` - Get user profile

### **Appointments**
- `GET /api/v1/appointments/` - List appointments
- `POST /api/v1/appointments/` - Create appointment
- `GET /api/v1/appointments/{id}/` - Get appointment details
- `PUT /api/v1/appointments/{id}/` - Update appointment
- `POST /api/v1/appointments/{id}/cancel/` - Cancel appointment
- `GET /api/v1/appointments/available-slots/{doctor_id}/{date}/` - Get available slots

### **Doctors**
- `GET /api/v1/doctors/` - List doctors
- `GET /api/v1/doctors/{id}/` - Get doctor details

### **Services**
- `GET /api/v1/services/` - List services
- `GET /api/v1/services/{id}/` - Get service details

## 🎨 **Frontend Features**

### **Pages & Sections**
- **Hero Section**: Hospital branding and call-to-action
- **About Section**: Mission, vision, and contact information
- **Services Section**: Medical specialties and services
- **Doctors Section**: Expert medical team profiles
- **Facilities Section**: Technology and equipment
- **Responsive Design**: Mobile, tablet, desktop optimized

### **Components**
- **Navbar**: Responsive navigation with mobile menu
- **Footer**: Contact information and links
- **Cards**: Reusable UI components
- **Buttons**: Consistent button styles
- **Animations**: Smooth Framer Motion animations

## 🔒 **Security Features**

### **Authentication**
- Token-based authentication
- User registration and login
- Role-based access control (Patient, Doctor, Admin, Staff)

### **Data Protection**
- Input validation
- SQL injection protection
- XSS protection
- CORS configuration

## 📊 **Database Models**

### **User Model**
- Custom user model with user types
- Patient, Doctor, Admin, Staff roles
- Contact information and emergency contacts

### **Appointment Model**
- Patient, Doctor, Service relationships
- Appointment scheduling and status tracking
- Medical information and notes
- Cost calculation

### **Doctor Model**
- Doctor profiles with specialties
- Qualifications and experience
- Consultation fees and availability

### **Service Model**
- Medical services catalog
- Pricing and duration information
- Active/inactive status

## 🚀 **Deployment**

### **Frontend (Vercel)**
1. Push code to GitHub
2. Connect repository to Vercel
3. Deploy with one click

### **Backend (Railway/Heroku)**
1. Set environment variables
2. Configure database
3. Deploy Django application

## 🧪 **Testing**

### **API Testing**
```bash
# Test registration
curl -X POST http://localhost:8000/api/v1/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "testpass123", "password_confirm": "testpass123", "user_type": "patient"}'

# Test appointment creation
curl -X POST http://localhost:8000/api/v1/appointments/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token your-token" \
  -d '{"doctor": 1, "service": 1, "appointment_date": "2024-01-15", "appointment_time": "10:00:00"}'
```

## 📞 **Support**

### **Contact Information**
- **Email**: info@healthbridge.com.np
- **Phone**: +977 980-1234567
- **Address**: Kalanki, Kathmandu, Nepal

### **Documentation**
- **API Docs**: http://localhost:8000/api/docs/
- **Frontend**: README.md
- **Backend**: API_DOCUMENTATION.md

## 🎉 **Success!**

Once everything is running, you'll have:
- ✅ **Modern Frontend**: Next.js website with beautiful UI
- ✅ **Powerful Backend**: Django API with comprehensive features
- ✅ **Database**: Supabase integration for data storage
- ✅ **Authentication**: Secure user management
- ✅ **Booking System**: Complete appointment management
- ✅ **Documentation**: Comprehensive API documentation

**Your HealthBridge Hospital system is ready to serve patients!** 🏥
