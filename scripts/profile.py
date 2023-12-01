from ydata_profiling import ProfileReport
import os
import pandas as pd
if not os.path.exists('./profiling'):
  os.makedirs('profiling', exist_ok=True)
columns=['class','Alcohol','Malic acid','Ash','Alcalinity_of_ash','Magnesium','Total_phenols','Flavanoids','Nonflavanoid_phenols','Proanthocyanins',
         'Color_intensity','Hue,','OD280_OD315_of_diluted_wines','Proline']
df=pd.read_csv("./data/wine/wine.data", names=columns,
                              sep=', ', engine='python')
profile= ProfileReport(df, title='Profiling Report')
profile.to_file(os.path.join('profiling', "report.html"))