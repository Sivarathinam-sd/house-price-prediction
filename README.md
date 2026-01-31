# House Price Prediction
Predicts house prices using machine learning by analysing property features, historical data, location to provide accurate real-estate values estimates.

<img src="hero.png" />

## Steps to Setup Github and Project

1. Open CMD and enter `python --version`, If python is not installed please visit <a>https://www.python.org/downloads/</a> <br>run the executable and follow the installation wizard.
2. Check whether git is install in the system `git --version`, visit <a>https://git-scm.com</a> to download and install git, alternatively git can also be installed using homebrew for mac users.
3. Install uv using the pip pakage manager `pip install uv` 
4. It is time to get your hands on the project by bringing it to your local repository.<br> `git clone https://github.com/Sivarathinam-sd/house-price-prediction.git`

## 2. Data Cleaning
1. We checked for missing values and found out that few columns `numBathrooms,  numBalconies, isNegotiable` had null values and was taken care by replacing them with assumed relevent data. <br> eg. The column `numBathrooms` had the unique values from '1', so we assumed the missing data would be '0'.
2. The `priceSqFt` column which should explain the price per square feet respect to the house was filled with null values, which felt use less for modeling and we removed it similarly columns like `verificationDate, description` was also removed due to irrelevance to the study and the price prediction model.
3. we examined unique for every columns to find out if any other datatypes or irrevevant data are present in that columns to avoid any `ValueError` and handled respectively.
4. we discovered that the given columns `house_size,SecurityDeposit` had few str values and we transformed them to their primary datatype.for eg. `SecurityDeposit` had 'No deposit' values and rest of them were numbers, so  where ever 'No Deposit' values were replaced with 0.
5. Finally, we got our final datset cleaned and ready for further processing. 
   
