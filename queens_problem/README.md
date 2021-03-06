# 8 Queens Problem
Here is the 8 Queens problem that is solved by "__Simulated Anealing__" algorithm.\
This little project has 2 files ("**main.py**" and "**queen_class.py**") that "**main.py**" is just a fast test for the main written algorithm ("**queen_class.py**").
## main.py
Just run this file by ```python3 main.py``` to see how the algorithm works.
## queen_class.py
Our main code is here.\
I declared 7 diffrent classes that are like this:
* **Environment Class**
* **Board Class**
* **Node Class**
* **Direction Class**
* **Colors Class**
### Environment Class
The biggest class in the project.\
This class involves the solving algorithm using __Simulated Anealing__.\
There are two functions named "**start_solve**" and "**simulated_anealing**" that "**start_solve**" is a loop for starting "**simulated_anealing**" from diffrent positions.\
"__simulated_anealing__" function returns nothing and everytime it is called, just changes the place of a queen to best of 8 directions around the queen or if it's the first move of node and we can't move to anydirections, we move the node to a random place in the same row (the random move was optional and I think it worth it).
### Board Class
__Board Class__ is the second biggest class after __Environment Class__.\
This class has an 8x8 dictionary attribute named "__nodes__" with keys like (x, y) and values of __Node__ object.\
Also with printing a board object, you can see the actual graphical autogenerated board and if the board is solved, you can see the answer ofcourse.\
This class will generate random board with 8 random queens placed in it with just initializing the class.
### Node Class
This class is used to have some functions like "**set_f**" to set the heuristic of that node based on how many queens can directly or nondirectly attack the queen placed in this node.\
"**f**" attribute of every node equals to (number of queens that can directly or nondirectly attack this queen) that this functionality is handled in "**set_f**" function in every node.\
"**set_queen**" is a function in __Node Class__ that will make __queen__ variable of the node to __Ture__ or __False__.\
This function also record queen nodes in __queens__ global variable.
### Direction Class
Used as an Enum Class to determine where the next queen should go.
### Colors Class
An Enum Class that has some color codes used for beauty of Board.