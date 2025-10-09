export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-green-600 to-blue-600">
      {/* Header */}
      <header className="bg-white/20 backdrop-blur-lg border-b border-white/30">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-white rounded-full flex items-center justify-center">
                <div className="w-4 h-4 bg-green-600 rounded-full"></div>
              </div>
              <span className="text-xl font-bold text-white">HealthBridge</span>
            </div>
            <nav className="hidden md:flex space-x-6">
              <a href="#about" className="text-white hover:text-green-200 transition-colors">About</a>
              <a href="#services" className="text-white hover:text-green-200 transition-colors">Services</a>
              <a href="#doctors" className="text-white hover:text-green-200 transition-colors">Doctors</a>
              <a href="#contact" className="text-white hover:text-green-200 transition-colors">Contact</a>
              <a href="/admin/login" className="text-white hover:text-green-200 transition-colors bg-white/20 px-3 py-1 rounded-lg">Admin</a>
            </nav>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <main className="flex-1 flex items-center justify-center py-20">
        <div className="text-center text-white max-w-4xl mx-auto px-4">
          <h1 className="text-4xl md:text-6xl font-bold mb-6">
            Bridging Care & Compassion
          </h1>
          <p className="text-lg md:text-xl mb-8 text-white/90">
            Premier healthcare services in Nepal with expertise, empathy, and state-of-the-art technology.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a 
              href="/appointment"
              className="bg-white text-green-600 px-8 py-3 rounded-full font-semibold hover:bg-gray-100 transition-colors text-center"
            >
              Book Appointment
            </a>
            <button className="border-2 border-white text-white px-8 py-3 rounded-full font-semibold hover:bg-white hover:text-green-600 transition-colors">
              Emergency: +977 980-1234567
            </button>
          </div>
        </div>
      </main>

      {/* Stats */}
      <section className="bg-white/10 backdrop-blur-lg py-16">
        <div className="container mx-auto px-4">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center text-white">
            <div>
              <div className="text-3xl font-bold">500+</div>
              <div className="text-sm">Patients Daily</div>
            </div>
            <div>
              <div className="text-3xl font-bold">50+</div>
              <div className="text-sm">Expert Doctors</div>
            </div>
            <div>
              <div className="text-3xl font-bold">24/7</div>
              <div className="text-sm">Emergency Care</div>
            </div>
            <div>
              <div className="text-3xl font-bold">15+</div>
              <div className="text-sm">Specialties</div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-black/20 py-8">
        <div className="container mx-auto px-4 text-center text-white">
          <p>&copy; 2024 HealthBridge Hospital. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}
