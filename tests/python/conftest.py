import sys
from pathlib import Path

# Make scripts/ importable as top-level modules in tests.
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
