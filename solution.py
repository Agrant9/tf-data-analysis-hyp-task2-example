import pandas as pd
import numpy as np
import scipy.stats as st


chat_id = 544835691 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    pval = permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis), 
                            vectorized=True, n_resamples=1000, alternative="two-sided").pvalue
    return True if pval < 0.07 else False # Ваш ответ, True или False
