const target = document.getElementById('target');
const gameContainer = document.getElementById('game-container');

let score = 0;

function moveTarget() {
    const maxX = gameContainer.clientWidth - target.clientWidth;
    const maxY = gameContainer.clientHeight - target.clientHeight;
    const randomX = Math.floor(Math.random() * maxX);
    const randomY = Math.floor(Math.random() * maxY);

    target.style.left = randomX + 'px';
    target.style.top = randomY + 'px';
}

target.addEventListener('click', () => {
    score++;
    moveTarget();
});

moveTarget();

setInterval(() => {
    moveTarget();
}, 1000);

const scoreDisplay = document.createElement('p');
scoreDisplay.innerText = 'Score: 0';
document.body.appendChild(scoreDisplay);

setInterval(() => {
    scoreDisplay.innerText = 'Score: ' + score;
}, 100);
