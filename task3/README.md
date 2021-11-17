MyCoolSoft is the application that “throws” standard 6-sided dice - one to five items. 
A user provides information about the number of throws and minimal and maximal number of dice as command line arguments.

For each throw the application prints values on dice faces and counts the result of the throw: “1” adds 10 points, 
“5” adds 5 points while other sides (“2”, “3”, “4”, “6”) do not add anything. 
The special combination of  “1”, “2”, “3”, “4” and “5” equals to 150 points 
(“1” and “5” do not add anything separately in this case). 
The order of dice does not affect the result.

Examples of execution string:

```$ ./mycoolsoft_0 65 1 4```

Application throws dice 65 times, there might be 1, 2, 3 or 4 dice in each throw.

```$ ./mycoolsoft_0 12 3 3```

Application throws dice 12 times, there are 3 dice in each throw

Examples of result calculation and application output:

```
1 1 5 = 25
2 4 6 6 = 0
5 1 3 5 = 20
```
 
Six developers provided their own implementations of MyCoolSoft to be tested, 
named mycoolsoft_1 to mycoolsoft_6 available at https://drive.google.com/drive/folders/1NIJqUrmir8bVJWqct61GhLXFWpLSnAZ8?usp=sharing. 
mycoolsoft_0 is the reference version that should not contain any errors. All of these are compiled for Ubuntu 18 using gcc 7.5 (glibc 2.27).

Tasks for our candidate are to automate the testing process and find as many errors in various implementations.

Final check will be performed using mycoolsoft_7 that is not present in the shared folder.
