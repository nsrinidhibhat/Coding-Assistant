# This file contains all the constants relevant to the Coding Assistant.
import os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
MODEL_CONFIG = config={
    "temperature": 0,
    "maxTokens": 1000,
}