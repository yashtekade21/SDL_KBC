const questions = [
    ["The International Literacy Day is observed on ",
        "Sep 8", "Nov 28", "May 2", "Sep 22", 1],

    ["The language of Lakshadweep, a Union Territory of India, is ",
        "Hindi", "Marathi", "Malayalam", "Telugu", 3],

    ["Which day is observed as the World Standards Day? ",
        "Jun 8", "Aug 2", "Oct 14", "Nov 15", 3],

    ["Bahubali festival is related to ", "Hinduism",
        "Islam", "Buddhism", "Jainism", 4],

    ["Who is the author of the epic 'Meghdoot'? ",
        "Vishakadatta", "Valmiki", "Banabhatta", "Kalidas", 4],

    ["Van Mahotsav was started by ", "Maharshi Karve",
        "Bal Gangadhar Tilak", "K.M. Munshi", "Sanjay Gandhi", 3],

    ["The Krithi system was perfected and Carnatic music was given by ",
        "Arunagirinathan", "Purandaradasa", "Shyama Shastri", "Swati Tirunal", 4],

    ["Writers Building is the headquarters of ", "The Times of India Group",
        "All India Writers Association", "West Bengal Government", "Press Trust of India", 4],

    ["The Konark Temple is dedicated to ",
        "Vishnu", "Shiva", "Krishna", "Sun-God", 4],

    ["The 227-year-old 'Nawab Saheb Ki Haveli' is located at ",
        "Hyderabad", "Jaipur", "New Delhi", "Agra", 2],

    ["Which of the following Academy is responsible for fostering the development of dance, drama, and music in India? ",
        "Lalit Kala Academy", "Sahitya Academy", "National School of Drama", "Sangeet Academy", 4],

    ["In which of the following countries has India not organised 'India Festival'? ",
        "Russia", "Japan", "France", "West Germany", 4],

    ["The Indian National Calendar is based on ",
        "Christian era", "Saka era", "Vikram era", "Hiji era", 2],

    ["The abbreviation 'fob' stands for ", "Free on Board",
        "Free of Bargain", "Fellow of Britain", "None of these", 1],

    ["Which British Army unit was given the motto 'Primus in Indis' because it was the first to serve in India? ",
        "41st (Welsh) Regiment of Foot", "1st Coldstream Guards", "5th Light Infantry", "39th Regiment of Foot", 4],
];

const prizeMoney = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000,
    160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000];

let currentQuestionIndex = 0;
let totalPrizeWon = 0;
let lifelinesUsed = { fiftyFifty: false, flipQuestion: false, askAudience: false, twoAttempts: false };
let attemptCount = 1;
let attemptedQuestions = new Set(); // Track attempted questions

function loadQuestion(index) {
    // Check if all questions have been attempted
    if (attemptedQuestions.size === questions.length) {
        document.getElementById('result').innerText = "Congratulations! You've completed the quiz and won ₹" + totalPrizeWon;
        return;
    }

    // Skip to next unattempted question if the current index has been attempted
    while (attemptedQuestions.has(index) && attemptedQuestions.size < questions.length) {
        index++;
        if (index >= questions.length) {
            index = 0; // Reset to start
        }
    }

    // Set the question number and prize amount
    document.getElementById('questionNumber').innerText = `Question ${index + 1} for ₹${prizeMoney[index]}`;
    document.getElementById('questionText').innerText = questions[index][0];
    document.getElementById('option1Text').innerText = questions[index][1];
    document.getElementById('option2Text').innerText = questions[index][2];
    document.getElementById('option3Text').innerText = questions[index][3];
    document.getElementById('option4Text').innerText = questions[index][4];

    // Reset all options (uncheck radio buttons and re-enable)
    document.querySelectorAll('input[name="option"]').forEach(radio => {
        radio.checked = false;
        radio.disabled = false; // Re-enable all options
    });

    // Clear previous result
    document.getElementById('result').innerText = "";
}

function getSelectedOption() {
    const selectedRadio = document.querySelector('input[name="option"]:checked');
    return selectedRadio ? parseInt(selectedRadio.value) : null;
}

function checkAnswer() {
    const selectedOption = getSelectedOption();
    if (selectedOption === null) {
        alert("Please select an answer!");
        return;
    }

    const correctOption = questions[currentQuestionIndex][5];
    if (selectedOption === correctOption) {
        document.getElementById('result').innerText = "Correct Answer!";
        totalPrizeWon = prizeMoney[currentQuestionIndex];
        attemptedQuestions.add(currentQuestionIndex); // Mark current question as attempted
        attemptCount = 1; // Reset attempt count for the next question

        // Check if it's the last question or ₹10,000,000 question
        if (currentQuestionIndex === questions.length - 1 || totalPrizeWon === 10000000) {
            // Redirect to win.html if the last question was answered correctly
            window.location.href = `win.html?amount=${totalPrizeWon}`;
            return;
        }

        currentQuestionIndex++;  // Move to the next question
        // Load the next question after a short delay
        setTimeout(() => loadQuestion(currentQuestionIndex), 1000);
    } else {
        attemptCount--; // Decrement attempt count
        if (attemptCount > 0) {
            alert(`Wrong answer. You have ${attemptCount} attempt(s) left.`);
            // Reset the question without redirecting
            setTimeout(() => loadQuestion(currentQuestionIndex), 1000);
        } else {
            document.getElementById('result').innerText = `Wrong Answer. Game Over! You won ₹${totalPrizeWon}.`;
            // Redirect to win.html after game over
            window.location.href = `win.html?amount=${totalPrizeWon}`;
        }
    }
}


document.getElementById('submitAnswer').addEventListener('click', checkAnswer);

// Lifelines
document.getElementById('fiftyFifty').addEventListener('click', () => {
    if (lifelinesUsed.fiftyFifty) return;
    lifelinesUsed.fiftyFifty = true;
    markLifelineUsed('fiftyFifty'); // Mark as used

    const correctOption = questions[currentQuestionIndex][5];
    const optionsToHide = [1, 2, 3, 4].filter(opt => opt !== correctOption).sort(() => 0.5 - Math.random()).slice(0, 2);

    optionsToHide.forEach(option => {
        document.getElementById('option' + option).disabled = true;
        document.getElementById('option' + option + 'Text').classList.add('hidden');
    });
});

document.getElementById('flipQuestion').addEventListener('click', () => {
    if (lifelinesUsed.flipQuestion) return;
    lifelinesUsed.flipQuestion = true;
    markLifelineUsed('flipQuestion'); // Mark as used

    // Increment to next question and ensure it's unattempted
    currentQuestionIndex++;
    loadQuestion(currentQuestionIndex);
});

document.getElementById('askAudience').addEventListener('click', () => {
    if (lifelinesUsed.askAudience) return;
    lifelinesUsed.askAudience = true;
    markLifelineUsed('askAudience'); // Mark as used

    const correctOption = questions[currentQuestionIndex][5];
    alert(`Audience suggests the correct option is: ${correctOption}`);
});

document.getElementById('twoAttempts').addEventListener('click', () => {
    if (lifelinesUsed.twoAttempts) return;
    lifelinesUsed.twoAttempts = true;
    markLifelineUsed('twoAttempts'); // Mark as used
    attemptCount = 2; // Reset attempt count
    alert("You now have 2 attempts for this question!");
});

// Function to mark a lifeline as used
function markLifelineUsed(lifeline) {
    const button = document.getElementById(lifeline);
    button.classList.add('used');
    button.disabled = true; // Disable the button after use
}

// Initial load
loadQuestion(currentQuestionIndex);
