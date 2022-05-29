# CIFO_2022

This project is the deliverable of Computational Intelligence for Optimization subject from University NOVA de Lisboa IMS 

The main goal if is to understand how Genetic Algorithms works, with the example of solve a sudoku puzzle.

The project is coded in python and analysed in SQL. 

Softwares need to run the code and results:

- IDE (ex.: Pycharm, VisualStudio, IntelliJ)
- Python installed with those libraries:
  * numpy
  * psycopg2
  * sql
  * scipy
  * statistics
  * math
  * intertools
  * operator
  * audioop
- PostgreSQL 

The project is dividev into 4 parts in this repository:

Folder Sudoku is composed by two main files .py:

- data_sudoku.py: the user add a Sudoku grid, where the empty spaces are returned as zeros
- functions.py: this file merge all the functions to identify the problem itself.
  *get_neighbour: to find the indiviuals of a population
  *split: to split the sudoku grid into a list of submatrixes 
  *fitness_min: fitness function to a minimization problem
  *fitness_max: fitness function to a maximization problem
  
 Folder Charles is composed by five main files .py:
 -Charles.py: there are the classes to create a Population and Individidual of this population
 -Crossover.py: crossover functions developed (single point, parallel mapped, between extremes and cycle)
 -mutation.py: mutation functions developed (mutation and swap_mutation)
 -selection.py: selection functions developed (roullete, rank and tournament)
 -GA.py: function which merge all the information above to make possible to solve the problem.
 
 Outside the folder has the third and forth part of the project:
 
 solve.py: is the code which combine the problem and the Genetic Algorithm in order to solve.
 
 while the analysis are made by:
 
 bancodedados.py: this code create tables and insert the information generated by solve.py into a online database of postgres.
 
 To access this database is necessary to download postgresql through this link: https://www.postgresql.org/download/
 (it's a open source SQL software although the servidor is a paid one with a limit of size) 
 To connect the database on postgresql:
 
 ![image](https://user-images.githubusercontent.com/71496553/170100074-26d58fc1-8913-4e20-bf20-7b4dee0eaa6c.png)

Click in Server, then:

![image](https://user-images.githubusercontent.com/71496553/170100255-de6b84b6-4d50-45ba-832b-677b9fa2846a.png)

Give a name for your connection.

![image](https://user-images.githubusercontent.com/71496553/170100433-15ebe565-b117-4864-9806-2eefb0bbb148.png)

Add the information in the connection tab (the password is in the bancodedados.py) 
