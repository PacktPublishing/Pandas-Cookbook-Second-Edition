## [Get this title for $10 on Packt's Spring Sale](https://www.packt.com/B15597?utm_source=github&utm_medium=packt-github-repo&utm_campaign=spring_10_dollar_2022)
-----
For a limited period, all eBooks and Videos are only $10. All the practical content you need \- by developers, for developers

# Pandas 1.x Cookbook - 2nd Edition
This is the code repository for [Pandas 1.x Cookbook - 2nd Edition](https://www.packtpub.com/programming/pandas-1-x-cookbook-second-edition), published by [Packt](https://www.packtpub.com/). It contains all the supporting project files necessary to work through the book from start to finish.

## About the Book
A new edition of the bestselling Pandas cookbook updated to pandas 1.x with new chapters on creating and testing, and exploratory data analysis. Recipes are written with modern pandas constructs. This book also covers EDA, tidying data, pivoting data, time-series calculations, visualizations, and more.

## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.

The code will look like the following:
```
def tweak_kag(df):
    na_mask = df.Q9.isna()
    hide_mask = df.Q9.str.startswith('I do not').fillna(False)
    df = df[~na_mask & ~hide_mask]

```


## Related Products
* [Artificial Intelligence with Python – Second Edition](https://www.packtpub.com/in/data/artificial-intelligence-with-python-second-edition)

* [Mastering Machine Learning Algorithms - Second Edition](https://www.packtpub.com/in/data/mastering-machine-learning-algorithms-second-edition)