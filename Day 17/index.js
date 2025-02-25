import "./quizz_questions"

class QuizzGame {
    score = 0
    questions = []

    constructor(questions) {
        this.questions = questions
    }

    printQuestionsSeparator(index) {
        console.log('\n' * (index > 0 ? 2 : 1))
    }

    getAnswer(index, question) {
        return prompt(`Q.${index} - ${question}`).trim().toLowerCase() === 'true'
    }

    processAnswer(answer, correctAnswer) {
        if (answer === correctAnswer) {
            this.score += 1
            console.log("You got it right!")
        } else {
            console.log("That's wrong.")
        }

        console.log(`The correct answer was: ${correctAnswer}`)
    }

    printScore(answeredQuestion) {
        numOfQuestions = this.questions.length

        if (answeredQuestion < numOfQuestions)
            console.log(`Your current score is: {self.score}/${answeredQuestion}.`)
        else
            console.log(`\nGame completed! Your final score is: ${this.score}/${numOfQuestions}`)
    }

    start() {
        this.questions.forEach(({ text, correctAnswer }, idx) => {
            this.printQuestionsSeparator(idx)
            answer = this.getAnswer(idx + 1, text)
            this.processAnswer(answer, correctAnswer)
            this.printScore(idx + 1)
        })
    }
}

const game = new QuizzGame(questions)
game.start()

