from PIL import Image

dummy_plot_filenames = [
    "forecast_plot_kitakouchi.png",
    "forecast_plot_minamikawachi.png",
    "forecast_plot_mishima.png",
    "forecast_plot_nakawachi.png",
    "forecast_plot_osaka_east.png",
    # Add all other plot filenames as needed from your `dummy_plot_urls` in app.py
    "forecast_plot_toyono.png",
    "forecast_plot_sakai.png",
    "forecast_plot_senshu.png",
    "forecast_plot_osaka_north.png",
    "forecast_plot_osaka_west.png",
    "forecast_plot_osaka_south.png",
    "forecast_plot_otokuni.png",
    "forecast_plot_yamashiro_north.png",
    "forecast_plot_yamashiro_south.png",
    "forecast_plot_nantan.png",
    "forecast_plot_chutan_west.png",
    "forecast_plot_chutan_east.png",
    "forecast_plot_tango.png",
    "forecast_plot_kyoto_shi.png",
    "forecast_plot_nara_shi.png",
    "forecast_plot_koriyama.png",
    "forecast_plot_chuwa_east.png",
    "forecast_plot_chuwa_west.png",
    "forecast_plot_yoshino.png",
]

for filename in dummy_plot_filenames:
    img = Image.new('RGB', (400, 300), color = 'white') # Create a 400x300 white image
    img.save(filename)
    print(f"Created dummy image: {filename}")

print("All dummy plot files created.")