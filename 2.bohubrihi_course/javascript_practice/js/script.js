// Project Task List
// --------------------------------

// Define UI element
// let form = document.querySelector("#task_form");
// let taskList = document.querySelector("ul");
// let clearBtn = document.querySelector("#clear_task_btn");
// let filter = document.querySelector("#task_filter");
// let taskInput = document.querySelector("#new_task");

// // Define event listeners
// form.addEventListener("submit", addTask);
// taskList.addEventListener("click", removeTask);
// clearBtn.addEventListener("click", clearTask);
// filter.addEventListener("keyup", filterTask);
// document.addEventListener("DOMContentLoaded", getTasks);

// // Define functions
// // Add Task
// function addTask(e) {
//   if (taskInput.value === "") {
//     alert("Add a task!");
//   } else {
//     // Create li element
//     let li = document.createElement("li");
//     li.appendChild(document.createTextNode(taskInput.value + " "));
//     let link = document.createElement("a");
//     link.setAttribute("href", "#");
//     link.innerHTML = "x";
//     li.appendChild(link);
//     taskList.appendChild(li);

//     storeTaskInLocalStorage(taskInput.value);

//     taskInput.value = "";
//   }
//   e.preventDefault();
// }

// // Remove Task
// function removeTask(e) {
//   if (e.target.hasAttribute("href")) {
//     if (confirm("Are you sure?")) {
//       let ele = e.target.parentElement;
//       ele.remove();
//       //console.log(ele);
//       removeFromLS(ele);
//     }
//   }
// }

// // Clear Task
// function clearTask(e) {
//   //taskList.innerHTML = "";

//   // Faster
//   while (taskList.firstChild) {
//     taskList.removeChild(taskList.firstChild);
//   }
//   localStorage.clear();
// }

// // Filter Task
// function filterTask(e) {
//   let text = e.target.value.toLowerCase();

//   document.querySelectorAll("li").forEach((task) => {
//     let item = task.firstChild.textContent;
//     if (item.toLowerCase().indexOf(text) != -1) {
//       task.style.display = "block";
//     } else {
//       task.style.display = "none";
//     }
//   });
// }

// // Store in Local Storage
// function storeTaskInLocalStorage(task) {
//   let tasks;
//   if (localStorage.getItem("tasks") === null) {
//     tasks = [];
//   } else {
//     tasks = JSON.parse(localStorage.getItem("tasks"));
//   }
//   tasks.push(task);

//   localStorage.setItem("tasks", JSON.stringify(tasks));
// }

// function getTasks() {
//   let tasks;
//   if (localStorage.getItem("tasks") === null) {
//     tasks = [];
//   } else {
//     tasks = JSON.parse(localStorage.getItem("tasks"));
//   }

//   tasks.forEach((task) => {
//     let li = document.createElement("li");
//     li.appendChild(document.createTextNode(task + " "));
//     let link = document.createElement("a");
//     link.setAttribute("href", "#");
//     link.innerHTML = "x";
//     li.appendChild(link);
//     taskList.appendChild(li);
//   });
// }

// function removeFromLS(taskItem) {
//   let tasks;
//   if (localStorage.getItem("tasks") === null) {
//     tasks = [];
//   } else {
//     tasks = JSON.parse(localStorage.getItem("tasks"));
//   }

//   let li = taskItem;
//   li.removeChild(li.lastChild); // <a>x</a>'

//   tasks.forEach((task, index) => {
//     if (li.textContent.trim() === task) {
//       tasks.splice(index, 1);
//     }
//   });

//   localStorage.setItem("tasks", JSON.stringify(tasks));
// }

// Project Book List
// -----------------------------

// Get the UI elements
// let form = document.querySelector("#book-form");
// let booklist = document.querySelector("#book-list");

// // Book Class
// class Book {
//   constructor(title, author, isbn) {
//     this.title = title;
//     this.author = author;
//     this.isbn = isbn;
//   }
// }

// // UI Class
// class UI {
//   static addToBooklist(book) {
//     let list = document.querySelector("#book-list");
//     let row = document.createElement("tr");
//     row.innerHTML = `
//         <td>${book.title}</td>
//         <td>${book.author}</td>
//         <td>${book.isbn}</td>
//         <td><a href='#' class="delete">X</a></td>`;

//     list.appendChild(row);
//   }

//   static clearFields() {
//     document.querySelector("#title").value = "";
//     document.querySelector("#author").value = "";
//     document.querySelector("#isbn").value = "";
//   }

//   static showAlert(message, className) {
//     let div = document.createElement("div");
//     div.className = `alert ${className}`;
//     div.appendChild(document.createTextNode(message));
//     //console.log(div);
//     let container = document.querySelector(".container");
//     let form = document.querySelector("#book-form");
//     container.insertBefore(div, form);

//     setTimeout(() => {
//       document.querySelector(".alert").remove();
//     }, 3000);
//   }

//   static deleteFromBook(target) {
//     if (target.hasAttribute("href")) {
//       target.parentElement.parentElement.remove();
//       Store.removeBook(
//         target.parentElement.previousElementSibling.textContent.trim()
//       );
//       UI.showAlert("Book Removed!", "success");
//     }
//   }
// }

// // Local Storage Class
// class Store {
//   static getBooks() {
//     let books;
//     if (localStorage.getItem("books") === null) {
//       books = [];
//     } else {
//       books = JSON.parse(localStorage.getItem("books"));
//     }
//     return books;
//   }

//   static addBook(book) {
//     let books = Store.getBooks();
//     books.push(book);

//     localStorage.setItem("books", JSON.stringify(books));
//   }

//   static displayBooks() {
//     let books = Store.getBooks();

//     books.forEach((book) => {
//       UI.addToBooklist(book);
//     });
//   }

//   static removeBook(isbn) {
//     let books = Store.getBooks();

//     books.forEach((book, index) => {
//       if (book.isbn === isbn) {
//         books.splice(index, 1);
//       }
//     });

//     localStorage.setItem("books", JSON.stringify(books));
//   }
// }

// // Add Event Listener
// form.addEventListener("submit", newBook);
// booklist.addEventListener("click", removeBook);
// document.addEventListener("DOMContentLoaded", Store.displayBooks());

// // Define functions

// function newBook(e) {
//   let title = document.querySelector("#title").value,
//     author = document.querySelector("#author").value,
//     isbn = document.querySelector("#isbn").value;

//   if (title === "" || author === "" || isbn === "") {
//     UI.showAlert("Please fill all the fields!", "error");
//   } else {
//     let book = new Book(title, author, isbn);

//     UI.addToBooklist(book);

//     UI.clearFields();

//     UI.showAlert("Book Added!", "success");

//     Store.addBook(book);
//   }

//   e.preventDefault();
// }

// function removeBook(e) {
//   UI.deleteFromBook(e.target);
//   e.preventDefault();
// }

// Project: Github Finder
// -----------------------------
let searchBtn = document.querySelector("#searchBtn");
let searchUser = document.querySelector("#searchUser");
let ui = new UI();

searchBtn.addEventListener("click", (e) => {
  let userText = searchUser.value;
  if (userText != "") {
    // Fetch API
    fetch(`https://api.github.com/users/${userText}`)
      .then((result) => result.json())
      .then((data) => {
        //console.log(data);
        if (data.message == "Not Found") {
          // Show Alert
          ui.showAlert("User not Found!", "alert alert-danger");
        } else {
          //Show Profile
          ui.showProfile(data);
        }
      });
  } else {
    // Clear Profile
    ui.clearProfile();
  }
});
