import { MetadataRoute } from 'next'

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: 'HealthBridge Hospital - Premier Healthcare in Nepal',
    short_name: 'HealthBridge',
    description: 'Leading multi-specialty hospital in Nepal with expert medical team and state-of-the-art technology.',
    start_url: '/',
    display: 'standalone',
    background_color: '#ffffff',
    theme_color: '#059669',
    icons: [
      {
        src: '/images/medical_team.jpg',
        sizes: 'any',
        type: 'image/jpeg',
      },
    ],
  }
}
