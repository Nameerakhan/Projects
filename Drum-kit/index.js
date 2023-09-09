var numberOfButtons = document.querySelectorAll(".drum").length;
for(let i = 0;i<numberOfButtons;i++){
document.querySelectorAll("button")[i].addEventListener("click",function()
{
    this.style.color = "white";
    this.style.backgroundColor = "aqua"
    var buttonInerHTml = this.innerHTML;//constructor function
    makeSound(buttonInerHTml);
    buttonAnimation(buttonInerHTml);
    
document.addEventListener("keypress",function(event){
// alert("the key has been pressed");

makeSound(event.key);
buttonAnimation(event.key);
});

function makeSound(key){
    if (key =='w'){// either i can use switch case in here

        var audio1 = new Audio('sounds/tom-1.mp3');
        audio1.play();
        }
        else if(key == 'a'){ 
            var audio2 = new Audio('sounds/tom-2.mp3');
            audio2.play();
        }
        else if(key === 's'){ 
            var audio3 = new Audio('sounds/tom-3.mp3');
            audio3.play();
        }
        else if(key === 'd'){ 
            var audio4 = new Audio('sounds/tom-4.mp3');
            audio4.play();
        }
        else if(key === 'j'){ 
            var audio5 = new Audio('sounds/snare.mp3');
            audio5.play();
        }
        else if(key === 'k'){ 
            var audio6 = new Audio('sounds/crash.mp3');
            audio6.play();
        }
        else if(key === 'l'){ 
            var audio7 = new Audio('sounds/kick-bass.mp3');
            audio7.play();
        }
        else{
        console.log(key);
    }
}

// key('w','w')
});
}
function buttonAnimation(currentKey) {
     var activeButton = document.querySelector("."+currentKey);
    //  document.getElementsByClassName("pressed");
     activeButton.classList.add("pressed");
     setTimeout(function() {
         activeButton.classList.remove("pressed");},100);
     }


