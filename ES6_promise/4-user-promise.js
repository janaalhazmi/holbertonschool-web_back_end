export default function signUpUser(firstName, lastName) {
  return new Promise((resolve, reject) => {
    if (!firstName || !lastName) {
      reject(new Error('Both firstName and lastName are required'));
    } else {
      resolve({ firstName, lastName });
    }
  });
}