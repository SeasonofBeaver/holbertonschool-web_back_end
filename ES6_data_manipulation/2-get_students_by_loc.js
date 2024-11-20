/* eslint-disable */
export default function getStudentsByLocation(StudentList, city) {
    if (typeof city !== 'string') {
        throw new TypeError("city must be a string.")
    }
    if (!Array.isArray(StudentList)) {
        throw new TypeError("StudentList must be an array.")
    }
    return StudentList.filter(student => student.location === city);
}