# Florida Business Search Project

A web application that allows users to search and retrieve business information from the Florida Secretary of State website. The project consists of a Python/Flask backend with Playwright for web scraping, a Supabase database for storage, and a React frontend for the user interface.

## Features

- Search Florida businesses by name
- Real-time web scraping of business details
- Storage of search results in Supabase database
- Responsive React frontend with tabular display
- RESTful API endpoints for search and data retrieval

## Tech Stack

- **Backend**: Python, Flask, Playwright
- **Frontend**: React.js
- **Database**: Supabase
- **API**: RESTful endpoints

## Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn
- Supabase account

## Project Structure

```
react-app/                      # Root directory
│
├── react-app/                  # Frontend subdirectory
│   ├── public/                 # Public assets
│   ├── src/                    # Source files
│   │   ├── components/         # React components
│   │   │   ├── SearchBar.js   # Search input component
│   │   │   └── ResultsTable.js # Results display component
│   │   ├── App.js             # Main App component
│   │   ├── App.css            # App styles
│   │   ├── index.js           # Entry point
│   │   └── index.css          # Global styles
│   ├── .gitignore             # Git ignore file
│   ├── package.json           # Dependencies and scripts
│   └── package-lock.json      # Lock file
│
└── backend/                    # Backend subdirectory
    ├── main.py                # Flask application entry point
    ├── crawler.py             # Playwright web scraper
    ├── config.py              # Configuration settings
    ├── database.py            # Database operations
    ├── requirements.txt       # Python dependencies
    └── venv/                  # Virtual environment
```

## Setup Instructions

### Backend Setup

1. Create and activate virtual environment:
```bash
cd backend
python -m venv venv
source venv/Scripts/activate  # On Mac: venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install
```

4. Create a `.env` file in the backend directory:
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

5. Start the Flask server:
```bash
python main.py
```

### Frontend Setup

1. Install dependencies:
```bash
cd react-app
npm install
```

2. Start the development server:
```bash
npm start
```

### Database Setup

1. Create a new project in Supabase
2. Create a table named `data` with the following schema:

```sql
CREATE TABLE data (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    business_name TEXT NOT NULL,
    registration_date TEXT,
    state TEXT,
    principals_and_contact_information TEXT,
    mailing_address TEXT,
    latest_annual_report TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now())
);
```

## API Endpoints

### Search Business
- **URL**: `/api/crawl
- **Method**: `POST`
- **Body**:
```json
{
    "business_name": "ACME "
}
```

## Usage

1. Access the application at `http://localhost:3000`
2. Enter a business name in the search box
3. Click "Search" to initiate the crawl
4. View results in the table below

## Error Handling

The application includes error handling for:
- Invalid business names
- Network failures
- Database connection issues
- Missing data

## Development Notes

- The Playwright crawler respects rate limits and includes appropriate delays
- Search results are cached in Supabase to minimize redundant crawling
- The frontend implements debouncing on the search input
- Error boundaries are implemented in React components


## Known Issues

- MacOS users should use port 5001 for the backend server
- Maximum of 500 results per search (Florida Secretary of State limitation)
- Some business documents require payment and cannot be accessed
