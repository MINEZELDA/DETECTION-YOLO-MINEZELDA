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
DEFAULT_IMAGE = IMAGES_DIR / 'PICP.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'PI.jpg'
VIDEO_DIR = ROOT / 'VIDEOS'
VIDEOS_DICT = {
    'VDO_1': VIDEO_DIR / 'VDO_1',
    'VDO_2': VIDEO_DIR / 'VDO_2',
    'VDO-3': VIDEO_DIR / 'VDO-3',
}
MODEL_DIR = ROOT / 'WEIGHTS'
DETECTION_MODEL = MODEL_DIR / 'yolo11n.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'yolo11n-seg.pt'
