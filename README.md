# Kilimo Hub-Ugandan Farmer Information Hub

A Django web application providing Ugandan farmers with accessible agricultural information
through web, mobile, SMS (*217#), and USSD channels.

## Features
- **Dashboard**-alerts, prices, weather at a glance
- **Crop Guidance**-planting calendars, AI chat advisor, variety info
- **Market Prices**-real-time prices from Kampala & regional markets
- **Disease Detection**-photo upload with AI diagnosis
- **Veterinary Advice**-AI vet chat + vaccination calendar
- **Weather**-7-day forecast with farming advisories
- **SMS/USSD**-*217# and SMS 8217 for non-smartphone access

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Environment Variables
Create a `.env` file in the project root or set these values in your deployment environment.
```
DEBUG=True
DJANGO_SECRET_KEY=your_secret_key
OPENWEATHER_API_KEY=your_openweather_api_key
SUNBIRD_API_URL=https://api.sunbird.ai/tasks/nllb_translate
SUNBIRD_API_KEY=your_sunbird_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```
Set the same variables in your Render service environment so the deployed site can fetch live weather and translations.

## App Structure
```
kilimo_hub/
├── core/          # Dashboard, alerts, farmer profiles
├── crops/         # Crop library, planting calendar, AI advisor
├── market/        # Market prices, commodities, price alerts
├── disease/       # Disease reports, photo diagnosis
├── veterinary/    # Vet chat, vaccine schedules
└── weather/       # Forecasts, planting advisories
```

## USSD Flow (*217#)
```
1. Market prices
   → Select crop → Select region → View prices
2. Weather
   → Enter district → View 3-day forecast
3. Crop advice
   → Select crop → Select topic → Read advice
4. Disease alert
   → Select district → View active alerts
5. Vet helpline
   → Connect to MAAIF vet (toll-free)
```

## SMS Commands (to 8217)
- `PRICE MAIZE`-Latest maize prices
- `WEATHER MUKONO`-Mukono weather
- `CROP MAIZE PLANT`-Maize planting guide
- `DISEASE MAIZE`-Maize disease alerts
- `VET COW FEVER`-Vet advice for cow with fever

## Languages Supported
- English (EN)
- Luganda (LG)
- Acholi (ACH)
- Runyankore (NY)
