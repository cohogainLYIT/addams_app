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
    let response
  
    group(
      'page_1 - http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/login/',
      function () {
        response = http.get('http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/login/')
        sleep(6.2)
  
        response = http.post(
          'http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/login/',
          {
            username: 'Gomez',
            password: 'Fester',
          }
        )
      }
    )
  }