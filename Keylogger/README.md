<h2>Python-Keylogger</h2>
Keylogger is the tool that is used to record keystrokes. It can be used for good purposes as well as malicious purposes. Parents can use keyloggers for monitoring children's screen time, companies can use keyloggers to keep track of employee's productivity. However, hackers can install keyloggers and gain access to sensitive information like date of birth, credit card details, passwords, and so on.

<h2>Steps for Project</h2>
This project stores keyloggers and outputs stored keyloggers as a .txt file. <br>
1. For this project, I imported the module pynput from the keyboard library by typing

`pip install pynput` in the visual studio terminal. <br>
2. I created the main method and introduced a listener object where we passed the on_press parameter so that whatever is typed it is stored in the object. <br>
3. Then we defined a function to convert the keys into the string and print it as a .txt file. <br>
4. Then, we asked the program to store the key as a character. While running this program computer will detect this program as a virus, so I went ahead and changed the settings in my Mac so it would not detect this program as a virus. <br>
