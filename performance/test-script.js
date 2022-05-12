import { group, sleep } from 'k6';
import http from 'k6/http/';

export let options = {
    maxRedirects: 0,
    stages: [
        { target: 20, duration: "20s"},
        { target: 20, duration: "40s"},
        { target: 0, duration: "20s"}
    ]
};

export default function() {
    http.get('http://ec2-54-74-169-197.eu-west-1.compute.amazonaws.com/')
    sleep(3);
}