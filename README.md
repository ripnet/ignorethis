### pynet homework

###### Classes
1. Completed `2016-10-15`

###### Issues 
- Python uses whitespace (yuck)
- Python does not like curly braces. Sacrilege.
- Python wants functions to be defined before using them. This is _super ugly_. I prefer to see helper functions at the bottom of a file, and the "main" function at the top. Yes, I know about `import`
- I can't test a variable assignment like I can in other languages. Another demerit for python. This code below requires two lines instead of one:
```Python
if match = re.search("set transform-set (.*)", child.text):
         ^
SyntaxError: invalid syntax
```
- This is ***completely unacceptable***:
```
$ python3 -c 'print(3/2)'
1.5
$ python2 -c 'print(3/2)'
1
```
- It seems the preferred style is_using_underscores. I think that requires too much typing and I much prefer camelCase. Fortunately, this isn't enforced.
