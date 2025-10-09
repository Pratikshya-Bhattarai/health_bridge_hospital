import { NextRequest, NextResponse } from 'next/server'

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    
    // Validate required fields
    const requiredFields = ['firstName', 'lastName', 'email', 'phone', 'date', 'time', 'department']
    for (const field of requiredFields) {
      if (!body[field]) {
        return NextResponse.json(
          { success: false, error: `${field} is required` },
          { status: 400 }
        )
      }
    }

    // Simulate API processing delay
    await new Promise(resolve => setTimeout(resolve, 1000))

    // Generate appointment ID
    const appointmentId = Math.floor(Math.random() * 10000) + 1000

    // Create appointment response
    const appointment = {
      id: appointmentId,
      patient: {
        first_name: body.firstName,
        last_name: body.lastName,
        email: body.email,
        phone: body.phone,
      },
      doctor: {
        name: body.doctor || 'Dr. Available Doctor',
        specialization: body.department,
      },
      service: {
        name: body.department,
        description: `${body.department} consultation`,
      },
      appointment_date: body.date,
      appointment_time: body.time,
      status: 'pending',
      symptoms: body.message || '',
      notes: body.message || '',
      created_at: new Date().toISOString(),
    }

    return NextResponse.json({
      success: true,
      data: appointment,
      message: 'Appointment booked successfully!',
    })

  } catch (error) {
    return NextResponse.json(
      { success: false, error: 'Internal server error' },
      { status: 500 }
    )
  }
}

export async function GET() {
  return NextResponse.json({
    success: true,
    data: [],
    message: 'No appointments found',
  })
}
