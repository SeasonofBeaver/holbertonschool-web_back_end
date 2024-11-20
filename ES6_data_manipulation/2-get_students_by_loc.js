/* eslint-disable */
export default function getStudentsByLocation(StudentList, city) {
    if (typeof city !== 'string') {
        throw new TypeError("city must be a string.")
    }
    if (!Array.isArray(studentList)) {
        throw new TypeError("StudentList must be an array.")
    }
    return list.filter(student => student.location === city);
}