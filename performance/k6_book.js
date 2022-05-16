import http from 'k6/http';
import { check, group, sleep, fail } from 'k6';

export const options = {
    vus: 5,
    duration: '1m',

    thresholds: {
        http_req_duration: ['p(95)<500'],
    },
};

const BASE_URL = 'http://ec2-3-249-199-235.eu-west-1.compute.amazonaws.com:5001/';
  
export default function book() {
    let response = http.get(`${BASE_URL}:5001/`)
    
    sleep(5)
  
    response = http.post(`${BASE_URL}:5001/`,
    {
        reservation_name: 'Ciarán',
        guests: '2',
        reservation_date: '2022-05-31',
        nice_to_have: 'wine and chocolate',
    })

    sleep(5)
}
  

export function handleSummary(data) {
    return{
        'stdout': textSummary(data, { indent: ' ', enableColors: true}),
        './output.json': JSON.stringify(data),
    }
}