'use client'

import { motion } from 'framer-motion'
import { Card, CardContent } from '@/components/ui/Card'
import { 
  Building2, 
  Shield, 
  Wifi, 
  Car, 
  Utensils, 
  Users,
  Clock,
  Heart
} from 'lucide-react'

const FacilitiesSection = () => {
  const facilities = [
    {
      icon: Building2,
      title: 'Modern Infrastructure',
      description: 'State-of-the-art building with advanced medical equipment and facilities.'
    },
    {
      icon: Shield,
      title: 'Safety & Security',
      description: '24/7 security and safety protocols to ensure patient and visitor safety.'
    },
    {
      icon: Wifi,
      title: 'Free WiFi',
      description: 'High-speed internet connectivity throughout the hospital premises.'
    },
    {
      icon: Car,
      title: 'Parking Facility',
      description: 'Ample parking space for patients and visitors with valet service.'
    },
    {
      icon: Utensils,
      title: 'Cafeteria',
      description: 'Healthy and hygienic food options for patients and visitors.'
    },
    {
      icon: Users,
      title: 'Waiting Areas',
      description: 'Comfortable and spacious waiting areas with entertainment options.'
    },
    {
      icon: Clock,
      title: '24/7 Services',
      description: 'Round-the-clock emergency and critical care services.'
    },
    {
      icon: Heart,
      title: 'Patient Care',
      description: 'Dedicated patient care coordinators for personalized assistance.'
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
            Our <span className="text-primary-600">Facilities</span>
          </h2>
          <p className="text-lg text-gray-600 max-w-3xl mx-auto leading-relaxed">
            We provide world-class facilities and amenities to ensure the comfort 
            and convenience of our patients and their families.
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {facilities.map((facility, index) => (
            <motion.div
              key={facility.title}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
            >
              <Card variant="elevated" className="p-6 text-center card-hover h-full">
                <CardContent className="space-y-4">
                  <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto">
                    <facility.icon className="w-8 h-8 text-primary-600" />
                  </div>
                  <h3 className="text-lg font-semibold text-gray-900">{facility.title}</h3>
                  <p className="text-gray-600 text-sm leading-relaxed">{facility.description}</p>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}

export default FacilitiesSection