export default function cleanSet(set, startString) {
    if (!(set instanceof Set) || typeof startString !== 'string' || startString.length === 0) {
        return '';
    }
    let result = '';
    for (const value of set) {
        if (value.startsWith(startString)) {
            result += value.substr(startString.length);
            result += '-';
        }
    }
    return result.slice(0, -1);
}