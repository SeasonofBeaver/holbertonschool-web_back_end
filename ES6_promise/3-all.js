/* eslint-disable */
import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
    return Promise.all([uploadPhoto(), createUser()])
        .then((results) => {
            const [photo, user] = results;
            console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
        })
        .catch(() => {
            console.log('Signup system offline');
        });
}