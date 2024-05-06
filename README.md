#name and Stevens login:
Fangqin Li fli31@stevens.edu

#the URL of your public GitHub repo:
https://github.com/FangqinLi/Text-based-adventure-game.git

#an estimate of how many hours you spent on the project:
25 hours

#a description of how you tested your code:
I interacted with it using the command line with the terminal of vscode, to act like a real player who wants to play this game. I also ran doctest for every function.

#any bugs or issues you could not resolve:
When I typed in ^D, it shows "I don't understand that" instead of the message indicating the user "Use 'quit' to exit."

#an example of a difficult issue or bug and how you resolved:


#a list of the three extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate them (i.e., what are the new verbs/features, how do you exercise them, where are they in the map):
1. Adding the "help" verb as the example of project requirements stated. You can always type in "help" to get what command you can use and if they should be followed by an argument. As I added the verb "drop", it is also shown after you typed in "help", and of course, "help" itself.
2. Adding the "drop" verb as the example of project requirements stated. After you "get" an item from a room that has one, you can drop it in any room. If you then "look" the room, there should be the item you dropped there. Also it is then not in your "inventory".
