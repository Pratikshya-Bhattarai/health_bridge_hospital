// API configuration and services for HealthBridge Hospital

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api'

// Types
export interface AppointmentData {
  firstName: string
  lastName: string
  email: string
  phone: string
  date: string
  time: string
  department: string
  doctor?: string
  message?: string
}

export interface ApiResponse<T> {
  success: boolean
  data?: T
  error?: string
  message?: string
}

export interface Appointment {
  id: number
  patient: {
    first_name: string
    last_name: string
    email: string
    phone: string
  }
  doctor: {
    name: string
    specialization: string
  }
  service: {
    name: string
    description: string
  }
  appointment_date: string
  appointment_time: string
  status: string
  symptoms?: string
  notes?: string
  created_at: string
}

export interface Doctor {
  id: number
  name: string
  specialization: string
  experience: string
  rating: number
  image?: string
}

export interface Service {
  id: number
  name: string
  description: string
  price: number
  duration: number
}

export interface AvailableSlot {
  time: string
  available: boolean
}

// API Client
class ApiClient {
  private baseURL: string

  constructor(baseURL: string) {
    this.baseURL = baseURL
  }

  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<ApiResponse<T>> {
    try {
      const url = `${this.baseURL}${endpoint}`
      const response = await fetch(url, {
        headers: {
          'Content-Type': 'application/json',
          ...options.headers,
        },
        ...options,
      })

      const data = await response.json()

      if (!response.ok) {
        return {
          success: false,
          error: data.error || data.message || 'An error occurred',
        }
      }

      return {
        success: true,
        data,
      }
    } catch (error) {
      return {
        success: false,
        error: error instanceof Error ? error.message : 'Network error',
      }
    }
  }

  // Appointment methods
  async createAppointment(appointmentData: AppointmentData): Promise<ApiResponse<Appointment>> {
    return this.request<Appointment>('/appointments', {
      method: 'POST',
      body: JSON.stringify(appointmentData),
    })
  }

  async getAppointments(): Promise<ApiResponse<Appointment[]>> {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 500))
    
    return {
      success: true,
      data: [],
      message: 'No appointments found',
    }
  }

  async getDoctors(): Promise<ApiResponse<Doctor[]>> {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 500))
    
    const mockDoctors: Doctor[] = [
      {
        id: 1,
        name: 'Dr. Suman Shrestha',
        specialization: 'Cardiology',
        experience: '15+ years',
        rating: 4.9,
      },
      {
        id: 2,
        name: 'Dr. Anjali Thapa',
        specialization: 'Neurology',
        experience: '12+ years',
        rating: 4.8,
      },
      {
        id: 3,
        name: 'Dr. Rajesh Gurung',
        specialization: 'Orthopedics',
        experience: '18+ years',
        rating: 4.9,
      },
    ]

    return {
      success: true,
      data: mockDoctors,
    }
  }

  async getServices(): Promise<ApiResponse<Service[]>> {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 500))
    
    const mockServices: Service[] = [
      {
        id: 1,
        name: 'Cardiology',
        description: 'Heart and cardiovascular care',
        price: 1500,
        duration: 30,
      },
      {
        id: 2,
        name: 'Neurology',
        description: 'Brain and nervous system care',
        price: 1200,
        duration: 45,
      },
      {
        id: 3,
        name: 'Orthopedics',
        description: 'Bone and joint care',
        price: 1000,
        duration: 30,
      },
    ]

    return {
      success: true,
      data: mockServices,
    }
  }

  async getAvailableSlots(doctorId: number, date: string): Promise<ApiResponse<AvailableSlot[]>> {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 300))
    
    const timeSlots = [
      '09:00', '09:30', '10:00', '10:30', '11:00', '11:30',
      '12:00', '12:30', '14:00', '14:30', '15:00', '15:30',
      '16:00', '16:30', '17:00', '17:30'
    ]
    
    const availableSlots: AvailableSlot[] = timeSlots.map(time => ({
      time,
      available: Math.random() > 0.3, // 70% chance of being available
    }))

    return {
      success: true,
      data: availableSlots,
    }
  }

  async cancelAppointment(appointmentId: number): Promise<ApiResponse<void>> {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 500))
    
    return {
      success: true,
      message: 'Appointment cancelled successfully',
    }
  }
}

// Create API client instance
export const apiClient = new ApiClient(API_BASE_URL)

// Utility functions
export const formatDate = (date: string): string => {
  return new Date(date).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}

export const formatTime = (time: string): string => {
  const [hours, minutes] = time.split(':')
  const hour = parseInt(hours)
  const ampm = hour >= 12 ? 'PM' : 'AM'
  const displayHour = hour % 12 || 12
  return `${displayHour}:${minutes} ${ampm}`
}

export const getStatusColor = (status: string): string => {
  switch (status.toLowerCase()) {
    case 'pending':
      return 'text-yellow-600 bg-yellow-100'
    case 'confirmed':
      return 'text-blue-600 bg-blue-100'
    case 'completed':
      return 'text-green-600 bg-green-100'
    case 'cancelled':
      return 'text-red-600 bg-red-100'
    default:
      return 'text-gray-600 bg-gray-100'
  }
}
