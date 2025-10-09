'use client'

import { useState } from 'react'
import { apiClient, type AppointmentData } from '@/lib/api'

export default function TestApiPage() {
  const [result, setResult] = useState<any>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const testBooking = async () => {
    setLoading(true)
    setError(null)
    
    try {
      const appointmentData: AppointmentData = {
        firstName: 'John',
        lastName: 'Doe',
        email: 'john.doe@example.com',
        phone: '+9779801234567',
        date: '2024-01-15',
        time: '10:00 AM',
        department: 'Cardiology',
        doctor: 'Dr. Suman Shrestha',
        message: 'Chest pain and shortness of breath'
      }

      const response = await apiClient.createAppointment(appointmentData)
      setResult(response)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  const testGetAppointments = async () => {
    setLoading(true)
    setError(null)
    
    try {
      const response = await apiClient.getAppointments()
      setResult(response)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  const testGetDoctors = async () => {
    setLoading(true)
    setError(null)
    
    try {
      const response = await apiClient.getDoctors()
      setResult(response)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container mx-auto px-4">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-3xl font-bold text-gray-900 mb-8">API Testing Dashboard</h1>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
            <button
              onClick={testBooking}
              disabled={loading}
              className="bg-green-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-green-700 transition-colors disabled:opacity-50"
            >
              {loading ? 'Testing...' : 'Test Booking API'}
            </button>
            
            <button
              onClick={testGetAppointments}
              disabled={loading}
              className="bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition-colors disabled:opacity-50"
            >
              {loading ? 'Testing...' : 'Test Get Appointments'}
            </button>
            
            <button
              onClick={testGetDoctors}
              disabled={loading}
              className="bg-purple-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-purple-700 transition-colors disabled:opacity-50"
            >
              {loading ? 'Testing...' : 'Test Get Doctors'}
            </button>
          </div>

          {error && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
              <h3 className="font-semibold text-red-800 mb-2">Error:</h3>
              <p className="text-red-600">{error}</p>
            </div>
          )}

          {result && (
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h3 className="text-lg font-semibold text-gray-900 mb-4">API Response:</h3>
              <pre className="bg-gray-100 rounded-lg p-4 overflow-auto text-sm">
                {JSON.stringify(result, null, 2)}
              </pre>
            </div>
          )}

          <div className="mt-8 bg-blue-50 rounded-lg p-6">
            <h3 className="text-lg font-semibold text-blue-900 mb-4">Available API Endpoints:</h3>
            <div className="space-y-2 text-sm">
              <div className="flex items-center space-x-2">
                <span className="bg-green-100 text-green-800 px-2 py-1 rounded text-xs font-mono">POST</span>
                <span className="font-mono">/api/appointments</span>
                <span className="text-gray-600">- Create new appointment</span>
              </div>
              <div className="flex items-center space-x-2">
                <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded text-xs font-mono">GET</span>
                <span className="font-mono">/api/appointments</span>
                <span className="text-gray-600">- Get all appointments</span>
              </div>
              <div className="flex items-center space-x-2">
                <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded text-xs font-mono">GET</span>
                <span className="font-mono">/api/doctors</span>
                <span className="text-gray-600">- Get all doctors</span>
              </div>
              <div className="flex items-center space-x-2">
                <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded text-xs font-mono">GET</span>
                <span className="font-mono">/api/services</span>
                <span className="text-gray-600">- Get all services</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
