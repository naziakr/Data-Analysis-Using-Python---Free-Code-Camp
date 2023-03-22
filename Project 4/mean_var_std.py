import numpy as np

def calculate(list):
    if (len(list)<9):
      raise ValueError ("List must contain nine numbers.")
    else:
      a = np.array(list).reshape (3,3)
      dict  = {}
      mean1 = np.mean(a, axis = 0).tolist()
      mean2 = np.mean(a, axis = 1).tolist()
      mean3 = np.mean(list)
      dict["mean"] = [mean1, mean2, mean3]
      var1 = np.var(a, axis = 0).tolist()
      var2 = np.var(a, axis=1).tolist()
      var3 = np.var(list)
      dict["variance"] = [var1, var2, var3]
      std1 = np.std(a, axis = 0).tolist()
      std2 = np.std(a,axis = 1).tolist()
      std3 = np.std(list)
      dict["standard deviation"] = [std1, std2, std3]
      max1 = np.max(a, axis =0).tolist()
      max2 = np.max(a, axis =1).tolist()
      max3 = np.max(list)
      dict["max"] = [max1, max2, max3]
      min1 = np.min(a, axis =0).tolist()
      min2 = np.min(a, axis =1).tolist()
      min3 = np.min(list)
      dict["min"] = [min1, min2, min3]
      sum1 = np.sum(a, axis =0).tolist()
      sum2 = np.sum(a, axis =1).tolist()
      sum3 = np.sum(list)
      dict["sum"] = [sum1, sum2, sum3]




    return dict
