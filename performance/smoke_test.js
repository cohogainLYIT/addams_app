import http from 'k6/http';
import { check, group, sleep, fail } from 'k6';

//export const options = {
//endregion    vus: 1,
//    duration: '20s',

//    thresholds: {
//        http_req_duration: ['p(99)<1500'],
//    },
//};

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
