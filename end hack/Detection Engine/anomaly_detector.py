
import numpy as np
from sklearn.ensemble import IsolationForest
import time
import random
import logging
from collections import deque
from flask import Flask, jsonify, render_template

# Flask web framework initialization
app = Flask(__name__)

# invalid content 

    # Start the Flask web application
    app.run(debug=True, host="0.0.0.0", port=5000)
