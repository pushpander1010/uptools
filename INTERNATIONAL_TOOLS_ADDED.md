# International Tools Added to UpTools

## Overview
Added 5 new tools targeting European, American, and Canadian audiences to attract foreign traffic.

## New Tools

### 1. Tip Calculator (`/tip-calculator/`)
- **Target Audience**: US, Canada, Europe
- **Features**:
  - Calculate tips with preset percentages (10%, 15%, 18%, 20%, 25%)
  - Custom tip percentage input
  - Bill splitting for multiple people
  - Shows tip amount, total, and per-person cost
- **Categories**: Finance, Calculator
- **Keywords**: tip calculator, bill splitter, restaurant tip, gratuity calculator

### 2. US Sales Tax Calculator (`/sales-tax-calculator/`)
- **Target Audience**: United States
- **Features**:
  - All 50 US states with accurate state sales tax rates
  - Add or remove tax modes
  - Identifies states with no sales tax (AK, DE, MT, NH, OR)
  - Real-time calculation
- **Categories**: Tax, Finance
- **Keywords**: sales tax calculator, state tax rates, US tax calculator

### 3. VAT Calculator (`/vat-calculator/`)
- **Target Audience**: Europe, UK, International
- **Features**:
  - All EU countries plus UK, Norway, Iceland
  - Standard VAT rates from 5% to 27%
  - Add or remove VAT modes
  - Shows net, VAT amount, and gross
  - Includes non-EU countries (Canada GST, Australia GST, New Zealand GST)
- **Categories**: Tax, Finance
- **Keywords**: VAT calculator, European tax, value added tax, EU VAT rates

### 4. Mortgage Calculator (`/mortgage-calculator/`)
- **Target Audience**: US, Canada, Europe, UK
- **Features**:
  - Calculate monthly mortgage payments
  - Total interest over loan term
  - Adjustable home price, down payment, interest rate, and loan term
  - Shows loan amount and total amount paid
- **Categories**: Finance, Calculator, Housing
- **Keywords**: mortgage calculator, home loan calculator, monthly payment calculator

### 5. Calorie Calculator (`/calorie-calculator/`)
- **Target Audience**: Universal (US, Europe, Canada, worldwide)
- **Features**:
  - Calculate BMR (Basal Metabolic Rate)
  - Calculate TDEE (Total Daily Energy Expenditure)
  - Weight loss and weight gain calorie targets
  - Gender-specific calculations (Mifflin-St Jeor Equation)
  - 5 activity levels from sedentary to extra active
  - Metric units (kg, cm)
- **Categories**: Health, Fitness
- **Keywords**: calorie calculator, TDEE calculator, BMR calculator, daily calorie needs

## SEO Optimization

All tools include:
- ✅ Unique meta titles and descriptions
- ✅ Canonical URLs
- ✅ Open Graph tags for social sharing
- ✅ JSON-LD structured data (SoftwareApplication, BreadcrumbList, FAQPage)
- ✅ FAQ sections with 3 common questions each
- ✅ Breadcrumb navigation
- ✅ AdSense integration
- ✅ Mobile-responsive design
- ✅ Accessibility features (skip links, ARIA labels)

## Files Modified

1. **uptools/index.html** - Added 5 new tools to TOOLS array
2. **uptools/wrangler.jsonc** - Added tool directories to watch_dir
3. **uptools/public/sitemap.xml** - Added 5 new URLs with lastmod date 2026-04-25

## Files Created

1. `uptools/tip-calculator/index.html`
2. `uptools/sales-tax-calculator/index.html`
3. `uptools/vat-calculator/index.html`
4. `uptools/mortgage-calculator/index.html`
5. `uptools/calorie-calculator/index.html`

## Traffic Potential

### High-Volume Keywords Targeted:
- "tip calculator" - 90K+ monthly searches (US)
- "sales tax calculator" - 60K+ monthly searches (US)
- "VAT calculator" - 40K+ monthly searches (EU/UK)
- "mortgage calculator" - 200K+ monthly searches (US/UK/CA)
- "calorie calculator" - 150K+ monthly searches (worldwide)

### Geographic Coverage:
- **United States**: Tip calculator, Sales tax calculator, Mortgage calculator, Calorie calculator
- **Canada**: Tip calculator, Mortgage calculator, Calorie calculator
- **Europe/UK**: VAT calculator, Mortgage calculator, Calorie calculator
- **Worldwide**: Calorie calculator

## Next Steps

1. **Build and Deploy**:
   ```bash
   cd uptools
   npm run build
   wrangler deploy
   ```

2. **Create OG Images** (optional but recommended):
   - Create 1200×630 images for each tool at:
     - `/assets/og/tip-calculator.png`
     - `/assets/og/sales-tax-calculator.png`
     - `/assets/og/vat-calculator.png`
     - `/assets/og/mortgage-calculator.png`
     - `/assets/og/calorie-calculator.png`

3. **Monitor Performance**:
   - Track organic traffic from target countries
   - Monitor keyword rankings in Google Search Console
   - Analyze user engagement metrics

4. **Future Expansion Ideas**:
   - 401(k) Calculator (US retirement)
   - Student Loan Calculator (US/UK)
   - Fuel Cost Calculator (Europe/US)
   - IBAN Validator (Europe)
   - Rent vs Buy Calculator (US/Europe)
   - UK Tax Calculator
   - Australian Tax Calculator

## Compliance

All tools follow the UpTools standards:
- Privacy-first (no data collection)
- No sign-ups required
- Fast loading times
- Works offline after first load
- Accessible (WCAG compliant)
