'use client'

import { motion } from 'framer-motion'
import { Card, CardContent } from '@/components/ui/Card'
import { Heart, Shield, Users, Award } from 'lucide-react'

const AboutSection = () => {
  const values = [
    {
      icon: Heart,
      title: 'Compassionate Care',
      description: 'We treat every patient with dignity, respect, and genuine care.'
    },
    {
      icon: Shield,
      title: 'Safety First',
      description: 'Your safety and well-being are our top priorities in all treatments.'
    },
    {
      icon: Users,
      title: 'Expert Team',
      description: 'Internationally trained doctors and healthcare professionals.'
    },
    {
      icon: Award,
      title: 'Excellence',
      description: 'Committed to delivering the highest quality healthcare services.'
    }
  ]

  return (
    <section id="about" className="section-padding bg-gray-50">
      <div className="container-custom">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold text-gray-900 mb-6">
            About <span className="text-primary-600">HealthBridge</span>
          </h2>
          <p className="text-lg text-gray-600 max-w-3xl mx-auto leading-relaxed">
            HealthBridge Hospital is a leading multi-specialty hospital in Nepal, committed to delivering 
            advanced healthcare with compassion. Our expert team, state-of-the-art technology, and 
            patient-centered care set us apart.
          </p>
        </motion.div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center mb-16">
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
          >
            <Card variant="elevated" className="p-8">
              <CardContent className="space-y-6">
                <div>
                  <h3 className="text-2xl font-bold text-gray-900 mb-4">Our Mission</h3>
                  <p className="text-gray-600 leading-relaxed">
                    To deliver safe, affordable, and holistic healthcare that enhances the quality of life 
                    for all our patients, while maintaining the highest standards of medical excellence.
                  </p>
                </div>
                <div>
                  <h3 className="text-2xl font-bold text-gray-900 mb-4">Our Vision</h3>
                  <p className="text-gray-600 leading-relaxed">
                    To be Nepal's most trusted hospital for excellence and patient satisfaction, 
                    recognized for our innovative approach to healthcare delivery.
                  </p>
                </div>
              </CardContent>
            </Card>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
            className="space-y-6"
          >
            <div className="bg-white p-6 rounded-xl shadow-lg">
              <h4 className="font-semibold text-gray-900 mb-2">Contact Information</h4>
              <div className="space-y-2 text-gray-600">
                <p><strong>Address:</strong> Kalanki, Kathmandu, Nepal</p>
                <p><strong>Phone:</strong> +977 980-1234567</p>
                <p><strong>Email:</strong> info@healthbridge.com.np</p>
                <p><strong>Emergency:</strong> 24/7 Available</p>
              </div>
            </div>
          </motion.div>
        </div>

        {/* Values Grid */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          viewport={{ once: true }}
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6"
        >
          {values.map((value, index) => (
            <motion.div
              key={value.title}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
            >
              <Card variant="elevated" className="text-center p-6 h-full card-hover">
                <CardContent className="space-y-4">
                  <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto">
                    <value.icon className="w-8 h-8 text-primary-600" />
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900">{value.title}</h3>
                  <p className="text-gray-600 text-sm leading-relaxed">{value.description}</p>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </section>
  )
}

export { AboutSection }
