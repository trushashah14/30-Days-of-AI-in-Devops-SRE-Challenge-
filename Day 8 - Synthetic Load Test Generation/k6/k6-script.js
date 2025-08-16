import http from 'k6/http';
import { sleep } from 'k6';
import { SharedArray } from 'k6/data';

// Allow input file selection via environment variable
const dataFile = __ENV.DATA_FILE || 'synthetic_requests.json';

// Use a JSON file exported from your notebook
const requests = new SharedArray('synthetic', function() {
  return JSON.parse(open(dataFile));
});

function ensureProtocol(url) {
  if (!url.startsWith('http://') && !url.startsWith('https://')) {
    return 'http://localhost' + url; // or your actual host
  }
  return url;
}

export const options = {
  stages: [
    { duration: '35s', target: 70 }, // ramp up to 70 users at 2 users/sec (70/2=35s)
    { duration: '25s', target: 70 }, // hold at 70 users for the remainder to total 1 min
  ],
};

export default function () {
  const req = requests[Math.floor(Math.random() * requests.length)];
  const url = ensureProtocol(req.endpoint);
  http.request(req.method, url);
  sleep(1);
}