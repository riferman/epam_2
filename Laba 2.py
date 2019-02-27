from collections import Counter

n = 23

string = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print("Сount_each_letter",
      Counter(string))  # Find how many times each letter is met in the text, print the findings as described below

a = (sorted(list(Counter(string).items()), key=lambda x: x[0]))  # Sort the table by alphabet and print it out
print("Sort the table", a)
a.sort(key=lambda x: x[1])  # Sort the table by the symbols’ frequency count and print it out
print("Sort the table by the symbols", a)

print("List revers", list(reversed(a)))  # Flip this list horizontally and print it out

print("Getting only certain amount of entries from the top", list(reversed(a))[:n])
