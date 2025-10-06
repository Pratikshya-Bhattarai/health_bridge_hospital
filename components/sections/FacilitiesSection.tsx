'use client'

import { motion } from 'framer-motion'
import { Card, CardContent } from '@/components/ui/Card'
import Image from 'next/image'
import { 
  AlertTriangle, 
  Wrench, 
  Microscope, 
  Bed, 
  Pill, 
  Smartphone,
  Shield,
  Clock,
  Users,
  Award
} from 'lucide-react'

const FacilitiesSection = () => {
  const facilities = [
    {
      icon: AlertTriangle,
      title: 'Emergency Care',
      description: '24/7 urgent medical response with dedicated emergency team.',
      color: 'text-red-600'
    },
    {
      icon: Wrench,
      title: 'Operation Theatres',
      description: 'Advanced surgical facilities with modern equipment.',
      color: 'text-blue-600'
    },
    {
      icon: Microscope,
      title: 'Diagnostics',
      description: 'MRI, CT, ultrasound, and comprehensive lab services.',
      color: 'text-green-600'
    },
    {
      icon: Bed,
      title: 'Intensive Care',
      description: 'ICU, CCU, NICU, and PICU with specialized monitoring.',
      color: 'text-purple-600'
    },
    {
      icon: Pill,
      title: 'Pharmacy',
      description: 'In-house medication and physiotherapy services.',
      color: 'text-orange-600'
    },
    {
      icon: Smartphone,
      title: 'Telemedicine',
      description: 'Convenient online consultations and remote monitoring.',
      color: 'text-indigo-600'
    }
  ]

  const whyChooseUs = [
    {
      icon: Shield,
      title: 'Internationally Trained Team',
      description: 'Our medical professionals are trained at leading institutions worldwide.'
    },
    {
      icon: Users,
      title: 'Patient-First Care',
      description: 'We prioritize patient dignity and comfort in all our services.'
    },
    {
      icon: Award,
      title: 'Affordable Healthcare',
      description: 'Quality healthcare packages that are accessible to all.'
    },
    {
      icon: Clock,
      title: 'Innovative Services',
      description: 'Continuously improving and adopting latest medical technologies.'
    }
  ]

  return (
    <section id="facilities" className="section-padding">
      <div className="container-custom">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold text-gray-900 mb-6">
            Facilities & <span className="text-primary-600">Technology</span>
          </h2>
          <p className="text-lg text-gray-600 max-w-3xl mx-auto leading-relaxed">
            State-of-the-art facilities and cutting-edge technology to provide 
            the best possible healthcare experience for our patients.
          </p>
        </motion.div>

        {/* Facilities Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
          {facilities.map((facility, index) => (
            <motion.div
              key={facility.title}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
            >
              <Card variant="elevated" className="p-6 h-full card-hover group">
                <CardContent className="space-y-4">
                  <div className="w-12 h-12 bg-gray-100 rounded-lg flex items-center justify-center group-hover:bg-primary-100 transition-colors">
                    <facility.icon className={`w-6 h-6 ${facility.color}`} />
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900">{facility.title}</h3>
                  <p className="text-gray-600 leading-relaxed">{facility.description}</p>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>

        {/* Why Choose Us */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-12"
        >
          <h3 className="text-2xl md:text-3xl font-bold text-gray-900 mb-8">
            Why Choose <span className="text-primary-600">HealthBridge?</span>
          </h3>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-16">
          {whyChooseUs.map((item, index) => (
            <motion.div
              key={item.title}
              initial={{ opacity: 0, x: index % 2 === 0 ? -30 : 30 }}
              whileInView={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
            >
              <Card variant="elevated" className="p-6">
                <CardContent className="flex items-start space-x-4">
                  <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <item.icon className="w-6 h-6 text-primary-600" />
                  </div>
                  <div>
                    <h4 className="text-lg font-semibold text-gray-900 mb-2">{item.title}</h4>
                    <p className="text-gray-600 leading-relaxed">{item.description}</p>
                  </div>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>

        {/* Team & Patient Care Images */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="grid grid-cols-1 md:grid-cols-2 gap-8"
        >
          <Card variant="elevated" className="overflow-hidden">
            <div className="relative h-64">
              <Image
                src="/images/Doctor_and_nurses_team.jpg"
                alt="Emergency Team"
                fill
                className="object-cover"
                sizes="(max-width: 768px) 100vw, 50vw"
              />
            </div>
            <CardContent className="p-6 text-center">
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Emergency Team</h3>
              <p className="text-gray-600">Highly skilled doctors and nurses, available 24/7 for critical care.</p>
            </CardContent>
          </Card>

          <Card variant="elevated" className="overflow-hidden">
            <div className="relative h-64">
              <Image
                src="/images/room.jpg"
                alt="Patient Care"
                fill
                className="object-cover"
                sizes="(max-width: 768px) 100vw, 50vw"
              />
            </div>
            <CardContent className="p-6 text-center">
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Patient Care</h3>
              <p className="text-gray-600">Comfortable rooms and compassionate consultations for all patients.</p>
            </CardContent>
          </Card>
        </motion.div>
      </div>
    </section>
  )
}

export { FacilitiesSection }
