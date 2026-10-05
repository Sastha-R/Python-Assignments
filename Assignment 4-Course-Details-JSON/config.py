from dotenv import load_dotenv
import os
from pathlib import Path


load_dotenv()

COURSE_FILE : Path = Path(os.getenv("COURSE_FILE"))

ENROLL_FILE : Path = Path(os.getenv("ENROLL_FILE"))

