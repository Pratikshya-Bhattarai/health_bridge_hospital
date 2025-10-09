'use client'

import { motion } from 'framer-motion'
import { Card, CardContent } from '@/components/ui/Card'
import { Star, Award, Users } from 'lucide-react'

const DoctorsSection = () => {
  const doctors = [
    {
      name: 'Dr. Suman Shrestha',
      specialty: 'Cardiologist',
      experience: '15+ years',
      rating: 4.9,
      image: '/images/our_doctors.jpg'
    },
    {
      name: 'Dr. Anjali Thapa',
      specialty: 'Neurologist',
      experience: '12+ years',
      rating: 4.8,
      image: '/images/our_doctors.jpg'
    },
    {
      name: 'Dr. Rajesh Gurung',
      specialty: 'Orthopedist',
      experience: '18+ years',
      rating: 4.9,
      image: '/images/our_doctors.jpg'
    }
  ]

  return (
    <section id="doctors" className="section-padding bg-gray-50">
      <div className="container-custom">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold text-gray-900 mb-6">
            Our <span className="text-primary-600">Expert Doctors</span>
          </h2>
          <p className="text-lg text-gray-600 max-w-3xl mx-auto leading-relaxed">
            Meet our team of highly qualified and experienced medical professionals 
            dedicated to providing exceptional healthcare services.
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {doctors.map((doctor, index) => (
            <motion.div
              key={doctor.name}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
            >
              <Card variant="elevated" className="p-6 text-center card-hover">
                <CardContent className="space-y-4">
                  <div className="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4 overflow-hidden">
                    <img 
                      src={doctor.image} 
                      alt={doctor.name}
                      className="w-full h-full object-cover"
                    />
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900">{doctor.name}</h3>
                  <p className="text-primary-600 font-medium">{doctor.specialty}</p>
                  <p className="text-gray-600 text-sm">{doctor.experience} experience</p>
                  <div className="flex items-center justify-center space-x-1">
                    <Star className="w-4 h-4 text-yellow-400 fill-current" />
                    <span className="text-sm font-medium">{doctor.rating}</span>
                  </div>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}

export default DoctorsSection