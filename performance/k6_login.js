import http from 'k6/http';
import { check, group, sleep, fail } from 'k6';

export const options = {
    vus: 5,
    duration: '1m',

    thresholds: {
        http_req_duration: ['p(95)<500'],
    },
};

const BASE_URL = 'http://ec2-3-249-142-230.eu-west-1.compute.amazonaws.com:5001/';
const USERNAME = 'Gomez';
const PASSWORD = 'Fester';


export default function login() {
    let response = http.get(`${BASE_URL}:5001/login/`)
    
    sleep(5)
  
    response = http.post(`${BASE_URL}:5001/login/`,
    {
        username: USERNAME,
        password: PASSWORD,
    })

    sleep(5)
}
