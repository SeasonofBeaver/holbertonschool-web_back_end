// counts all students in the CSV file and prints out the Number and the Name of the students.

const fs = require('fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf8');
        const lines = data.split('\n').filter((line) => line.trim() !== ''); // Remove empty lines
        if (lines.length === 0) throw new Error('Cannot load the database');

        const headers = lines[0].split(',');
        const students = lines.slice(1).map((line) => {
            const values = line.split(',');
            const student = {};
            headers.forEach((header, index) => {
                student[header] = values[index];
            });
            return student;
        });

        console.log(`Number of students: ${students.length}`);

        const fields = {};
        students.forEach((student) => {
            const field = student.field;
            if (field) {
                if (!fields[field]) {
                    fields[field] = [];
                }
                fields[field].push(student.firstname);
            }
        });

        for (const [field, names] of Object.entries(fields)) {
            console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }
    } catch (err) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
