from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

class Database:
    def __init__(self):
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    def insert_business(self, business_data):
        try:
            result = self.supabase.table('data').insert(business_data).execute()
            return result.data
        except Exception as e:
            print(f"Error inserting data: {str(e)}")
            return None
    
    def get_business(self, business_name):
        try:
            result = self.supabase.table('data').select('*').ilike('business_name', f'%{business_name}%').execute()
            return result.data
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            return None