### 1. Formulating Question

### 2. Gather Data

1. Go to website [the numbers](https://www.the-numbers.com/)

2. Navigate to: Movies--> Budgets and finances

3. Create new csv file on google sheet, then collect data from site

### 3. Clean Data

1. Note there are '$0' dollars, we have to remove all these fields from our dataset

2. Click on top-left-corner of spread sheet--> data--> sort--> advance sorting option--> ✅ Data header row; sort by: worldwide ...--> sort

3. Now delete all "0" by holding shift key and pressing del key

4. Delete other unimportant feature too: serial no, release date, movie title, domestic gross

5. Format number: Go to Format--> number --> custom number format--> 0.00--> apply

6. Download cleaned csv file []()

### 4. Explore & visualize data

1. Open jypter notebook on browser [jupyter notebook](https://jupyter.org/try-jupyter/lab/?path=notebooks%2FIntro.ipynb)

2. create new notebook and name it "Linear regression"

3. upload clean dataset from local space

4. import libraries

```py
import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
```

5. Reading data from csv

```py
data = pandas.read_csv('dataset.csv')
```

6. exploring data

```py
data.describe()
```

7.

```py
X = DataFrame(data, columns=['production_budget_usd'])
y = DataFrame(data, columns=['worldwide_gross_usd'])
```

8.

```py
plt.figure(figsize=(10,6))
plt.scatter(X, y, alpha=0.3)
plt.title('Film Cost vs Global Revenue')
plt.xlabel('Production Budget $')
plt.ylabel('Worldwide Gross $')
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()

```

### 5. Train Algorithm

```py
regression = LinearRegression()
regression.fit(X, y)
```

```py
regression.coef_    # theta_1
```

```py
#Intercept
regression.intercept_
```

```py
plt.figure(figsize=(10,6))
plt.scatter(X, y, alpha=0.3)

# Adding the regression line here:
plt.plot(X, regression.predict(X), color='red', linewidth=3)

plt.title('Film Cost vs Global Revenue')
plt.xlabel('Production Budget $')
plt.ylabel('Worldwide Gross $')
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()

```

### 6. Evaluate

```py
#Getting r square from Regression
regression.score(X, y)
```
