/* eslint-disable */
export default function updateStudentGradeByCity(StudentList, city, newGrades) {
    if (!Array.isArray(StudentList)) {
        throw new TypeError("StudentList must be an array.")
    }
    return StudentList
        .filter(student => student.location === city)
        .map(student => {
            const gradeObject = newGrades.find(grade => grade.studentId === student.id);

            return {
                ...student,
                grade: gradeObject ? gradeObject.grade : 'N/A',
            };
        });
}