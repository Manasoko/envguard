import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    import envguard as _envguard
    sys.modules.setdefault("envguard", _envguard)
except ImportError:
    pass
