'use client'

import { motion } from 'framer-motion'
import { Card, CardContent } from '@/components/ui/Card'
import Image from 'next/image'

const DoctorsSection = () => {
  const doctors = [
    {
      name: 'Dr. Suman Shrestha',
      specialty: 'MBBS, MD (Cardiology)',
      description: 'Specialist in angioplasty and bypass surgery with 15+ years of experience.',
      image: '/images/our_doctors.jpg',
      experience: '15+ Years'
    },
    {
      name: 'Dr. Anjali Thapa',
      specialty: 'MBBS, MS (Neurosurgery)',
      description: 'Expert in stroke care and brain surgeries, trained internationally.',
      image: '/images/our_doctors.jpg',
      experience: '12+ Years'
    },
    {
      name: 'Dr. Rajesh Gurung',
      specialty: 'MBBS, MD (Orthopedics)',
      description: 'Specialist in joint replacement and trauma care with advanced training.',
      image: '/images/our_doctors.jpg',
      experience: '18+ Years'
    },
    {
      name: 'Dr. Priya Lama',
      specialty: 'MBBS, MD (Pediatrics)',
      description: 'Expert in neonatal and child health care with compassionate approach.',
      image: '/images/our_doctors.jpg',
      experience: '10+ Years'
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
            Meet our team of highly qualified and experienced medical professionals, 
            dedicated to providing the best possible care for our patients.
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {doctors.map((doctor, index) => (
            <motion.div
              key={doctor.name}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
            >
              <Card variant="elevated" className="overflow-hidden card-hover">
                <div className="relative h-64 bg-gray-200">
                  <Image
                    src={doctor.image}
                    alt={doctor.name}
                    fill
                    className="object-cover"
                    sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 25vw"
                  />
                  <div className="absolute top-4 right-4 bg-primary-600 text-white px-2 py-1 rounded-full text-xs font-semibold">
                    {doctor.experience}
                  </div>
                </div>
                <CardContent className="p-6 text-center">
                  <h3 className="text-xl font-semibold text-gray-900 mb-2">{doctor.name}</h3>
                  <p className="text-primary-600 font-medium mb-3">{doctor.specialty}</p>
                  <p className="text-gray-600 text-sm leading-relaxed">{doctor.description}</p>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>

        {/* Team Stats */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.4 }}
          viewport={{ once: true }}
          className="mt-16"
        >
          <Card variant="elevated" className="p-8">
            <CardContent>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
                <div>
                  <div className="text-3xl font-bold text-primary-600 mb-2">50+</div>
                  <div className="text-gray-600">Expert Doctors</div>
                </div>
                <div>
                  <div className="text-3xl font-bold text-primary-600 mb-2">200+</div>
                  <div className="text-gray-600">Medical Staff</div>
                </div>
                <div>
                  <div className="text-3xl font-bold text-primary-600 mb-2">15+</div>
                  <div className="text-gray-600">Specialties</div>
                </div>
                <div>
                  <div className="text-3xl font-bold text-primary-600 mb-2">24/7</div>
                  <div className="text-gray-600">Emergency Care</div>
                </div>
              </div>
            </CardContent>
          </Card>
        </motion.div>
      </div>
    </section>
  )
}

export { DoctorsSection }
