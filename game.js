class AlgebraQuest {
    constructor() {
        this.player = {
            name: '',
            avatar: '',
            totalScore: 0,
            badges: [],
            completedLevels: []
        };
        
        this.currentGame = {
            grade: 0,
            questions: [],
            currentQuestion: 0,
            score: 0,
            correctAnswers: 0,
            startTime: 0,
            streak: 0,
            hintsUsed: 0
        };
        
        this.init();
    }
    
    init() {
        this.loadProgress();
        this.setupEventListeners();
        this.createStars();
        this.showScreen('welcomeScreen');
    }
    
    setupEventListeners() {
        document.querySelectorAll('.avatar-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.selectAvatar(e));
        });
        
        document.getElementById('playerName').addEventListener('input', (e) => {
            document.getElementById('startBtn').disabled = e.target.value.trim().length < 2;
        });
        
        document.getElementById('startBtn').addEventListener('click', () => this.startGame());
        
        document.querySelectorAll('.btn-level').forEach((btn, index) => {
            btn.addEventListener('click', () => {
                const grade = parseInt(btn.parentElement.dataset.grade);
                this.startLevel(grade);
            });
        });
        
        document.getElementById('submitBtn').addEventListener('click', () => this.submitAnswer());
        document.getElementById('answerInput').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.submitAnswer();
        });
        
        document.getElementById('hintBtn').addEventListener('click', () => this.showHint());
        document.getElementById('backBtn').addEventListener('click', () => this.showLevelScreen());
        document.getElementById('retryBtn').addEventListener('click', () => this.startLevel(this.currentGame.grade));
        document.getElementById('menuBtn').addEventListener('click', () => this.showLevelScreen());
        document.getElementById('nextLevelBtn').addEventListener('click', () => {
            const nextGrade = this.currentGame.grade + 1;
            if (nextGrade <= 8) {
                this.startLevel(nextGrade);
            }
        });
    }
    
    selectAvatar(e) {
        document.querySelectorAll('.avatar-btn').forEach(btn => btn.classList.remove('selected'));
        e.currentTarget.classList.add('selected');
        this.player.avatar = e.currentTarget.dataset.avatar;
    }
    
    startGame() {
        const name = document.getElementById('playerName').value.trim();
        if (name && this.player.avatar) {
            this.player.name = name;
            this.saveProgress();
            this.showLevelScreen();
        }
    }
    
    showLevelScreen() {
        document.getElementById('playerNameDisplay').textContent = this.player.name;
        document.getElementById('playerAvatar').textContent = this.player.avatar;
        document.getElementById('totalScore').textContent = this.player.totalScore;
        document.getElementById('badgeCount').textContent = this.player.badges.length;
        
        this.displayBadges();
        this.updateLevelCards();
        this.showScreen('levelScreen');
    }
    
    updateLevelCards() {
        document.querySelectorAll('.level-card').forEach(card => {
            const grade = parseInt(card.dataset.grade);
            if (this.player.completedLevels.includes(grade)) {
                card.classList.add('completed');
            }
        });
    }
    
    displayBadges() {
        const container = document.getElementById('badgesDisplay');
        container.innerHTML = '';
        
        if (this.player.badges.length === 0) {
            container.innerHTML = '<p style="color: #999;">Complete levels to earn badges!</p>';
        } else {
            this.player.badges.forEach(badge => {
                const badgeEl = document.createElement('div');
                badgeEl.className = 'badge';
                badgeEl.innerHTML = `${badge.icon}<div class="badge-name">${badge.name}</div>`;
                badgeEl.title = badge.description;
                container.appendChild(badgeEl);
            });
        }
    }
    
    startLevel(grade) {
        this.currentGame = {
            grade: grade,
            questions: this.generateQuestions(grade),
            currentQuestion: 0,
            score: 0,
            correctAnswers: 0,
            startTime: Date.now(),
            streak: 0,
            hintsUsed: 0
        };
        
        document.getElementById('currentGrade').textContent = `Grade ${grade}`;
        document.getElementById('gameAvatar').textContent = this.player.avatar;
        this.showScreen('gameScreen');
        this.displayQuestion();
        this.startTimer();
    }
    
    generateQuestions(grade) {
        const questions = [];
        const numQuestions = 10;
        
        for (let i = 0; i < numQuestions; i++) {
            questions.push(this.generateQuestion(grade, i));
        }
        
        return questions;
    }
    
    generateQuestion(grade, index) {
        const questionGenerators = {
            4: this.generateGrade4Question,
            5: this.generateGrade5Question,
            6: this.generateGrade6Question,
            7: this.generateGrade7Question,
            8: this.generateGrade8Question
        };
        
        return questionGenerators[grade].call(this, index);
    }
    
    generateGrade4Question(index) {
        const types = ['missing_number', 'simple_equation', 'pattern'];
        const type = types[index % types.length];
        
        if (type === 'missing_number') {
            const a = Math.floor(Math.random() * 20) + 1;
            const b = Math.floor(Math.random() * 20) + 1;
            const answer = a + b;
            return {
                text: `${a} + ___ = ${answer}`,
                answer: b,
                hint: `What do you need to add to ${a} to get ${answer}?`,
                visual: '🔢'
            };
        } else if (type === 'simple_equation') {
            const x = Math.floor(Math.random() * 15) + 1;
            const b = Math.floor(Math.random() * 10) + 1;
            const answer = x + b;
            return {
                text: `x + ${b} = ${answer}. What is x?`,
                answer: x,
                hint: `Subtract ${b} from both sides: x = ${answer} - ${b}`,
                visual: '✨'
            };
        } else {
            const start = Math.floor(Math.random() * 10) + 1;
            const step = Math.floor(Math.random() * 5) + 2;
            const missing = start + step * 3;
            return {
                text: `What comes next? ${start}, ${start + step}, ${start + step * 2}, ___`,
                answer: missing,
                hint: `Look at the difference between each number. They increase by ${step}.`,
                visual: '🔄'
            };
        }
    }
    
    generateGrade5Question(index) {
        const types = ['two_step', 'order_ops', 'variable_expression'];
        const type = types[index % types.length];
        
        if (type === 'two_step') {
            const x = Math.floor(Math.random() * 10) + 1;
            const a = Math.floor(Math.random() * 5) + 2;
            const b = Math.floor(Math.random() * 10) + 1;
            const answer = a * x + b;
            return {
                text: `${a}x + ${b} = ${answer}. What is x?`,
                answer: x,
                hint: `First subtract ${b} from both sides, then divide by ${a}.`,
                visual: '🎯'
            };
        } else if (type === 'order_ops') {
            const a = Math.floor(Math.random() * 5) + 2;
            const b = Math.floor(Math.random() * 5) + 2;
            const c = Math.floor(Math.random() * 10) + 1;
            const answer = a * b + c;
            return {
                text: `${a} × ${b} + ${c} = ?`,
                answer: answer,
                hint: `Remember PEMDAS! Multiply first: ${a} × ${b} = ${a * b}, then add ${c}.`,
                visual: '🧮'
            };
        } else {
            const x = Math.floor(Math.random() * 8) + 1;
            const a = Math.floor(Math.random() * 5) + 2;
            const b = Math.floor(Math.random() * 5) + 1;
            const answer = a * x + b;
            return {
                text: `If x = ${x}, what is ${a}x + ${b}?`,
                answer: answer,
                hint: `Replace x with ${x}: ${a} × ${x} + ${b}`,
                visual: '📊'
            };
        }
    }
    
    generateGrade6Question(index) {
        const types = ['inequality', 'ratio', 'expression_simplify'];
        const type = types[index % types.length];
        
        if (type === 'inequality') {
            const x = Math.floor(Math.random() * 10) + 1;
            const b = Math.floor(Math.random() * 10) + 1;
            const answer = x + b;
            return {
                text: `x + ${b} < ${answer + 5}. What is the largest whole number x can be?`,
                answer: x + 4,
                hint: `Subtract ${b} from both sides. x must be less than ${answer + 5 - b}.`,
                visual: '⚖️'
            };
        } else if (type === 'ratio') {
            const a = Math.floor(Math.random() * 5) + 2;
            const b = Math.floor(Math.random() * 5) + 2;
            const multiplier = Math.floor(Math.random() * 4) + 2;
            const answer = b * multiplier;
            return {
                text: `If ${a}:${b} = ${a * multiplier}:x, what is x?`,
                answer: answer,
                hint: `${a} was multiplied by ${multiplier} to get ${a * multiplier}. Do the same to ${b}.`,
                visual: '🎲'
            };
        } else {
            const a = Math.floor(Math.random() * 5) + 2;
            const b = Math.floor(Math.random() * 5) + 2;
            const answer = a + b;
            return {
                text: `Simplify: ${a}x + ${b}x = ?`,
                answer: answer,
                hint: `Combine like terms: (${a} + ${b})x = ${answer}x. Just enter ${answer}.`,
                visual: '🔍'
            };
        }
    }
    
    generateGrade7Question(index) {
        const types = ['multi_step', 'negative_numbers', 'linear'];
        const type = types[index % types.length];
        
        if (type === 'multi_step') {
            const x = Math.floor(Math.random() * 10) + 1;
            const a = Math.floor(Math.random() * 4) + 2;
            const b = Math.floor(Math.random() * 10) + 1;
            const c = Math.floor(Math.random() * 10) + 1;
            const answer = a * x + b + c;
            return {
                text: `${a}x + ${b} + ${c} = ${answer}. What is x?`,
                answer: x,
                hint: `First combine ${b} + ${c} = ${b + c}, then solve ${a}x + ${b + c} = ${answer}.`,
                visual: '🎪'
            };
        } else if (type === 'negative_numbers') {
            const x = Math.floor(Math.random() * 10) + 1;
            const a = Math.floor(Math.random() * 5) + 2;
            const b = Math.floor(Math.random() * 10) + 5;
            const answer = a * x - b;
            return {
                text: `${a}x - ${b} = ${answer}. What is x?`,
                answer: x,
                hint: `Add ${b} to both sides to get ${a}x = ${answer + b}, then divide by ${a}.`,
                visual: '➖'
            };
        } else {
            const m = Math.floor(Math.random() * 5) + 1;
            const x = Math.floor(Math.random() * 10) + 1;
            const b = Math.floor(Math.random() * 10) + 1;
            const answer = m * x + b;
            return {
                text: `If y = ${m}x + ${b} and x = ${x}, what is y?`,
                answer: answer,
                hint: `Substitute ${x} for x: y = ${m}(${x}) + ${b} = ${m * x} + ${b}`,
                visual: '📈'
            };
        }
    }
    
    generateGrade8Question(index) {
        const types = ['quadratic_simple', 'system', 'function'];
        const type = types[index % types.length];
        
        if (type === 'quadratic_simple') {
            const x = Math.floor(Math.random() * 8) + 2;
            const answer = x * x;
            return {
                text: `x² = ${answer}. What is x? (positive answer)`,
                answer: x,
                hint: `What number times itself equals ${answer}? Think of square roots.`,
                visual: '²'
            };
        } else if (type === 'system') {
            const x = Math.floor(Math.random() * 5) + 1;
            const y = Math.floor(Math.random() * 5) + 1;
            const sum = x + y;
            return {
                text: `x + y = ${sum} and x = ${x}. What is y?`,
                answer: y,
                hint: `Substitute x = ${x} into the equation: ${x} + y = ${sum}`,
                visual: '🔗'
            };
        } else {
            const input = Math.floor(Math.random() * 10) + 1;
            const a = Math.floor(Math.random() * 4) + 2;
            const b = Math.floor(Math.random() * 10) + 1;
            const answer = a * input + b;
            return {
                text: `If f(x) = ${a}x + ${b}, what is f(${input})?`,
                answer: answer,
                hint: `Replace x with ${input}: f(${input}) = ${a}(${input}) + ${b}`,
                visual: '🔢'
            };
        }
    }
    
    displayQuestion() {
        const q = this.currentGame.questions[this.currentGame.currentQuestion];
        document.getElementById('questionText').textContent = q.text;
        document.getElementById('visualAid').textContent = q.visual;
        document.getElementById('answerInput').value = '';
        document.getElementById('hintBox').classList.add('hidden');
        document.getElementById('feedback').classList.add('hidden');
        document.getElementById('answerInput').focus();
        
        const progress = ((this.currentGame.currentQuestion + 1) / this.currentGame.questions.length) * 100;
        document.getElementById('progressFill').style.width = progress + '%';
        document.getElementById('progressText').textContent = 
            `Question ${this.currentGame.currentQuestion + 1} of ${this.currentGame.questions.length}`;
        
        document.getElementById('currentScore').textContent = this.currentGame.score;
        document.getElementById('streak').textContent = this.currentGame.streak;
    }
    
    showHint() {
        const q = this.currentGame.questions[this.currentGame.currentQuestion];
        const hintBox = document.getElementById('hintBox');
        hintBox.textContent = '💡 ' + q.hint;
        hintBox.classList.remove('hidden');
        this.currentGame.hintsUsed++;
    }
    
    submitAnswer() {
        const userAnswer = parseFloat(document.getElementById('answerInput').value);
        const q = this.currentGame.questions[this.currentGame.currentQuestion];
        const feedback = document.getElementById('feedback');
        
        if (isNaN(userAnswer)) {
            feedback.textContent = '⚠️ Please enter a number!';
            feedback.className = 'feedback incorrect';
            feedback.classList.remove('hidden');
            return;
        }
        
        const isCorrect = Math.abs(userAnswer - q.answer) < 0.01;
        
        if (isCorrect) {
            const basePoints = 100;
            const streakBonus = this.currentGame.streak * 10;
            const hintPenalty = document.getElementById('hintBox').classList.contains('hidden') ? 0 : 20;
            const points = Math.max(basePoints + streakBonus - hintPenalty, 50);
            
            this.currentGame.score += points;
            this.currentGame.correctAnswers++;
            this.currentGame.streak++;
            
            feedback.textContent = `🎉 Correct! +${points} points! ${this.currentGame.streak > 1 ? '🔥 Streak: ' + this.currentGame.streak : ''}`;
            feedback.className = 'feedback correct';
            feedback.classList.remove('hidden');
            
            this.createStarAnimation();
        } else {
            this.currentGame.streak = 0;
            feedback.textContent = `❌ Not quite. The answer was ${q.answer}. Keep trying!`;
            feedback.className = 'feedback incorrect';
            feedback.classList.remove('hidden');
        }
        
        document.getElementById('currentScore').textContent = this.currentGame.score;
        document.getElementById('streak').textContent = this.currentGame.streak;
        
        setTimeout(() => {
            this.currentGame.currentQuestion++;
            if (this.currentGame.currentQuestion < this.currentGame.questions.length) {
                this.displayQuestion();
            } else {
                this.showResults();
            }
        }, 2000);
    }
    
    showResults() {
        this.stopTimer();
        
        const timeSpent = Math.floor((Date.now() - this.currentGame.startTime) / 1000);
        const accuracy = Math.round((this.currentGame.correctAnswers / this.currentGame.questions.length) * 100);
        
        document.getElementById('resultsAvatar').textContent = this.player.avatar;
        document.getElementById('finalScore').textContent = this.currentGame.score;
        document.getElementById('correctAnswers').textContent = 
            `${this.currentGame.correctAnswers}/${this.currentGame.questions.length}`;
        document.getElementById('accuracy').textContent = accuracy + '%';
        document.getElementById('timeSpent').textContent = timeSpent + 's';
        
        this.player.totalScore += this.currentGame.score;
        
        if (!this.player.completedLevels.includes(this.currentGame.grade)) {
            this.player.completedLevels.push(this.currentGame.grade);
        }
        
        const newBadge = this.checkForNewBadges();
        if (newBadge) {
            document.getElementById('newBadge').textContent = `🎊 New Badge Earned: ${newBadge.icon} ${newBadge.name}!`;
            document.getElementById('newBadge').classList.remove('hidden');
        } else {
            document.getElementById('newBadge').classList.add('hidden');
        }
        
        const encouragement = this.getEncouragement(accuracy);
        document.getElementById('encouragement').textContent = encouragement;
        
        if (accuracy >= 70 && this.currentGame.grade < 8) {
            document.getElementById('nextLevelBtn').classList.remove('hidden');
        } else {
            document.getElementById('nextLevelBtn').classList.add('hidden');
        }
        
        if (accuracy >= 90) {
            document.getElementById('resultsTitle').textContent = '🌟 Outstanding! 🌟';
        } else if (accuracy >= 70) {
            document.getElementById('resultsTitle').textContent = '🎉 Great Job! 🎉';
        } else {
            document.getElementById('resultsTitle').textContent = 'Keep Practicing! 💪';
        }
        
        this.saveProgress();
        this.showScreen('resultsScreen');
    }
    
    checkForNewBadges() {
        const badges = [
            { id: 'first_try', icon: '🌟', name: 'First Steps', description: 'Complete your first level', condition: () => this.player.completedLevels.length === 1 },
            { id: 'grade4_master', icon: '🎓', name: 'Grade 4 Master', description: 'Complete Grade 4', condition: () => this.currentGame.grade === 4 && !this.player.badges.find(b => b.id === 'grade4_master') },
            { id: 'grade5_master', icon: '📚', name: 'Grade 5 Master', description: 'Complete Grade 5', condition: () => this.currentGame.grade === 5 && !this.player.badges.find(b => b.id === 'grade5_master') },
            { id: 'grade6_master', icon: '🏅', name: 'Grade 6 Master', description: 'Complete Grade 6', condition: () => this.currentGame.grade === 6 && !this.player.badges.find(b => b.id === 'grade6_master') },
            { id: 'grade7_master', icon: '🥇', name: 'Grade 7 Master', description: 'Complete Grade 7', condition: () => this.currentGame.grade === 7 && !this.player.badges.find(b => b.id === 'grade7_master') },
            { id: 'grade8_master', icon: '👑', name: 'Algebra King', description: 'Complete Grade 8', condition: () => this.currentGame.grade === 8 && !this.player.badges.find(b => b.id === 'grade8_master') },
            { id: 'perfect', icon: '💯', name: 'Perfect Score', description: 'Get 100% accuracy', condition: () => this.currentGame.correctAnswers === this.currentGame.questions.length && !this.player.badges.find(b => b.id === 'perfect') },
            { id: 'speed', icon: '⚡', name: 'Speed Demon', description: 'Complete a level in under 2 minutes', condition: () => (Date.now() - this.currentGame.startTime) < 120000 && !this.player.badges.find(b => b.id === 'speed') },
            { id: 'streak', icon: '🔥', name: 'Hot Streak', description: 'Get 5 correct in a row', condition: () => this.currentGame.streak >= 5 && !this.player.badges.find(b => b.id === 'streak') }
        ];
        
        for (const badge of badges) {
            if (badge.condition() && !this.player.badges.find(b => b.id === badge.id)) {
                this.player.badges.push(badge);
                return badge;
            }
        }
        
        return null;
    }
    
    getEncouragement(accuracy) {
        if (accuracy === 100) {
            return "Perfect! You're a true algebra master! 🌟";
        } else if (accuracy >= 90) {
            return "Excellent work! You've got this! 🎉";
        } else if (accuracy >= 80) {
            return "Great job! You're doing really well! 👏";
        } else if (accuracy >= 70) {
            return "Good effort! Keep practicing and you'll improve! 💪";
        } else if (accuracy >= 60) {
            return "Nice try! Review the hints and try again! 📚";
        } else {
            return "Don't give up! Every mistake is a learning opportunity! 🌱";
        }
    }
    
    startTimer() {
        this.timerInterval = setInterval(() => {
            const elapsed = Math.floor((Date.now() - this.currentGame.startTime) / 1000);
            document.getElementById('timer').textContent = elapsed;
        }, 1000);
    }
    
    stopTimer() {
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
        }
    }
    
    createStars() {
        setInterval(() => {
            const star = document.createElement('div');
            star.className = 'star';
            star.textContent = ['⭐', '✨', '🌟'][Math.floor(Math.random() * 3)];
            star.style.left = Math.random() * 100 + '%';
            star.style.top = '-50px';
            document.querySelector('.stars').appendChild(star);
            
            setTimeout(() => star.remove(), 3000);
        }, 2000);
    }
    
    createStarAnimation() {
        for (let i = 0; i < 5; i++) {
            setTimeout(() => {
                const star = document.createElement('div');
                star.className = 'star';
                star.textContent = '⭐';
                star.style.left = Math.random() * 100 + '%';
                star.style.top = Math.random() * 50 + '%';
                document.querySelector('.stars').appendChild(star);
                
                setTimeout(() => star.remove(), 3000);
            }, i * 100);
        }
    }
    
    showScreen(screenId) {
        document.querySelectorAll('.screen').forEach(screen => {
            screen.classList.remove('active');
        });
        document.getElementById(screenId).classList.add('active');
    }
    
    saveProgress() {
        localStorage.setItem('algebraQuest', JSON.stringify(this.player));
    }
    
    loadProgress() {
        const saved = localStorage.getItem('algebraQuest');
        if (saved) {
            const data = JSON.parse(saved);
            if (data.name) {
                this.player = data;
            }
        }
    }
}

const game = new AlgebraQuest();
