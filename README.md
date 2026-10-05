# 🏠 StayNest - Verified Student Housing & Brokerage-Free Rentals

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://staynest.streamlit.app)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **India's Most Trusted Accommodation Platform for Students & Working Professionals**

StayNest is a revolutionary accommodation platform that connects students with verified PG accommodations and individuals with brokerage-free flats. We build trust by partnering with universities and verifying every property before publication.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Modules](#modules)
- [Database](#database)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

---

## ✨ Features

### 🎯 Core Features
- ✅ **Verified Properties** - Every property is verified by StayNest team
- ✅ **Zero Brokerage** - No hidden charges, completely transparent pricing
- ✅ **University Partnerships** - Official partnerships with educational institutions
- ✅ **Advanced Search** - Filter by location, budget, amenities, and more
- ✅ **AI Recommendations** - Smart recommendations based on preferences
- ✅ **Secure Booking** - Safe and transparent booking system

### 👨‍🎓 Student Module
- Student registration and profile management
- Browse and search properties
- Save favorite properties to wishlist
- Book property visits
- Leave ratings and reviews
- Receive personalized recommendations
- Notifications for new listings

### 🏢 Owner Module
- Property listing management
- Upload multiple images
- Manage bookings and inquiries
- Analytics dashboard
- Response tracking

### 🎓 University Module
- University registration as official partner
- Verified partner badge
- View nearby properties
- Student statistics dashboard
- Exclusive partnership features

### 🔐 Admin Module
- Property verification system
- User management
- University management
- Analytics and reports
- System configuration

### 🔍 Advanced Search
- Filter by city and location
- University proximity search
- Budget range selection
- Amenity filters (WiFi, AC, Parking, Laundry, etc.)
- Gender-based filtering
- Distance-based search
- Verified property filter
- Sort by ratings, distance, price

### 📊 Analytics
- Interactive dashboards
- Booking analytics
- Property statistics
- Monthly registrations
- City-wise listings
- University-wise distribution
- Revenue tracking (future-ready)

---

## 🛠️ Tech Stack

### Backend & Frontend
- **Streamlit 1.36.0** - UI Framework
- **Python 3.9+** - Programming Language
- **SQLite** - Database

### Data & Analytics
- **Pandas** - Data manipulation
- **Plotly** - Interactive visualizations
- **Matplotlib & Seaborn** - Statistical visualizations

### Security
- **bcrypt** - Password hashing
- **PyJWT** - Authentication tokens
- **Cryptography** - Data encryption

### Additional Libraries
- **Pillow** - Image processing
- **OpenCV** - Advanced image operations
- **scikit-learn** - AI/ML recommendations
- **Faker** - Sample data generation
- **geopy** - Geolocation services

---

## 📦 Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Git

### Clone the Repository
```bash
git clone https://github.com/yourusername/staynest.git
cd staynest
```

### Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Quick Start

### Run the Application Locally
```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

### Initialize Database
The database is automatically initialized on first run. Sample data can be populated using:
```bash
python sample_data/generate_sample_data.py
```

---

## 📁 Project Structure

```
staynest/
├── app.py                          # Main application entry point
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── .gitignore                      # Git ignore rules
│
├── .streamlit/
│   └── config.toml                # Streamlit configuration
│
├── database/
│   ├── __init__.py
│   ├── db.py                      # Database connection & initialization
│   ├── schema.py                  # Database schema definition
│   └── crud.py                    # CRUD operations
│
├── authentication/
│   ├── __init__.py
│   ├── auth.py                    # Authentication logic
│   ├── session.py                 # Session management
│   └── password.py                # Password utilities
│
├── components/
│   ├── __init__.py
│   ├── navbar.py                  # Navigation bar
│   ├── cards.py                   # Reusable card components
│   ├── footer.py                  # Footer component
│   ├── sidebar.py                 # Sidebar component
│   └── modals.py                  # Modal dialogs
│
├── utils/
│   ├── __init__.py
│   ├── helpers.py                 # Helper functions
│   ├── validators.py              # Input validation
│   ├── constants.py               # Application constants
│   └── logger.py                  # Logging utility
│
├── pages/
│   ├── __init__.py
│   ├── home.py                    # Landing/home page
│   ├── about.py                   # About page
│   ├── contact.py                 # Contact page
│   └── search.py                  # Search page
│
├── student/
│   ├── __init__.py
│   ├── dashboard.py               # Student dashboard
│   ├── profile.py                 # Student profile management
│   ├── wishlist.py                # Wishlist management
│   ├── bookings.py                # Booking management
│   └── recommendations.py         # Recommendation engine
│
├── owner/
│   ├── __init__.py
│   ├── dashboard.py               # Owner dashboard
│   ├── properties.py              # Property management
│   ├── listings.py                # Listing creation/editing
│   ├── analytics.py               # Analytics for owners
│   └── bookings.py                # Booking management
│
├── university/
│   ├── __init__.py
│   ├── dashboard.py               # University dashboard
│   ├── partner.py                 # Partner verification
│   ├── analytics.py               # University analytics
│   └── properties.py              # Nearby properties
│
├── admin/
│   ├── __init__.py
│   ├── dashboard.py               # Admin dashboard
│   ├── verification.py            # Property verification
│   ├── user_management.py         # User management
│   ├── reports.py                 # Reports and analytics
│   └── settings.py                # System settings
│
├── css/
│   ├── style.css                  # Custom styling
│   ├── components.css             # Component styles
│   └── animations.css             # Animation styles
│
├── assets/
│   ├── icons/                     # Icon files
│   ├── logos/                     # Logo files
│   └── fonts/                     # Font files
│
├── images/
│   ├── properties/                # Property images
│   ├── universities/              # University logos
│   └── banners/                   # Banner images
│
└── sample_data/
    ├── generate_sample_data.py    # Sample data generation
    ├── users.py                   # Sample users
    ├── properties.py              # Sample properties
    └── universities.py            # Sample universities
```

---

## 💻 Usage

### For Students
1. Register as a student with your email and university
2. Browse properties using advanced search filters
3. Save favorite properties to your wishlist
4. Book property visits
5. Leave ratings and reviews
6. Receive personalized recommendations

### For Property Owners
1. Register as a property owner
2. Add property details and upload images
3. Manage your listings
4. View booking requests
5. Track analytics

### For Universities
1. Register your university
2. Get verified partner badge
3. View nearby properties
4. Access student statistics

### For Administrators
1. Login to admin panel
2. Verify and approve properties
3. Manage users and universities
4. View analytics and reports
5. Configure system settings

---

## 🗄️ Database

StayNest uses **SQLite** for data persistence with the following tables:

- **users** - User accounts and profiles
- **students** - Student-specific information
- **owners** - Property owner details
- **universities** - University partners
- **properties** - Property listings
- **bookings** - Booking records
- **wishlist** - Student wishlists
- **reviews** - Property reviews and ratings
- **messages** - User messages
- **notifications** - System notifications
- **admin** - Admin users

All database operations include:
- ✅ Validation
- ✅ Error handling
- ✅ Transaction management
- ✅ Performance optimization

---

## 🌐 Deployment

### Deploy on Streamlit Community Cloud

#### Step 1: Push to GitHub
```bash
git add .
git commit -m "Initial commit - StayNest application"
git push origin main
```

#### Step 2: Create Streamlit Account
- Go to [Streamlit Community Cloud](https://streamlit.io/cloud)
- Sign in with your GitHub account

#### Step 3: Deploy
- Click "New app"
- Select your repository
- Choose the main branch
- Set main file path to `app.py`
- Click "Deploy"

#### Step 4: Configure Secrets (if needed)
- Go to your app settings
- Add any sensitive data in the Secrets section

### Environment Variables
Create a `.env` file for local development (not committed to Git):
```
DATABASE_PATH=data/staynest.db
SECRET_KEY=your-secret-key
JWT_SECRET=your-jwt-secret
DEBUG=True
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Setting Up Development Environment
```bash
# Clone the repository
git clone https://github.com/yourusername/staynest.git
cd staynest

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies with dev tools
pip install -r requirements.txt

# Install pre-commit hooks (optional)
pre-commit install
```

### Making Changes
1. Create a new branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Run tests: `pytest`
4. Format code: `black .`
5. Lint: `flake8 .`
6. Commit: `git commit -am 'Add new feature'`
7. Push: `git push origin feature/your-feature`
8. Open a Pull Request

### Code Standards
- Follow PEP 8 guidelines
- Write meaningful variable names
- Add docstrings to functions
- Handle errors gracefully
- Write unit tests

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

## 📞 Support

### Get Help
- 📧 Email: support@staynest.com
- 💬 GitHub Issues: [Report a bug](https://github.com/yourusername/staynest/issues)
- 📖 Documentation: [Wiki](https://github.com/yourusername/staynest/wiki)

### FAQ
**Q: Is StayNest free to use?**
A: Yes, StayNest is completely free for students to search and book properties. Owners get free listings.

**Q: How do you verify properties?**
A: Every property is manually verified by our team before publication. We visit properties and check documentation.

**Q: Can I list my property?**
A: Yes! Register as an owner and follow our listing process. Your property will be verified within 24-48 hours.

**Q: How do bookings work?**
A: Students can book property visits directly through the platform. Owners will receive notifications and can confirm visits.

---

## 🚀 Roadmap

- [ ] Mobile application (iOS & Android)
- [ ] Advanced AI recommendations
- [ ] Video tours
- [ ] Virtual property visits
- [ ] Online payment integration
- [ ] Legal document management
- [ ] Roommate matching
- [ ] Property comparison tool
- [ ] Multilingual support
- [ ] Enterprise solutions

---

## 👥 Team

**StayNest** is built with ❤️ by a dedicated team of developers and designers.

---

## 🙏 Acknowledgments

- Streamlit team for the amazing framework
- All contributors and supporters
- University partners
- Property owners and students

---

**Made with ❤️ for Students | Verified Properties | Zero Brokerage**

© 2026 StayNest. All rights reserved.
