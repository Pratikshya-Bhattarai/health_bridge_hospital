import { Navbar } from '@/components/layout/Navbar'
import { Footer } from '@/components/layout/Footer'
import { HeroSection } from '@/components/sections/HeroSection'
import { AboutSection } from '@/components/sections/AboutSection'
import { ServicesSection } from '@/components/sections/ServicesSection'
import { DoctorsSection } from '@/components/sections/DoctorsSection'
import { FacilitiesSection } from '@/components/sections/FacilitiesSection'

export default function HomePage() {
  return (
    <main className="min-h-screen">
      <Navbar />
      <HeroSection />
      <AboutSection />
      <ServicesSection />
      <DoctorsSection />
      <FacilitiesSection />
      <Footer />
    </main>
  )
}
