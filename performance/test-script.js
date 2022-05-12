import { sleep, check } from 'k6';
import http from 'k6/http';

export const options = {
   duration: '2m',
   vus: 10
};

export default function() {
    http.get('http://ec2-54-74-169-197.eu-west-1.compute.amazonaws.com:5001/')
    sleep(3);
}