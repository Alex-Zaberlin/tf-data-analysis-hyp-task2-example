import pandas as pd
import numpy as np
from scipy.stats import cramervonmises_2samp

chat_id = 282219367 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_value = 0.08
    return cramervonmises_2samp(x, y).pvalue < p_value# Ваш ответ, True или False
