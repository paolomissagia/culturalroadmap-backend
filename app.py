import os
from supabase import create_client, Client
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()

# flask
app = Flask(__name__)
CORS(app)

# supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


# routes
@app.route('/<category>/<level>')
def get_guide_by_category_and_level(category=None, level=None):
    # query supabase
    response = supabase.table('guides').select(
        "*").eq('category', category).eq('level', level).execute()
    # return response
    return str(response.data)
