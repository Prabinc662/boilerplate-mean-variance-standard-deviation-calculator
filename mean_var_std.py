import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        initial_array = np.array(list)
        new_array = initial_array.reshape(3,3)
        initial_mean = []
        transpose_mean = []
        initial_var = []
        transpose_var = []
        initial_std = []
        transpose_std = []
        initial_max = []
        transpose_max = []
        initial_min = []
        transpose_min = []
        initial_sum = []
        transpose_sum = []
        for i in new_array:
            initial_mean.append(np.mean(i))
            initial_var.append(np.var(i))
            initial_std.append(np.std(i))
            initial_max.append(np.max(i))
            initial_min.append(np.min(i))
            initial_sum.append(np.sum(i))
            
        for j in new_array.T:
            transpose_mean.append(np.mean(j))
            transpose_var.append(np.var(j))
            transpose_std.append(np.std(j))
            transpose_max.append(np.max(j))
            transpose_min.append(np.min(j))
            transpose_sum.append(np.sum(j))
            
        result_mean = [transpose_mean, initial_mean, np.mean(initial_array)]
        result_variance = [transpose_var, initial_var, np.var(initial_array)]
        result_std_dev = [transpose_std, initial_std, np.std(initial_array)]
        result_max = [transpose_max, initial_max, np.max(initial_array)]
        result_min = [transpose_min, initial_min, np.min(initial_array)]
        result_sum = [transpose_sum, initial_sum, np.sum(initial_array)]
        calculations = {'mean': result_mean,
                'variance': result_variance,
                'standard deviation': result_std_dev,
                'max': result_max,
                'min': result_min,
                'sum': result_sum
                }
        return calculations