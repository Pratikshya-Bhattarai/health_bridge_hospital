interface MedicalOrganization {
  '@type': 'MedicalOrganization'
  name: string
  description: string
  url: string
  logo: string
  address: {
    '@type': 'PostalAddress'
    streetAddress: string
    addressLocality: string
    addressCountry: string
  }
  contactPoint: {
    '@type': 'ContactPoint'
    telephone: string
    contactType: string
    availableLanguage: string[]
  }
  medicalSpecialty: string[]
  hasOfferCatalog: {
    '@type': 'OfferCatalog'
    name: string
    itemListElement: Array<{
      '@type': 'Offer'
      itemOffered: {
        '@type': 'MedicalProcedure'
        name: string
      }
    }>
  }
}

interface LocalBusiness {
  '@type': 'LocalBusiness'
  '@id': string
  name: string
  description: string
  url: string
  telephone: string
  address: {
    '@type': 'PostalAddress'
    streetAddress: string
    addressLocality: string
    addressCountry: string
  }
  openingHours: string
  priceRange: string
  image: string
}

interface StructuredDataProps {
  type: 'organization' | 'localBusiness'
}

export function StructuredData({ type }: StructuredDataProps) {
  const organizationData: MedicalOrganization = {
    '@type': 'MedicalOrganization',
    name: 'HealthBridge Hospital',
    description: 'Leading multi-specialty hospital in Nepal, committed to delivering advanced healthcare with compassion.',
    url: 'https://healthbridge.com.np',
    logo: 'https://healthbridge.com.np/images/medical_team.jpg',
    address: {
      '@type': 'PostalAddress',
      streetAddress: 'Kalanki',
      addressLocality: 'Kathmandu',
      addressCountry: 'Nepal'
    },
    contactPoint: {
      '@type': 'ContactPoint',
      telephone: '+977-980-1234567',
      contactType: 'customer service',
      availableLanguage: ['English', 'Nepali']
    },
    medicalSpecialty: [
      'Cardiology',
      'Neurology',
      'Orthopedics',
      'Pediatrics',
      'Internal Medicine',
      'Emergency Medicine'
    ],
    hasOfferCatalog: {
      '@type': 'OfferCatalog',
      name: 'Medical Services',
      itemListElement: [
        {
          '@type': 'Offer',
          itemOffered: {
            '@type': 'MedicalProcedure',
            name: 'Emergency Care'
          }
        },
        {
          '@type': 'Offer',
          itemOffered: {
            '@type': 'MedicalProcedure',
            name: 'Cardiology Services'
          }
        }
      ]
    }
  }

  const localBusinessData: LocalBusiness = {
    '@type': 'LocalBusiness',
    '@id': 'https://healthbridge.com.np/#localbusiness',
    name: 'HealthBridge Hospital',
    description: 'Leading multi-specialty hospital in Nepal',
    url: 'https://healthbridge.com.np',
    telephone: '+977-980-1234567',
    address: {
      '@type': 'PostalAddress',
      streetAddress: 'Kalanki',
      addressLocality: 'Kathmandu',
      addressCountry: 'Nepal'
    },
    openingHours: 'Mo-Su 00:00-23:59',
    priceRange: '$$',
    image: 'https://healthbridge.com.np/images/medical_team.jpg'
  }

  const data = type === 'organization' ? organizationData : localBusinessData

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(data) }}
    />
  )
}