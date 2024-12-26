import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
FLORIDA_BUSINESS_SEARCH_URL = "https://search.sunbiz.org/Inquiry/CorporationSearch/ByName"