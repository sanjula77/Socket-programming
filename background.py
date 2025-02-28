from rembg import remove
from PIL import Image
import onnxruntime as ort

# Force ONNXRuntime to use CPU only
ort.set_default_logger_severity(3)  # Suppress unnecessary logs
providers = ["CPUExecutionProvider"]  # Force CPU execution

# Input and output paths
input_path = r"C:\Users\ASUS\Desktop\greenplatimg\croplogo.png"
output_path = r"C:\Users\ASUS\Desktop\greenplatimg\a\output.png"

# Process image
image = Image.open(input_path)
output = remove(image, session_options=None, providers=providers)
output.save(output_path)
