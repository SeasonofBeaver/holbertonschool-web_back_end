/* eslint-disable */
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
    const signUpPromise = signUpUser(firstName, lastName).then(
        (value) => ({ status: 'fulfilled', value }),
        (reason) => ({ status: 'rejected', value: reason })
    );
    const uploadPhotoPromise = uploadPhoto(fileName).then(
        (value) => ({ status: 'fulfilled', value }),
        (reason) => ({ status: 'rejected', value: reason })
    );

    return Promise.allSettled([signUpPromise, uploadPhotoPromise]);
}