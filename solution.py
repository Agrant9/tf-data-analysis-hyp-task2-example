import pandas as pd
import numpy as np
import scipy.stats as st


chat_id = 544835691 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, pval = st.ttest_ind(x, y, equal_var = False, alternative = 'less')
    return True if pval < 0.07 else False # Ваш ответ, True или False
