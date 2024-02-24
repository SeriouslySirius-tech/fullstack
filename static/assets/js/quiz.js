let intro = document.querySelector(".intro");
let logo = document.querySelector(".logoHeader");
let logoSpan = document.querySelectorAll(".logo");

window.addEventListener("DOMContentLoaded", ()=>{

    setTimeout(() => {
        logoSpan[0].classList.add("active");
    }, 1000);

    setTimeout(() => {
        logoSpan[1].classList.add("active");
        logoSpan[2].classList.add("active");
    }, 2000);


    setTimeout(() => {
        logoSpan[0].classList.remove("active");
        logoSpan[2].classList.remove("active");
        logoSpan[0].classList.add("fade");
        logoSpan[2].classList.add("fade");
        logoSpan[1].classList.add("fade");
    }, 3000);

    setTimeout(() => {
        logoSpan[1].classList.remove("active");
        
    }, 4000)

    setTimeout(() => {
        intro.style.top = "200vh";
    }, 5000)
})
    var questions = [
      "Question 1: What is the capital of France?",
      "Question 2: Who wrote 'Romeo and Juliet'?",
      "Question 3: What is the largest mammal?",
      "Question 4: In which year did World War I begin?",
      "Question 5: What is the chemical symbol for gold"
    ];

    var currentQuestionIndex = 0;

    function updateQuestion() {
      document.getElementById('frontFace').innerText = questions[currentQuestionIndex];
      document.getElementById('backFace').innerText = questions[(currentQuestionIndex + 1) % questions.length];
    }

    function handleCardClick(event) {
      const cardContainer = document.querySelector('.card-container');
      const card = document.querySelector('.card');

      const clickX = event.clientX - cardContainer.getBoundingClientRect().left;

      if (clickX > cardContainer.offsetWidth / 2) {
        // Right side clicked
        currentQuestionIndex = (currentQuestionIndex + 1) % questions.length;
      } else {
        // Left side clicked
        currentQuestionIndex = (currentQuestionIndex - 1 + questions.length) % questions.length;
      }

      card.classList.toggle('flip');
      setTimeout(() => {
        cardContainer.style.transform = card.classList.contains('flip') ? 'rotateY(180deg)' : 'rotateY(0deg)';
        updateQuestion();
      }, 250); // Wait for half of the flip animation before updating content
    }
    
    updateQuestion(); // Initialize with the first question
