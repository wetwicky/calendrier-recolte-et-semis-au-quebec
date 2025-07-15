# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-07-14

### 🎉 Initial Release - Complete Bilingual Quebec Planting & Harvest Calendar

#### ✨ Added
- **Complete French calendar** (`semis-et-recoltes.ics`) with 111 events
- **Complete English calendar** (`planting-and-harvest-quebec.ics`) with 111 events
- **17 planting events** with practical gardening tips for annual crops
- **78 harvest events** (39 start + 39 end dates) covering 39 fruit and vegetable varieties
- **16 exclusion events** explaining why certain crops are not suitable for Quebec's climate
- **Annual recurrence rules** (`RRULE:FREQ=YEARLY`) for automatic yearly repetition
- **Bilingual documentation** with complete installation instructions
- **Emoji categorization** for better visual identification (🌱🍅🍎🚫)

#### 🍎 Crops Included
**Fruits (13 varieties):**
- Strawberries, Raspberries, Blueberries, Blackberries
- Apples, Pears, Plums, Cherries, Ground Cherries
- Gooseberries, Blackcurrants, Rhubarb

**Vegetables (26 varieties):**
- Leafy greens: Lettuce, Spinach, Cabbage, Brussels Sprouts
- Root vegetables: Carrots, Beets, Turnips, Potatoes, Radishes
- Legumes: Green beans, Fava beans, Green peas
- Solanaceae: Tomatoes, Cherry tomatoes, Peppers, Eggplants
- Cucurbits: Zucchini, Cucumbers, Squash, Pumpkins
- Brassicas: Broccoli, Cauliflower
- Alliums: Onions, Garlic, Leeks
- Others: Corn, Asparagus

#### 🚫 Documented Exclusions
- **Citrus fruits** (oranges, lemons, grapefruits) - Too frost-sensitive
- **Tropical fruits** (avocados, figs, kiwis) - Climate too cold/short season
- **Heat-loving vegetables** (okra, artichokes) - Insufficient heat
- **Long-season crops** (watermelons, sweet potatoes) - Growing season too short
- **Complex cultivation** (fennel, endives, celeriac) - Difficult techniques

#### 🛠️ Automation Scripts
- `compare_calendars.py` - Quality assurance between French/English versions
- `count_stats.py` - Display detailed calendar statistics
- `verify_ics.py` - Validate and clean ICS files
- `clean_duplicates.py` - Remove duplicate events
- `add_rrule.py` - Manage recurrence rules
- `add_semis.py` - Add planting events with practical tips

#### 📱 Compatibility
- **Calendar Applications:** Google Calendar, Apple Calendar, Outlook, Thunderbird
- **Mobile Apps:** iOS Calendar, Android Calendar, Calendar apps
- **Standards:** Full ICS (iCalendar) RFC 5545 compliance
- **Platforms:** Windows, macOS, Linux, iOS, Android

#### 🌍 Localization
- **French Version:** Complete with Quebec French terminology
- **English Version:** Full translation with gardening terminology
- **Climate Zone:** Optimized for USDA/Canada zones 3a-5b
- **Region:** Southern Quebec, St. Lawrence Valley, Montreal, Quebec City

#### 📚 Documentation
- Bilingual README with installation instructions
- Complete crop lists with harvest periods
- Exclusion explanations with climate reasoning
- Usage examples for major calendar applications
- Contribution guidelines with conventional commits

### 🔧 Technical Details
- **Format:** ICS (iCalendar) version 2.0
- **Events:** 111 total events per language
- **Recurrence:** Annual repetition with RRULE
- **Categories:** FRUITS/VEGETABLES, PLANTING/HARVEST/EXCLUSION
- **Encoding:** UTF-8 with emoji support
- **File Size:** ~50KB per calendar file

### 🎯 Target Users
- Home gardeners in Quebec
- Community gardens and allotments
- Agricultural education programs
- Permaculture practitioners
- Urban farming initiatives
- Anyone interested in Quebec's growing seasons

---

## Upcoming Features (Roadmap)
- [ ] Herb and aromatic plant calendar
- [ ] Greenhouse/indoor growing schedules
- [ ] Regional variations (Northern Quebec, Gaspé)
- [ ] Companion planting suggestions
- [ ] Weather integration alerts
- [ ] Mobile app versions

---

**Download:** See [Releases](https://github.com/wetwicky/calendrier-recolte-et-semis-au-quebec/releases) for the latest version.
