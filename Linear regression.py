{"cells":[{"metadata":{},"cell_type":"markdown","source":"# Welcome to Jupyter!"},{"metadata":{"trusted":true},"cell_type":"code","source":"import pandas as pd\nimport numpy as np\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import mean_squared_error, r2_score\nimport matplotlib.pyplot as plt\n\nnp.random.seed(42)\n\nsquare_feet = np.random.randint(1000, 4000, 100)  \nbedrooms = np.random.randint(1, 6, 100)  \nbathrooms = np.random.randint(1, 4, 100)  \n\nprice = square_feet * 150 + bedrooms * 10000 + bathrooms * 20000 + np.random.randint(10000, 50000, 100)\n\ndf = pd.DataFrame({\n    'Square_Feet': square_feet,\n    'Bedrooms': bedrooms,\n    'Bathrooms': bathrooms,\n    'Price': price\n})\n\nprint(df.head())\nX = df[['Square_Feet', 'Bedrooms', 'Bathrooms']]\ny = df['Price']  \n\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)\n\ny_pred = model.predict(X_test)\nmse = mean_squared_error(y_test, y_pred)\nr2 = r2_score(y_test, y_pred)\n\nprint(f\"Mean Squared Error: {mse}\")\nprint(f\"R-squared: {r2}\")\n\nplt.scatter(y_test, y_pred)\nplt.xlabel(\"True Prices\")\nplt.ylabel(\"Predicted Prices\")\nplt.title(\"True vs Predicted House Prices\")\nplt.show()\n","execution_count":1,"outputs":[{"output_type":"stream","text":"   Square_Feet  Bedrooms  Bathrooms   Price\n0         1860         4          1  352436\n1         2294         3          3  452854\n2         2130         3          2  410177\n3         2095         1          2  380145\n4         2638         3          1  475438\nMean Squared Error: 153880497.74201012\nR-squared: 0.9906619067811275\n","name":"stdout"},{"output_type":"display_data","data":{"text/plain":"<Figure size 432x288 with 1 Axes>","image/png":"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\n"},"metadata":{"needs_background":"light"}}]},{"metadata":{},"cell_type":"markdown","source":"This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).\n\nOutline of some basics:\n\n* [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)\n* [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)\n* [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)\n* [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)\n* [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)\n* [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)\n* [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages."},{"metadata":{},"cell_type":"markdown","source":"You can also get this tutorial and run it on your laptop:\n\n    git clone https://github.com/ipython/ipython-in-depth\n\nInstall IPython and Jupyter:\n\nwith [conda](https://www.anaconda.com/download):\n\n    conda install ipython jupyter\n\nwith pip:\n\n    # first, always upgrade pip!\n    pip install --upgrade pip\n    pip install --upgrade ipython jupyter\n\nStart the notebook in the tutorial directory:\n\n    cd ipython-in-depth\n    jupyter notebook"},{"metadata":{"trusted":true},"cell_type":"code","source":"import pandas as pd\nimport numpy as np\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import mean_squared_error, r2_score\nimport matplotlib.pyplot as plt\n\n# Generating a synthetic dataset\nnp.random.seed(42)\n\n# Generate random data for square footage, bedrooms, and bathrooms\nsquare_feet = np.random.randint(1000, 4000, 100)  # Square footage between 1000 and 4000\nbedrooms = np.random.randint(1, 6, 100)  # Bedrooms between 1 and 5\nbathrooms = np.random.randint(1, 4, 100)  # Bathrooms between 1 and 3\n\n# Assume house prices depend on square footage, number of bedrooms, and bathrooms\nprice = square_feet * 150 + bedrooms * 10000 + bathrooms * 20000 + np.random.randint(10000, 50000, 100)\n\n# Creating a DataFrame\ndf = pd.DataFrame({\n    'Square_Feet': square_feet,\n    'Bedrooms': bedrooms,\n    'Bathrooms': bathrooms,\n    'Price': price\n})\n\n# Display the first few rows of the dataset\nprint(df.head())\n\n# Features and Target\nX = df[['Square_Feet', 'Bedrooms', 'Bathrooms']]  # Features\ny = df['Price']  # Target\n\n# Split the data into training and testing sets\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\n# Initialize and train the Linear Regression model\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)\n\n# Make predictions\ny_pred = model.predict(X_test)\n\n# Evaluate the model\nmse = mean_squared_error(y_test, y_pred)\nr2 = r2_score(y_test, y_pred)\n\n# Print model performance\nprint(f\"Mean Squared Error: {mse}\")\nprint(f\"R-squared: {r2}\")\n\n# Visualize the predictions\nplt.scatter(y_test, y_pred)\nplt.xlabel(\"True Prices\")\nplt.ylabel(\"Predicted Prices\")\nplt.title(\"True vs Predicted House Prices\")\nplt.show()\n","execution_count":null,"outputs":[]}],"metadata":{"kernelspec":{"name":"python3","display_name":"Python 3","language":"python"},"language_info":{"name":"python","version":"3.6.15","mimetype":"text/x-python","codemirror_mode":{"name":"ipython","version":3},"pygments_lexer":"ipython3","nbconvert_exporter":"python","file_extension":".py"}},"nbformat":4,"nbformat_minor":2}