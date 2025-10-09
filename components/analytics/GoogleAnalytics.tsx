'use client'

import Script from 'next/script'

interface GoogleAnalyticsProps {
  gaId?: string
}

export function GoogleAnalytics({ gaId }: GoogleAnalyticsProps) {
  // Use environment variable if no gaId is provided
  const trackingId = gaId || process.env.NEXT_PUBLIC_GA_ID

  // Don't render if no tracking ID is available
  if (!trackingId) {
    return null
  }

  return (
    <>
      <Script
        src={`https://www.googletagmanager.com/gtag/js?id=${trackingId}`}
        strategy="afterInteractive"
      />
      <Script id="google-analytics" strategy="afterInteractive">
        {`
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', '${trackingId}', {
            page_title: document.title,
            page_location: window.location.href
          });
        `}
      </Script>
    </>
  )
}

// Default export for easier importing
export default function GoogleAnalyticsDefault() {
  return <GoogleAnalytics />
}
