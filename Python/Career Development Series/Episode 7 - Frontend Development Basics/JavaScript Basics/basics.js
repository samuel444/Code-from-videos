document.writeln('Hello');

var name = 'Sam';
document.writeln('My name is ' + name);


function animal(name,noise,species) {
    document.writeln(name + ' is a ' + species + ' that goes ' + noise);
}
animal('Poppy','Bark','Dog');


namesArray = new Array('Sophie','Sam','Dan','Hannah');
if (namesArray[2] == 'Sophie') {
    document.writeln('Sophie is in the list at index 2');
}
else if (namesArray.includes('Sophie')) {
    document.writeln('Sophie is in the list but not at index 2');
}
else {
    document.writeln('Sophie is not in the list');
}


var i = 0
while (i < 30) {
    document.writeln('o');
    i += 1;
}


for (names in namesArray) {
    document.writeln(namesArray[names]);
}


var name = prompt('What is your name?');

alert('This is an alert, press ok');

var answer = confirm('This is a confirm message, you either ok or cancel');
document.writeln(answer);

setTimeout('alert("Press ok!")',5000);

const textbox = document.getElementById('textbox');
textbox.style.backgroundColor = 'blue';
textbox.style.content = 'hello world';


const button1 = document.getElementById("myButton1");
button1.addEventListener("click", function() {
    textbox.style.backgroundColor = 'orange';
});
  
const button2 = document.getElementById("myButton2");
button2.addEventListener("click", function() {
    const newParagraph = document.createElement("p");
    newParagraph.textContent = "You pressed the button";
    document.body.appendChild(newParagraph);
});

const button3 = document.getElementById("myButton3");
button3.addEventListener("click", function() {
    window.location.href = 'https://www.youtube.com';
});
