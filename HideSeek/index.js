let seek = 0;
let streak = 0;
let highscore = 0;

function changeStreak(found){
    if(found == true){
        streak = 0;
    }
    else{
        streak += 1;
        if (streak > highscore){
            highscore = streak
        }
    }return streak;
}

document.getElementById("tree").onclick = function(){
    seek = Math.floor(Math.random() * 3) + 1;
    if (seek == 1){
        document.getElementById("results").innerHTML = "You've been found";
        changeStreak(true);
        document.getElementById("streak").innerHTML = "Streak: " + streak;
    }
    else{
        document.getElementById("results").innerHTML = "You got lucky this time";
        changeStreak(false);
        document.getElementById("streak").innerHTML = "Streak: " + streak;
        document.getElementById("highscore").innerHTML = "Highscore: " + highscore;
    }
}

document.getElementById("bush").onclick = function(){
    seek = Math.floor(Math.random() * 3) + 1;
    if (seek == 2){
        document.getElementById("results").innerHTML = "You've been found";
        changeStreak(true);
        document.getElementById("streak").innerHTML = "Streak: " + streak;
    }
    else{
        document.getElementById("results").innerHTML = "You got lucky this time";
        changeStreak(false);
        document.getElementById("streak").innerHTML = "Streak: " + streak;
        document.getElementById("highscore").innerHTML = "Highscore: " + highscore;
    }
}

document.getElementById("swings").onclick = function(){
    seek = Math.floor(Math.random() * 3) + 1;
    if (seek == 3){
        document.getElementById("results").innerHTML = "You've been found";
        changeStreak(true);
        document.getElementById("streak").innerHTML = "Streak: " + streak;
    }
    else{
        document.getElementById("results").innerHTML = "You got lucky this time";
        changeStreak(false);
        document.getElementById("streak").innerHTML = "Streak: " + streak;
        document.getElementById("highscore").innerHTML = "Highscore: " + highscore;
    }
}