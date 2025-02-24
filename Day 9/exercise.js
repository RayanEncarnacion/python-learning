const student_scores = {
    Harry: 88,
    Ron: 78,
    Hermione: 95,
    Draco: 75,
    Neville: 60,
};

function get_grade(score) {
    if (score > 90) return "Outstanding";
    if (score > 80) return "Exceeds Expectations";
    if (score > 70) return "Acceptable";
    else return "Fail";
}

const student_grades = Object.entries(student_scores).reduce(
    (acc, [student, score]) => {
        acc[student] = get_grade(score);
        return acc;
    },
    {}
);

/* 
    ! The logic to get the grade from the score can be extracted to a function for better readability
    function add_grade_to_student(acc, [student, score]) {
        acc[student] = get_grade(score);
        return acc;
    }

    student_grades = Object.entries(student_scores).reduce(add_grade_to_student, {});

    ! More readable version (but less efficient) avoiding the reduce method (hard to understand by some devs)
    student_grades = Object.fromEntries(
        Object.entries(student_scores).map(([student, score]) => [student, get_grade(score)])
    );
*/
