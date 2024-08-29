import sys
import os
import importlib

module_path = os.path.dirname(__file__)
sys.path.insert(0, module_path)

main = importlib.import_module("main")

globals().update(
    {name: getattr(main, name) for name in dir(main) if not name.startswith("_")}
)
