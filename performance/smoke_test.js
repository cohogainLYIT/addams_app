import http from 'k6/http';
import { check, group, sleep, fail } from 'k6';

export const options = {
    vus: 1,
    duration: '10s',

    thresholds: {
        http_req_duration: ['p(99)<3000'],
    },
};

const BASE_URL = 'http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/';
const USERNAME = 'Gomez';
const PASSWORD = 'Fester';


export default function () {
    // Request page containing a form
    let loginPageResponse = http.post('http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/login/', {
        username: USERNAME,
        password: PASSWORD,
    });
};