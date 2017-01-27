# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> They are similar because they are both unordered iterable data structures.  They are different because tuples cannot be modified once made, while lists can.  Tuples work as keys in dictionary because you want to be sure your keys will not change.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> They are similar because they are both unordered iterable data structures.  They are different because sets have the whole host of set operations associated with them and also there can be repetition of values in sets.  It would be easier to find an item in a set becuase there would be less items in it and you'd simply search for a subset.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is an anonymous function.  It is basically a function that you use once in a certain specific case where you are transforming data according to a rule such as in the map and filter functions.  
people = [(John,Aspiring Data Scientist, 25),(Matt,Trucker, 30),(Alfred,Retired,80)]
sort_by_age = sorted(people, key = lambda person: person[2])

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions create a list by applying every value in a range or i in a list to the conditions or function specified.
return [x**2 for x in range(10) if x % 2 == 1]  This returns the square of odd numbers between 0 and 10.
my_list = [1,3,5,7,9]
return map(lambda y: y**2, filter(lambda x: x % 2 == 1, my_list))


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 Days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 Days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 Days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





