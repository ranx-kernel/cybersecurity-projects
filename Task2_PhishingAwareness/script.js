// script.js

function checkAnswer(answer){

    const result = document.getElementById("result");

    if(answer === "correct"){

        result.innerHTML =
        "✅ Correct! Urgent requests for passwords are common phishing tactics.";

        result.style.color = "lightgreen";
    }

    else{

        result.innerHTML =
        "❌ Wrong Answer! Try Again.";

        result.style.color = "red";
    }

}