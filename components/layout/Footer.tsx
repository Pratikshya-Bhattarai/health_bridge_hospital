import Link from 'next/link'
import { Phone, Mail, MapPin, Clock, Facebook, Twitter, Instagram, Linkedin } from 'lucide-react'

const Footer = () => {
  const currentYear = new Date().getFullYear()

  const quickLinks = [
    { href: '#about', label: 'About Us' },
    { href: '#services', label: 'Services' },
    { href: '#doctors', label: 'Our Doctors' },
    { href: '#specialties', label: 'Specialties' },
    { href: '#facilities', label: 'Facilities' },
  ]

  const services = [
    'Emergency Care',
    'Cardiology',
    'Neurology',
    'Orthopedics',
    'Maternity Care',
    'Pediatrics',
  ]

  return (
    <footer className="gradient-bg text-white">
      <div className="container-custom section-padding">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {/* Hospital Info */}
          <div className="space-y-4">
            <div className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-white rounded-full flex items-center justify-center">
                <div className="w-4 h-4 bg-primary-600 rounded-full"></div>
              </div>
              <span className="text-xl font-bold">HealthBridge</span>
            </div>
            <p className="text-white/90 text-sm leading-relaxed">
              Leading multi-specialty hospital in Nepal, committed to delivering advanced healthcare with compassion and excellence.
            </p>
            <div className="flex space-x-4">
              <a href="#" className="text-white/80 hover:text-white transition-colors" aria-label="Facebook">
                <Facebook size={20} />
              </a>
              <a href="#" className="text-white/80 hover:text-white transition-colors" aria-label="Twitter">
                <Twitter size={20} />
              </a>
              <a href="#" className="text-white/80 hover:text-white transition-colors" aria-label="Instagram">
                <Instagram size={20} />
              </a>
              <a href="#" className="text-white/80 hover:text-white transition-colors" aria-label="LinkedIn">
                <Linkedin size={20} />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Quick Links</h3>
            <ul className="space-y-2">
              {quickLinks.map((link) => (
                <li key={link.href}>
                  <Link
                    href={link.href}
                    className="text-white/80 hover:text-white transition-colors text-sm"
                  >
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Services */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Our Services</h3>
            <ul className="space-y-2">
              {services.map((service) => (
                <li key={service}>
                  <span className="text-white/80 text-sm">{service}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact Info */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Contact Info</h3>
            <div className="space-y-3">
              <div className="flex items-start space-x-3">
                <MapPin size={16} className="mt-1 text-white/80" />
                <span className="text-white/80 text-sm">
                  Kalanki, Kathmandu, Nepal
                </span>
              </div>
              <div className="flex items-center space-x-3">
                <Phone size={16} className="text-white/80" />
                <a
                  href="tel:+9779801234567"
                  className="text-white/80 hover:text-white transition-colors text-sm"
                >
                  +977 980-1234567
                </a>
              </div>
              <div className="flex items-center space-x-3">
                <Mail size={16} className="text-white/80" />
                <a
                  href="mailto:info@healthbridge.com.np"
                  className="text-white/80 hover:text-white transition-colors text-sm"
                >
                  info@healthbridge.com.np
                </a>
              </div>
              <div className="flex items-start space-x-3">
                <Clock size={16} className="mt-1 text-white/80" />
                <div className="text-white/80 text-sm">
                  <div>24/7 Emergency</div>
                  <div>Mon-Sat: 8AM-6PM</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="border-t border-white/20 mt-12 pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
            <p className="text-white/80 text-sm">
              © {currentYear} HealthBridge Hospital. All rights reserved.
            </p>
            <div className="flex space-x-6 text-sm">
              <Link href="/privacy" className="text-white/80 hover:text-white transition-colors">
                Privacy Policy
              </Link>
              <Link href="/terms" className="text-white/80 hover:text-white transition-colors">
                Terms of Service
              </Link>
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
}

export default Footer
