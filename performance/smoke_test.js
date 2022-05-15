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
    let loginPageResponse = http.get('http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/login/');
    
    sleep(10);

    // Now, submit form setting/overriding some fields of the form
    let loginFormResponse = loginPageResponse.submitForm({
      formSelector: 'form',
      fields: { username: USERNAME, password: PASSWORD },
    });
    sleep(3);

    check(loginFormResponse, {
        'http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/home/': (loginFormResponse) => loginFormResponse.headers.Location
    })
  }

  export function book() {
    let response
  
    group('page_1 - http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/', function () {
      response = http.get('http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/', {
        headers: {
          'upgrade-insecure-requests': '1',
        },
      })
      sleep(14.1)
  
      response = http.post(
        'http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/',
        {
          reservation_name: 'ciaran',
          guests: '2',
          reservation_date: '2022-05-20',
          nice_to_have: 'wine',
        },
        {
          headers: {
            'content-type': 'application/x-www-form-urlencoded',
            origin: 'http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001',
            'upgrade-insecure-requests': '1',
          },
        }
      )
      sleep(3)
    })
  }