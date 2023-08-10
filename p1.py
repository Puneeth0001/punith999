import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:\\Users\\Admin\\Desktop\\mtcars.csv")

mpg=data['mpg']
plt.hist(mpg)
plt.show()
print