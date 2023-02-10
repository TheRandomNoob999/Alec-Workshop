let totalWacked = 0;
let looping = false;

function setUp(){
    document.getElementById("button1").style.visibility = "hidden";
    document.getElementById("button2").style.visibility = "hidden";
    document.getElementById("button3").style.visibility = "hidden";
    document.getElementById("button4").style.visibility = "hidden";
    document.getElementById("button5").style.visibility = "hidden";
    document.getElementById("button6").style.visibility = "hidden";
    document.getElementById("start").style.visibility = "visible";
    document.getElementById("title").style.visibility = "visible";
    document.getElementById("title2").style.visibility = "visible";
}

function clicked(buttonID){
    document.getElementById(buttonID).style.visibility = "hidden";
    totalWacked += 1;
    if(totalWacked == 10){
        looping = false;
        setUp();
    }
}

function spawnMole(){
    let random = Math.floor(Math.random() * 6) + 1;
    let buttonID = "button" + random;
    if (document.getElementById(buttonID).style.visibility == "visible"){
        spawnMole()
    }
    else{
        document.getElementById(buttonID).style.visibility = "visible";
    }
}

function failSave(){
    if (looping == true){
        looping = false;
        setUp();
    }
}

function loop(){
    totalWacked = 0;
    setTimeout(spawnMole, ((Math.random() * 6) + 2) * 1000);
    setTimeout(spawnMole, ((Math.random() * 5) + 3) * 1000);
    setTimeout(spawnMole, ((Math.random() * 4) + 3) * 1000);
    setTimeout(spawnMole, ((Math.random() * 2) + 1) * 1000);
    setTimeout(spawnMole, ((Math.random() * 2) + 2) * 1000);
    setTimeout(spawnMole, ((Math.random() * 6) + 2) * 1000);
    setTimeout(spawnMole, ((Math.random() * 5) + 4) * 1000);
    setTimeout(spawnMole, ((Math.random() * 4) + 3) * 1000);
    setTimeout(spawnMole, ((Math.random() * 3) + 2) * 1000);
    setTimeout(spawnMole, (Math.random() * 3) * 1000);
    setTimeout(failSave, 25000)
}

function start(){
    document.getElementById("start").style.visibility = "hidden";
    document.getElementById("title").style.visibility = "hidden";
    document.getElementById("title2").style.visibility = "hidden";
    
    looping = true;
    loop();
}
document.getElementById("start").onclick = function(){
    start();
}

document.getElementById("button1").onclick = function(){
    clicked("button1")
}
document.getElementById("button2").onclick = function(){
    clicked("button2")
}
document.getElementById("button3").onclick = function(){
    clicked("button3")
}
document.getElementById("button4").onclick = function(){
    clicked("button4")
}
document.getElementById("button5").onclick = function(){
    clicked("button5")
}
document.getElementById("button6").onclick = function(){
    clicked("button6")
}
setUp();