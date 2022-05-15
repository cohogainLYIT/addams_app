import http from 'k6/http';
import { check, group, sleep, fail } from 'k6';

export const options = {
    vus: 1,
    duration: '1m',

    thresholds: {
        http_req_duration: ['p(99)<3000'],
    },
};

const BASE_URL = 'http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/';
const USERNAME = 'Gomez';
const PASSWORD = 'Fester';


export default function login() {
    let response = http.get('http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/login/')
    
    sleep(5)
  
    response = http.post('http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/login/',
    {
        username: 'Gomez',
        password: 'Fester',
    })

    sleep(5)
}
  
export function book() {
    let response = http.get('http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/')
    
    sleep(5)
  
    response = http.post('http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/',
    {
        reservation_name: 'Ciarán',
        guests: '2',
        reservation_date: '2022-05-31',
        nice_to_have: 'wine and chocolate',
    })

    sleep(5)
}
  