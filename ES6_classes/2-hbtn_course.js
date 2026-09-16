import { array, number } from "yargs";

export default class HolbertonCourse{
    constructor(name, length, students){
        this._name = String(name);
        this._length = Number(length);
        this._students = Array.isArray(students) ? students : [];
        if (typeof name !== 'string') {
            throw new TypeError('Name must be a string');
        }
        if (typeof length !== 'number') {
            throw new TypeError('Length must be a number');
        }
        if (!Array.isArray(students)) {
            throw new TypeError('Students must be an array');
        }
    }
}