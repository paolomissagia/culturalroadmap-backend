import os
from supabase import create_client, Client
from flask import Flask
from dotenv import load_dotenv
load_dotenv()

# flask
app = Flask(__name__)

# supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


# routes
@app.route('/<level>/<category>')
def get_guide_by_level_and_category(level = None, category = None):
    # query supabase
    response = supabase.table('guides').select("*").eq('level', level).eq('category', category).execute()
    # return response
    return str(response.data)