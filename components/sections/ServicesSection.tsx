'use client'

import { motion } from 'framer-motion'
import { Card, CardContent } from '@/components/ui/Card'
import { 
  Stethoscope, 
  Microscope, 
  Baby, 
  Scissors, 
  UserCheck, 
  Heart,
  Brain,
  Bone,
  Pill,
  Tooth
} from 'lucide-react'

const ServicesSection = () => {
  const services = [
    {
      icon: Stethoscope,
      title: '24/7 Emergency Care',
      description: 'Immediate, round-the-clock critical care with rapid response teams.',
      color: 'text-red-600'
    },
    {
      icon: Microscope,
      title: 'Advanced Diagnostics',
      description: 'State-of-the-art imaging, lab services, and comprehensive health screenings.',
      color: 'text-blue-600'
    },
    {
      icon: Baby,
      title: 'Maternity & Child Health',
      description: 'Comprehensive care for mothers and children with specialized NICU facilities.',
      color: 'text-pink-600'
    },
    {
      icon: Scissors,
      title: 'Surgical Units',
      description: 'Advanced surgical and critical care facilities with modern operation theaters.',
      color: 'text-purple-600'
    },
    {
      icon: UserCheck,
      title: 'Outpatient Clinics',
      description: 'Specialized consultations and follow-up care for all medical needs.',
      color: 'text-green-600'
    },
    {
      icon: Heart,
      title: 'Cardiology',
      description: 'Complete heart care including angioplasty, bypass surgery, and valve replacement.',
      color: 'text-red-500'
    }
  ]

  const specialties = [
    { icon: Heart, name: 'Cardiology', description: 'Heart & vascular care' },
    { icon: Brain, name: 'Neurology', description: 'Brain & nervous system' },
    { icon: Bone, name: 'Orthopedics', description: 'Bones & joints' },
    { icon: Baby, name: 'Pediatrics', description: 'Child healthcare' },
    { icon: Pill, name: 'Internal Medicine', description: 'General health' },
    { icon: Tooth, name: 'Dental Care', description: 'Oral health' }
  ]

  return (
    <section id="services" className="section-padding">
      <div className="container-custom">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold text-gray-900 mb-6">
            Our <span className="text-primary-600">Services</span>
          </h2>
          <p className="text-lg text-gray-600 max-w-3xl mx-auto leading-relaxed">
            Comprehensive healthcare services designed to meet all your medical needs with 
            cutting-edge technology and compassionate care.
          </p>
        </motion.div>

        {/* Main Services */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
          {services.map((service, index) => (
            <motion.div
              key={service.title}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
            >
              <Card variant="elevated" className="p-6 h-full card-hover group">
                <CardContent className="space-y-4">
                  <div className="w-12 h-12 bg-gray-100 rounded-lg flex items-center justify-center group-hover:bg-primary-100 transition-colors">
                    <service.icon className={`w-6 h-6 ${service.color}`} />
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900">{service.title}</h3>
                  <p className="text-gray-600 leading-relaxed">{service.description}</p>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>

        {/* Specialties */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-12"
        >
          <h3 className="text-2xl md:text-3xl font-bold text-gray-900 mb-8">
            Medical <span className="text-primary-600">Specialties</span>
          </h3>
        </motion.div>

        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
          {specialties.map((specialty, index) => (
            <motion.div
              key={specialty.name}
              initial={{ opacity: 0, scale: 0.9 }}
              whileInView={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              viewport={{ once: true }}
            >
              <Card variant="elevated" className="p-4 text-center card-hover">
                <CardContent className="space-y-3">
                  <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mx-auto">
                    <specialty.icon className="w-6 h-6 text-primary-600" />
                  </div>
                  <div>
                    <h4 className="font-semibold text-gray-900 text-sm">{specialty.name}</h4>
                    <p className="text-xs text-gray-600">{specialty.description}</p>
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

export default ServicesSection
