// Scenario: Scenario_1 (executor: ramping-vus)

import { sleep, group } from 'k6'
import http from 'k6/http'

export const options = {
  ext: {
    loadimpact: {
      distribution: { 'amazon:ie:dublin': { loadZone: 'amazon:ie:dublin', percent: 100 } },
      apm: [],
    },
  },
  thresholds: {},
  scenarios: {
    Scenario_1: {
      executor: 'ramping-vus',
      gracefulStop: '30s',
      stages: [
        { target: 5, duration: '1m' },
        { target: 0, duration: '1m' },
      ],
      gracefulRampDown: '30s',
      exec: 'scenario_1',
    },
  },
}

export function scenario_1() {
  let response

  group(
    'page_1 - http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/login/',
    function () {
      response = http.get('http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/login/', {
        headers: {
          'upgrade-insecure-requests': '1',
        },
      })
      sleep(6.2)

      response = http.post(
        'http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001/login/',
        {
          username: 'Gomez',
          password: 'Fester',
        },
        {
          headers: {
            'content-type': 'application/x-www-form-urlencoded',
            origin: 'http://ec2-52-213-198-226.eu-west-1.compute.amazonaws.com:5001',
            'upgrade-insecure-requests': '1',
          },
        }
      )
    }
  )
}