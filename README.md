# **Snake-Game** 
![Responsive](/images/responsive.png "Responsive-Design")<hr>
<p>Snake-Game is a old but very popular game.<br>
This game is always reminiscent of the first cells phone that came out.<br><br>
"Snake" is a very easy game at beginning but after becomes more, and more difficult.<br>
This game can train the logic and reaction of each person.<br><br>
The game has the "Score" option where you can see how much food your snake actually eat.<br>
At the end of the you have the "Final Score" option where you can see how many points did you get.<br> <br>
This project is the third of five milestone projects that needs to be completed by me in order to obtain the Full Stack Development Diploma from <a href="https://codeinstitute.net/">Code Institute</a> <br>
Required technologies for the project: <b><u>Python</u></b><br><br>
A live version of this project can be found <a href="https://snake-game-sbn.herokuapp.com/">here!</a><hr>
</p>

# **Table of Content**
<ul>
<li><a href="#ux">UX</a></li>
<li><a href="#user-stories">User Stories</a></li>
<li><a href="#user-goals">User Goals</a></li>
<li><a href="#project-requirements">Project Requirements</a></li>
<li><a href="#features">Features</a></li>
<li><a href="#technologies-used">Technologies Used</a></li>
<li><a href="#testing">Testing</a></li>
<li><a href="#development-and-deployment">Development and Deployment</a></li>
<li><a href="#credits">Credits</a></li>
<li><a href="#acknowledgment">Acknowledgment</a></li>
</ul><hr>

# **UX** 

### **This game is ment for:**
<ul>
<li>All individuals that wants to relax playing a good game.</li>
<li>All individuals that wants to remember for old times.</li></ul><hr>

### **User Stories**
<ul>
<li>I want to relax playing a game.</li>
<li>I want to know how good i am in the game.</li>
<li>I want to know how many points i can have at the end.</li>
<li>I want to remember the old times.</li></ul><hr>

### **User Goals**

*To make every user happy and have a good time in the game.*<hr>

### **Project Requirements**

*Python application using libraries and deployed to a cloud-based platform.*<hr>

# **Features**

*Snake Game consists of one feature. The user is playing and at the end he will receive the final score.*<hr>

### **Start Game** <hr>

The game will automate start when the user will access the link. <br>
The snake in game is under "-" symbol. The snake have to eat food that in game is under "#" symbol, in order to obtain more points.<br><br>
![Features-1](/images/features-1.png "Features-1")<hr><br>

On the window upper level left side you can see the Live Score after every time when the snake eat food.<br><br>
![Features-2](/images/features-2.png "Features-2")<hr><br>

During the game after more food your snake become bigger and bigger.<br>
At the end in case you'll lose, the final score of points will appear on console.<br><br>
![Features-3](/images/features-3.png "Features-3")<hr><br>

# **Technologies Used**

### **Languages**
<br>

<ul>
<li><a href="https://en.wikipedia.org/wiki/Python_programming_language">Python</a></li>
<li><a href="https://en.wikipedia.org/wiki/HTML">HTML</a> - Provided in Code Institute template</li>
<li><a href="https://en.wikipedia.org/wiki/CSS">CSS</a> - Provided in Code Institute template</li>
<li><a href="https://en.wikipedia.org/wiki/javascript">JavaScript</a> - Provided in Code Institute template</li>
</ul><hr><br>

### **Libraries**
<br>

<ul>
<li><a href="https://docs.python.org/3/howto/curses.html">Curses</a></li>
<li><a href="https://docs.python.org/3/library/random.html">Random</a></li>
</ul><hr><br>

# **Testing**

### **Validator Testing**

*The code has been tested on <a href="http://pep8online.com/">PEP8 Online</a>*<br>
*One error appears on line 33, the line is too long. I tried to short the line, but Python is not happy with that and appeared 3 more errors, so i kept the line how it is (see screenshot).*
<br>

![Error](/images/error.png "Error")<hr><br>

# **Development and Deployment**
<br>

The development environment used for this project was GitPod. <br>
To track the development stage and handle version control regular commits and pushes to GitHub has been conducted.<br>
The GitPod environment was created using a template provided by Code Institute.<br><br>
The live version was deployed using <a href="https://heroku.com/">Heroku</a><br><br>

### **Steps taken to deploy the project via CLI**
<br>

<ul>
<li>Access <a href="https://heroku.com/">Heroku</a></li>
<li>Login or Create an account if necessary.</li>
<li>Click "New" button on Heroku Dashboard and after select "Create new app".</li>
<li>Write the name for your app and select your region, after click "Create App".</li>
<li>In the settings tab of your new app, create a config var</li>
<ul><li>Name is: PORT and value is: 8000</li></ul>
<li>Create two buildpacks, the first have to be Python and second have to be Nodejs.</li>
</ul><br><hr>

### **In order to deploy the project via Heroku CLI, you have to follow the next steps**
<br>
<ul>
<li>Login to Heroku on GitPod Project and enter your details.</li>
<ul><li>command: heroku login -i</li></ul>
<li>Get your app name from Heroku.</li>
<ul><li>command: heroku apps</li></ul>
<li>Set the Heroku remote (Replace app_name with your actual app name).</li>
<ul><li>command: heroku git:remote app_name</li></ul>
<li>Add, commit and push to GitHub.</li>
<ul><li>command: git add . && git commit -m "Deploy to Heroku via CLI"</li></ul>
<li>Push to both, GitHub and Heroku.</li>
<ul><li>command: git push origin main</li>
<li> command: git push heroku main</li></ul><br>
After these steps the application was deployed to <a href="https://snake-game-sbn.herokuapp.com/">snake-game-sbn.herokuapp.com</a></ul><hr><br>

# **Credits**

### **For code inspiration, help and advice**
<br>

<ul>
<li><a href="https://github.com/sbnn3/love-sandwiches">Code Institute Essential Project - Love Sandwiches</a> - for inspiration and understanding on how to develop the project.</li>
<li><a href="https://codeinstitute.net/">Code Institute</a> - for all course material leading up to this project.</li>
<li><a href="https://www.youtube.com/watch?v=M_npdRYD4K0">Youtube Tutorial</a> -  for inspiration and better understanding of steps that i have to take to develop the Snake Project.</li>
<li><a href="https://www.youtube.com/watch?v=rbasThWVb">Youtube Tutorial</a> -  for inspiration and better understanding of steps that i have to take to develop the Snake Project.</li>
</ul><hr><br>

# **Acknowledgment**
<br>

*Martina Terlevic - My mentor at Code Institute for permanently support and feedback.*<br>
*Code Institute Tututor Team - For help during the lessons and challenges*<br>
