from flask import Flask, jsonify, send_from_directory, request
import json
import os
from PIL import Image # Required for creating dummy PNGs, install with: pip install Pillow

app = Flask(__name__)

# --- Load GeoJSON data once on server start ---
# Ensure these JSON files (kyoto_overlay.json, osaka_overlay.json, nara_overlay.json)
# are in the same directory as this app.py file.
try:
    with open('kyoto_overlay.json', 'r', encoding='utf-8') as f:
        kyoto_data = json.load(f)
    with open('osaka_overlay.json', 'r', encoding='utf-8') as f:
        osaka_data = json.load(f)
    with open('nara_overlay.json', 'r', encoding='utf-8') as f:
        nara_data = json.load(f)
    print("✅ Successfully loaded GeoJSON overlay files.")
except FileNotFoundError as e:
    print(f"❌ Error loading GeoJSON file: {e}. Make sure the JSON files are in the same directory.")
    # Exit or handle gracefully if critical files are missing
    exit(1)
except json.JSONDecodeError as e:
    print(f"❌ Error decoding JSON from overlay file: {e}. Check JSON file format.")
    exit(1)


# --- Dummy Case Data ---
# This dictionary simulates the influenza case data.
# The keys here MUST match the 'database names' defined in the
# `REGION_GROUP_TO_DB_NAME_MAP` in your `merged_map_v1.4.1.html` file.
# Values are arbitrary numbers representing influenza cases.
dummy_case_data = {
    "Kitakouchi": 55,
    "Minamikawachi": 30,
    "Mishima": 45,
    "Nakawachi": 22,
    "Osaka-shi-East": 18,
    "Toyono": 12,
    "Sakai-shi": 40,
    "Senshuu": 25,
    "Osaka-shi-North": 60,
    "Osaka-shi-West": 35,
    "Osaka-shi-South": 28,
    "Otokuni": 15,
    "Yamashiro-North": 10,
    "Yamashiro-South": 5,
    "Nantan": 8,
    "Chutan-West": 3,
    "Chutan-East": 7,
    "Tango": 4,
    "Kyoto-shi": 70,
    "Nara-shi": 50,
    "Koriyama": 20,
    "Chuwa-East": 9,
    "Chuwa-West": 14,
    "Yoshino": 6,
    "Osaka-Prefecture": 200, # Example total for the entire prefecture
    "Kyoto-Prefecture": 150,
    "Nara-Prefecture": 100,
}
print("✅ Dummy case data loaded.")


# --- Dummy Forecast Plot URLs ---
# This maps region names (matching the `REGION_GROUP_TO_DB_NAME_MAP` values)
# to dummy image file paths.
# Ensure these dummy PNG files are created in the same directory.
dummy_plot_urls = {
    "Kitakouchi": "forecast_plot_kitakouchi.png",
    "Minamikawachi": "forecast_plot_minamikawachi.png",
    "Mishima": "forecast_plot_mishima.png",
    "Nakawachi": "forecast_plot_nakawachi.png",
    "Osaka-shi-East": "forecast_plot_osaka_east.png",
    "Toyono": "forecast_plot_toyono.png",
    "Sakai-shi": "forecast_plot_sakai.png",
    "Senshuu": "forecast_plot_senshu.png",
    "Osaka-shi-North": "forecast_plot_osaka_north.png",
    "Osaka-shi-West": "forecast_plot_osaka_west.png",
    "Osaka-shi-South": "forecast_plot_osaka_south.png",
    "Otokuni": "forecast_plot_otokuni.png",
    "Yamashiro-North": "forecast_plot_yamashiro_north.png",
    "Yamashiro-South": "forecast_plot_yamashiro_south.png",
    "Nantan": "forecast_plot_nantan.png",
    "Chutan-West": "forecast_plot_chutan_west.png",
    "Chutan-East": "forecast_plot_chutan_east.png",
    "Tango": "forecast_plot_tango.png",
    "Kyoto-shi": "forecast_plot_kyoto_shi.png",
    "Nara-shi": "forecast_plot_nara_shi.png",
    "Koriyama": "forecast_plot_koriyama.png",
    "Chuwa-East": "forecast_plot_chuwa_east.png",
    "Chuwa-West": "forecast_plot_chuwa_west.png",
    "Yoshino": "forecast_plot_yoshino.png",
}
print("✅ Dummy plot URLs configured.")


# --- Route to serve the main HTML file ---
@app.route('/')
def index():
    """Serves the main HTML file."""
    # Ensure 'merged_map_v1.4.1.html' is in the same directory as app.py
    return send_from_directory('.', 'merged_map_v1.4.1.html')

# --- Route to serve static files (GeoJSON, images, etc.) ---
@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serves static files like GeoJSON overlays and forecast plot images."""
    # This assumes static files are in the same directory as app.py
    return send_from_directory('.', filename)

# --- API endpoint for total cases data ---
@app.route('/api/total_cases')
def get_total_cases():
    """
    Returns dummy influenza case data as JSON.
    In a real application, this would fetch live data from a database or external service.
    """
    print("Serving /api/total_cases request.")
    return jsonify(dummy_case_data)

# --- API endpoint for forecast data ---
@app.route('/api/forecast')
def get_forecast():
    """
    Returns a dummy forecast plot URL for a given region.
    Expects a 'region' query parameter (e.g., /api/forecast?region=Kitakouchi).
    """
    region = request.args.get('region')
    print(f"Serving /api/forecast request for region: {region}")
    if region:
        plot_url = dummy_plot_urls.get(region)
        if plot_url:
            # The frontend expects 'plot_url' key in the response
            return jsonify({"region": region, "plot_url": f"/static/{plot_url}"})
        else:
            # If region not found in dummy_plot_urls, return an error
            return jsonify({"error": f"No forecast data available for region: {region}"}), 404
    else:
        # If 'region' parameter is missing, return an error
        return jsonify({"error": "Region parameter is missing"}), 400

# --- Function to create dummy PNG files ---
def create_dummy_png_files():
    """
    Creates blank PNG files for the dummy forecast plots if they don't exist.
    This is for development/testing purposes.
    """
    print("Checking for dummy plot files...")
    for filename in dummy_plot_urls.values():
        file_path = os.path.join(os.path.dirname(__file__), filename) # Get absolute path
        if not os.path.exists(file_path):
            try:
                # Create a simple 400x300 white image
                img = Image.new('RGB', (400, 300), color = 'white')
                img.save(file_path)
                print(f"Created dummy image: {file_path}")
            except Exception as e:
                print(f"Error creating dummy image {file_path}: {e}")
        else:
            print(f"Dummy image already exists: {file_path}")
    print("Finished checking/creating dummy plot files.")

# --- Main entry point for running the Flask app ---
if __name__ == '__main__':
    # Call the function to create dummy PNGs before running the app
    create_dummy_png_files()
    
    # Run the Flask development server
    # debug=True enables reloader and debugger, useful for development
    app.run(debug=True)
