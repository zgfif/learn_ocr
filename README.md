sudo pacman -S tesseract
sudo pacman -S tesseract-data-deu
sudo pacman -S tesseract-data-eng

python -m venv .venv

source .venv/bin/activate
pip install pytest
pip install opencv-python # for cv2 module
pip install pytesseract Pillow



python -m pytest
