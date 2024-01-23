<div style="display: flex; justify-content: space-between; align-items: center;">
  <div style="width: 30%; text-align: center;">
    <p>Benjamin Schreiber</p>
  </div>
  <div style="width: 30%; text-align: center;">
    <p>Milestone 1</p>
  </div>
  <div style="width: 30%; text-align: center;">
    <p>Monday, January 22</p>
  </div>
</div>

**<p style="text-align: center">Team Name: BS-DS-ST-DF-PollPall</p>**

**For this milestone, I will provide what key tools, technologies, and the process model used for this
course project. Below, are all 3 of those, divided into different sections to provide a structured layout
of the plan as of now:**

***<u>Key Tools</u>***:

* Visual Studio Code, IDE.
    * Visual Studio Code is a great lightweight IDE that is perfect for our stack. We have decided to not fully integrate into any IDE environment (for example, Visual Studio) to allow developers to choose whatever environment they want. Our project should be able to be ran from command line, vim, etc. We will do this by using virtual environments, like venv in python or node in JavaScript.

* Docker, containerization
    * Docker will allow us to host a database without the trouble of setting it up on our own environment.

* GitHub, project management suite && VCS
    * GitHub provides a great SCRUM board that we will use throughout the project to create tasks. It also hosts our version control, Git, and will allow us to create a New Branch -> Pull Request -> Review -> Merge development flow.

* Swagger, documentation
    * Our project uses a REST API. Swagger allows us to not have to use some tool like PostMan (or even Curl if you're l33t), and have a universal tool to authenticate, and create HTTP requests.

* JSDoc, Black Formatter
    * JSDoc is a specific way to write JavaScript code using documentation to typehint. We don't like TypeScript because its verboes and gross. Then, the Black Formatter for python will make sure our code looks the same throughout commits without us having to spend any thought on it, as its automatic.



***<u>Technologies</u>***:

* React (JavaScript, HTML)
    * We have decided to use the React-suite for our front end development. We feel that functional-component based react is a great way to write clean frontends, and is also one of the most used JavaScript frameworks out there. Some people call React slow, but in reality, we're doing web dev, and if "slow" adds an extra 0.01 seconds to website load time, the user won't care.

* Tailwind
    * Writing CSS is overrated. Tailwind is great, because we don't have to deal with any CSS code, and can just use the built in classes tailwind provides for just about everything.

* Google Material Design
    * For this project, we really want to not write a bunch of front end code, because none of us consider ourselves graphic designers. Google Material Design is a library for React, that gives us tons of components, so we spend less time writing JavaScript and more time making the front end.

* Django (Python)
    * Since we all have some experience in Python, Django was a natural choice for our REST API. Django is great because it is a heavy weight REST framework, implementing an ORM. This makes database calls non-existant, as we simply configure a file and then use their object-based api to do any CRUD operations to our database. Further, Django allows us to write some very lightweight code. If we had an object we wanted to create, read, update, destroy, the entire code for that is a two lines: a class declaration, and an extension of a Django built-in. Further, any authentication is as simple as adding an override. Django is great!

* SignalR 
    * For our prompt, we need a more advanced connection between server and client than a standard REST API, which is one way (client -> server -> client). We need a client to be able to listen for updates from the server, and the server to listen for updates from a client. For this, we decided to use SignalR. SignalR is great because its an Azure service, and we can import the libraries for both Python and JavaScript to call it. We decided on this instead of implementing WebSockets ourselves to make sure we make the deadline for the project, and really spend the most time creating the project instead of the tools involved.

* MongoDB
    * Our server is going to be handling a LOT of read write operations when a session is made (each user needs to be tied to a session). We have two options: cache them in memory, or store them in a fast database. We think storing in memory isn't good for expansion, so we are choosing to use MongoDB, a NoSQL non-relational database. A new session will be some generated UUID, and each user will be tied to that session (Key, Value).


***<u>Process Model</u>***:

**The process model used here will be the Spiral model**

We want to work in phases, and then test those phases meticuously before merging them to main. The spiral model is exactly this.

* We can add more features with the spiral model whenever we want. Our base app will be very bare, just a proof of concept. If we finish early, what if we want to add more? Better UI? More advanced features? The spiral model allows for this.

* We like testing. All of our code will ideally be unit tested. The spiral model allows us to test in phases. For example, if a phase was to allow the server to store sessions, and then end sessions, we need to write tests to make sure that works, before going to the next phase.


We are aware of the drawbacks of the model

* We think time spent testing and analyzing each version is time well spent. The spiral model lets us aim low for our first iteration of the project, and we really want a strong base before we add on to it.

**This is what I think are the appropriate tools, technologies and the model that is necessary for me to
get the job done as I envisioned it (for now).**