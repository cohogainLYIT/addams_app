import http from 'k6/http';
import { check, group, sleep, fail } from 'k6';

export const options = {
    vus: 1,
    duration: '20s',

    thresholds: {
        http_req_duration: ['p(99)<1500'],
    },
};

const BASE_URL = 'http://ec2-3-249-228-212.eu-west-1.compute.amazonaws.com:5001';
const USERNAME = 'Gomez';
const PASSWORD = 'Fester';


export default function () {
    // Request page containing a form
    let res = http.get('http://ec2-3-249-228-212.eu-west-1.compute.amazonaws.com:5001/login/');
  
    // Now, submit form setting/overriding some fields of the form
    res = res.submitForm({
      formSelector: 'login',
      fields: { username: USERNAME, password: PASSWORD },
    });
    sleep(3);
  }
