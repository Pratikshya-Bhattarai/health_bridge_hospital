'use client'

import { useState, useEffect } from 'react'
import Link from 'next/link'
import { Button } from '@/components/ui/Button'
import { Menu, X, Phone, Mail } from 'lucide-react'

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false)
  const [isScrolled, setIsScrolled] = useState(false)

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50)
    }

    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const navItems = [
    { href: '#about', label: 'About' },
    { href: '#services', label: 'Services' },
    { href: '#doctors', label: 'Doctors' },
    { href: '#specialties', label: 'Specialties' },
    { href: '#facilities', label: 'Facilities' },
  ]

  return (
    <header className={`fixed top-0 w-full z-50 transition-all duration-300 ${
      isScrolled ? 'glass backdrop-blur-lg' : 'bg-transparent'
    }`}>
      <nav className="container-custom">
        <div className="flex justify-between items-center py-4">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-2 group">
            <div className="w-8 h-8 bg-white rounded-full flex items-center justify-center group-hover:scale-110 transition-transform">
              <div className="w-4 h-4 bg-primary-600 rounded-full"></div>
            </div>
            <span className="text-xl font-bold text-white">HealthBridge</span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-8">
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="text-white hover:text-primary-200 transition-colors duration-200 font-medium"
              >
                {item.label}
              </Link>
            ))}
            <Button variant="secondary" size="sm">
              Contact
            </Button>
          </div>

          {/* Mobile menu button */}
          <button
            className="md:hidden text-white p-2"
            onClick={() => setIsOpen(!isOpen)}
            aria-label="Toggle menu"
          >
            {isOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>

        {/* Mobile Navigation */}
        {isOpen && (
          <div className="md:hidden glass rounded-lg mt-2 p-4">
            <div className="flex flex-col space-y-4">
              {navItems.map((item) => (
                <Link
                  key={item.href}
                  href={item.href}
                  className="text-white hover:text-primary-200 transition-colors duration-200 font-medium"
                  onClick={() => setIsOpen(false)}
                >
                  {item.label}
                </Link>
              ))}
              <div className="flex flex-col space-y-2 pt-4 border-t border-white/20">
                <div className="flex items-center space-x-2 text-white text-sm">
                  <Phone size={16} />
                  <span>+977 980-1234567</span>
                </div>
                <div className="flex items-center space-x-2 text-white text-sm">
                  <Mail size={16} />
                  <span>info@healthbridge.com.np</span>
                </div>
              </div>
            </div>
          </div>
        )}
      </nav>
    </header>
  )
}

export { Navbar }
