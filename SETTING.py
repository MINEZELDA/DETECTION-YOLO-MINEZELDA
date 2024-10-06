from pathlib import Path
import sys
FILE = Path(__file__).resolve()
ROOT = FILE.parent
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
ROOT = ROOT.relative_to(Path.cwd())
IMAGE = 'IMAGE'
VIDEO = 'VIDEO'
SOURCES_LIST = [IMAGE, VIDEO]
IMAGES_DIR = ROOT / 'IMAGES'
DEFAULT_IMAGE = IMAGES_DIR / 'LISA.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'LISADETECTION.jpg'
VIDEO_DIR = ROOT / 'VIDEOS'
VIDEOS_DICT = {
    'LISAROCKSTAR.mp4': VIDEO_DIR / 'LISAROCKSTAR.mp4',
    'LISAMONEY.mp4': VIDEO_DIR / 'LISAMONEY.mp4',
    'LISALARISA.mp4': VIDEO_DIR / 'LISALARISA.mp4',
}
MODEL_DIR = ROOT / 'WEIGHTS'
DETECTION_MODEL = MODEL_DIR / 'yolo11n.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'yolo11n-seg.pt'
