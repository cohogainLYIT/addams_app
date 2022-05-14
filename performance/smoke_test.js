import http from 'k6/http';
import { check, group, sleep, fail } from 'k6';

export const options = {
    vus: 1,
    duration: '1m',

    thresholds: {
        http_req_duration: ['p(99)<1500'],
    },
};

const BASE_URL = 'http://ec2-3-249-228-212.eu-west-1.compute.amazonaws.com:5001';
const USERNAME = 'Gomez';
const PASSWORD = 'Fester';

export default () => {
    const loginRes = http.post(`${BASE_URL}/login/`, {
      username: USERNAME,
      password: PASSWORD,
    });
};