import { NextRequest, NextResponse } from 'next/server'

// Mock appointments data
let appointments = [
  {
    id: 1001,
    patient: {
      first_name: 'John',
      last_name: 'Doe',
      email: 'john.doe@example.com',
      phone: '+9779801234567'
    },
    doctor: {
      name: 'Dr. Suman Shrestha',
      specialization: 'Cardiology'
    },
    service: {
      name: 'Cardiology',
      description: 'Heart consultation'
    },
    appointment_date: '2024-01-15',
    appointment_time: '10:00 AM',
    status: 'confirmed',
    symptoms: 'Chest pain and shortness of breath',
    notes: 'Patient complains of chest pain',
    created_at: '2024-01-14T10:30:00.000Z'
  },
  {
    id: 1002,
    patient: {
      first_name: 'Sarah',
      last_name: 'Smith',
      email: 'sarah.smith@example.com',
      phone: '+9779807654321'
    },
    doctor: {
      name: 'Dr. Anjali Thapa',
      specialization: 'Neurology'
    },
    service: {
      name: 'Neurology',
      description: 'Brain consultation'
    },
    appointment_date: '2024-01-16',
    appointment_time: '02:00 PM',
    status: 'pending',
    symptoms: 'Headaches and dizziness',
    notes: 'Patient reports frequent headaches',
    created_at: '2024-01-14T11:15:00.000Z'
  },
  {
    id: 1003,
    patient: {
      first_name: 'Emergency',
      last_name: 'Patient',
      email: 'emergency@example.com',
      phone: '+9779801111111'
    },
    doctor: {
      name: 'Dr. Available Doctor',
      specialization: 'Emergency'
    },
    service: {
      name: 'Emergency',
      description: 'Emergency consultation'
    },
    appointment_date: '2024-01-14',
    appointment_time: '09:00 AM',
    status: 'completed',
    symptoms: 'Severe chest pain, difficulty breathing',
    notes: 'Emergency case - immediate attention required',
    created_at: '2024-01-14T08:45:00.000Z'
  }
]

export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url)
    const status = searchParams.get('status')
    const search = searchParams.get('search')

    let filteredAppointments = appointments

    // Filter by status
    if (status && status !== 'all') {
      filteredAppointments = filteredAppointments.filter(apt => apt.status === status)
    }

    // Filter by search term
    if (search) {
      filteredAppointments = filteredAppointments.filter(apt => 
        apt.patient.first_name.toLowerCase().includes(search.toLowerCase()) ||
        apt.patient.last_name.toLowerCase().includes(search.toLowerCase()) ||
        apt.patient.email.toLowerCase().includes(search.toLowerCase()) ||
        apt.doctor.name.toLowerCase().includes(search.toLowerCase())
      )
    }

    return NextResponse.json({
      success: true,
      data: filteredAppointments,
      total: filteredAppointments.length
    })

  } catch (error) {
    return NextResponse.json(
      { success: false, error: 'Failed to fetch appointments' },
      { status: 500 }
    )
  }
}

export async function PATCH(request: NextRequest) {
  try {
    const body = await request.json()
    const { id, status } = body

    if (!id || !status) {
      return NextResponse.json(
        { success: false, error: 'Appointment ID and status are required' },
        { status: 400 }
      )
    }

    // Find and update appointment
    const appointmentIndex = appointments.findIndex(apt => apt.id === id)
    
    if (appointmentIndex === -1) {
      return NextResponse.json(
        { success: false, error: 'Appointment not found' },
        { status: 404 }
      )
    }

    appointments[appointmentIndex].status = status

    return NextResponse.json({
      success: true,
      data: appointments[appointmentIndex],
      message: 'Appointment status updated successfully'
    })

  } catch (error) {
    return NextResponse.json(
      { success: false, error: 'Failed to update appointment' },
      { status: 500 }
    )
  }
}

export async function DELETE(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url)
    const id = searchParams.get('id')

    if (!id) {
      return NextResponse.json(
        { success: false, error: 'Appointment ID is required' },
        { status: 400 }
      )
    }

    const appointmentIndex = appointments.findIndex(apt => apt.id === parseInt(id))
    
    if (appointmentIndex === -1) {
      return NextResponse.json(
        { success: false, error: 'Appointment not found' },
        { status: 404 }
      )
    }

    appointments.splice(appointmentIndex, 1)

    return NextResponse.json({
      success: true,
      message: 'Appointment deleted successfully'
    })

  } catch (error) {
    return NextResponse.json(
      { success: false, error: 'Failed to delete appointment' },
      { status: 500 }
    )
  }
}
