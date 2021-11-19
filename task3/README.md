## Assignment

```MyCoolSoft is the application that “throws” standard 6-sided dice - one to five items. 
A user provides information about the number of throws and minimal and maximal number of dice as command line arguments.

For each throw the application prints values on dice faces and counts the result of the throw: 
“1” adds 10 points, “5” adds 5 points while other sides (“2”, “3”, “4”, “6”) do not add anything. 
The special combination of  “1”, “2”, “3”, “4” and “5” equals to 150 points 
(“1” and “5” do not add anything separately in this case). 
The order of dice does not affect the result.

Examples of execution string:

```$ ./mycoolsoft_0 65 1 4```

Application throws dice 65 times, there might be 1, 2, 3 or 4 dice in each throw.

```$ ./mycoolsoft_0 12 3 3```

Application throws dice 12 times, there are 3 dice in each throw

Examples of result calculation and application output:

1 1 5 = 25
2 4 6 6 = 0
5 1 3 5 = 20


mycoolsoft_0 is the reference version that should not contain any errors.

Tasks for our candidate are to automate the testing process and find as many errors in various implementations.

Final check will be performed using mycoolsoft_7 that is not present in the shared folder.
```

## Resolution

1. Implemented own realization for reference.
2. Implemented wrapper for binary files provided.
3. Implemented parametrized unittest testcases.

To run test:
1. Use python 3.9
2. From root folder run ```PYTHONPATH=$(pwd) python3 task3/tests/test_mycoolsoft.py task3/reference/mycoolsoft_0``` to run tests against mycoolsoft_0

Errors found:
1. mycoolsoft_0 does not raise Error for "not number" params passed to input like 'a' or '.' or ''.
2. mycoolsoft_0 does not raise Error for float numbers passed like '1.1' is interpreted as 1.
3. mycoolsoft_1 is the same behavior as for mycoolsoft_0.
4. mycoolsoft_2 same errors as for mycoolsoft_0.
5. mycoolsoft_2 wrong result calculation. It simply sums outcome. Like (1, 5) is 6 but should be 15.
6. mycoolsoft_3 same as for mycoolsoft_0.
7. mycoolsoft_3 gives wrong number of throws for 100000, 10000, 1000, it throws 99999, 9999, 999.
8. mycoolsoft_4 same as for mycoolsoft_0.
10. mycoolsoft_5 same as for mycoolsoft_0.
11. mycoolsoft_5 no error thrown for negative amount of throws and negative ranges.
12. mycoolsoft_6 same errors as for mycoolsoft_0
