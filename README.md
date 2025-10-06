# HealthBridge Hospital - Next.js Website

A modern, responsive healthcare website built with Next.js 14, TypeScript, and Tailwind CSS.

## 🚀 Features

- **Modern Tech Stack**: Next.js 14 with App Router, TypeScript, Tailwind CSS
- **Responsive Design**: Mobile-first approach with perfect responsiveness across all devices
- **Performance Optimized**: Lighthouse score ≥ 90, optimized images, lazy loading
- **SEO Ready**: Complete meta tags, sitemap, robots.txt, structured data
- **Accessibility**: WCAG compliant with semantic HTML and ARIA labels
- **Animations**: Smooth animations with Framer Motion
- **Component Library**: Reusable UI components with consistent design system

## 🛠️ Tech Stack

- **Framework**: Next.js 14+ with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Animations**: Framer Motion
- **Icons**: Lucide React
- **Deployment**: Vercel Ready

## 📁 Project Structure

```
├── app/                    # Next.js App Router
│   ├── globals.css        # Global styles
│   ├── layout.tsx         # Root layout with metadata
│   ├── page.tsx           # Home page
│   ├── not-found.tsx      # 404 page
│   ├── sitemap.ts         # Dynamic sitemap
│   └── robots.ts          # Robots.txt
├── components/            # Reusable components
│   ├── ui/               # Base UI components
│   ├── layout/           # Layout components
│   └── sections/         # Page sections
├── lib/                  # Utility functions
├── public/               # Static assets
│   └── images/          # Optimized images
└── styles/              # Additional styles
```

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd health-bridge-hospital
```

2. Install dependencies
```bash
npm install
# or
yarn install
```

3. Copy environment variables
```bash
cp env.example .env.local
```

4. Run the development server
```bash
npm run dev
# or
yarn dev
```

5. Open [http://localhost:3000](http://localhost:3000) in your browser

## 🏗️ Build & Deployment

### Build for Production
```bash
npm run build
npm start
```

### Deploy to Vercel
1. Push your code to GitHub
2. Connect your repository to Vercel
3. Deploy with one click

## 🎨 Customization

### Colors
Update the color palette in `tailwind.config.ts`:
```typescript
colors: {
  primary: {
    // Your primary colors
  },
  secondary: {
    // Your secondary colors
  }
}
```

### Content
- Update hospital information in components
- Replace images in `public/images/`
- Modify contact details in layout components

### SEO
- Update metadata in `app/layout.tsx`
- Modify sitemap in `app/sitemap.ts`
- Update robots.txt in `app/robots.ts`

## 📱 Responsive Design

The website is fully responsive with breakpoints:
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

## ♿ Accessibility

- Semantic HTML structure
- ARIA labels and roles
- Keyboard navigation support
- Screen reader compatibility
- High contrast ratios
- Focus indicators

## 🚀 Performance

- Optimized images with Next.js Image component
- Lazy loading for better performance
- Code splitting and bundle optimization
- Static generation for fast loading
- Lighthouse score ≥ 90

## 📞 Contact Information

- **Phone**: +977 980-1234567
- **Email**: info@healthbridge.com.np
- **Address**: Kalanki, Kathmandu, Nepal
- **Emergency**: 24/7 Available

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📞 Support

For support, email info@healthbridge.com.np or call +977 980-1234567.
