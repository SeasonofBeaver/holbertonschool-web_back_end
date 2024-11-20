/* eslint-disable */
export default function getStudentIdsSum(StudentList) {
    if (!Array.isArray(StudentList)) {
        throw new TypeError("StudentList must be an array.")
    }
    return StudentList.reduce((sum, student) => sum + student.id, 0);
}