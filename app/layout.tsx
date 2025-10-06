import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { StructuredData } from '@/components/seo/StructuredData'

const inter = Inter({ 
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
})

export const metadata: Metadata = {
  title: {
    default: 'HealthBridge Hospital - Premier Healthcare in Nepal',
    template: '%s | HealthBridge Hospital'
  },
  description: 'HealthBridge Hospital is a leading multi-specialty hospital in Nepal, committed to delivering advanced healthcare with compassion. Expert team, state-of-the-art technology, and patient-centered care.',
  keywords: [
    'hospital Nepal',
    'healthcare Kathmandu',
    'medical services Nepal',
    'emergency care',
    'cardiology',
    'neurology',
    'orthopedics',
    'maternity care',
    'pediatrics',
    'HealthBridge Hospital'
  ],
  authors: [{ name: 'HealthBridge Hospital' }],
  creator: 'HealthBridge Hospital',
  publisher: 'HealthBridge Hospital',
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  metadataBase: new URL('https://healthbridge.com.np'),
  alternates: {
    canonical: '/',
  },
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: 'https://healthbridge.com.np',
    title: 'HealthBridge Hospital - Premier Healthcare in Nepal',
    description: 'Leading multi-specialty hospital in Nepal with expert medical team and state-of-the-art technology.',
    siteName: 'HealthBridge Hospital',
    images: [
      {
        url: '/images/medical_team.jpg',
        width: 1200,
        height: 630,
        alt: 'HealthBridge Hospital Medical Team',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'HealthBridge Hospital - Premier Healthcare in Nepal',
    description: 'Leading multi-specialty hospital in Nepal with expert medical team and state-of-the-art technology.',
    images: ['/images/medical_team.jpg'],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  verification: {
    google: 'your-google-verification-code',
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={inter.variable}>
      <head>
        <StructuredData type="organization" />
        <StructuredData type="localBusiness" />
      </head>
      <body className={`${inter.className} antialiased`}>
        {children}
      </body>
    </html>
  )
}
