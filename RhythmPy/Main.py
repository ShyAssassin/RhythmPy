try:
    from src import Run
except ImportError:
    from .src import Run

if __name__ == "__main__":
    Run()