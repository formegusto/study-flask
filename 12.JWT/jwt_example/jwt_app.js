const header = {
  typ: "JWT",
  alg: "HS256",
};

const encodedHeader = new Buffer.from(JSON.stringify(header))
  .toString("base64")
  .replace("=", "");

console.log("header: ", encodedHeader);
/*
    header:  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
*/

exp = Date.now() + 1000 * 60 * 60 * 24 * 3;
const payload = {
  iss: "formegusto.com",
  exp: exp,
  "https://github.com/formegusto/study-flask": true,
  userId: "formegusto@gmail.com",
  username: "formegusto",
};
const encodedPayload = new Buffer.from(JSON.stringify(payload))
  .toString("base64")
  .replace("=", "");
console.log("payload: ", encodedPayload);
/*
    payload:  eyJpc3MiOiJmb3JtZWd1c3RvLmNvbSIsImV4cCI6MTYzMTUwMTk2ODE1MywiaHR0cHM6Ly9naXRodWIuY29tL2Zvcm1lZ3VzdG8vc3R1ZHktZmxhc2siOnRydWUsInVzZXJJZCI6ImZvcm1lZ3VzdG9AZ21haWwuY29tIiwidXNlcm5hbWUiOiJmb3JtZWd1c3RvIn0
*/

const crypto = require("crypto");
const secret = "formegusto@jwt";
const signature = crypto
  .createHmac("sha256", secret)
  .update(`${encodedHeader}.${encodedPayload}`)
  .digest("base64")
  .replace("=", "");
console.log("signature: ", signature);
/*
    signature:  hTCarc7g8m1mhwVy9yADDhQ/sHj6CigBRJdGkoQJtQs
*/

const urjwt = `${encodedHeader}.${encodedPayload}.${signature}`;
console.log("u'r JWT: ", urjwt);
/*
    u'r JWT:  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmb3JtZWd1c3RvLmNvbSIsImV4cCI6MTYzMTUwMjQzNjI4NiwiaHR0cHM6Ly9naXRodWIuY29tL2Zvcm1lZ3VzdG8vc3R1ZHktZmxhc2siOnRydWUsInVzZXJJZCI6ImZvcm1lZ3VzdG9AZ21haWwuY29tIiwidXNlcm5hbWUiOiJmb3JtZWd1c3RvIn0.F/C/sGLCdoyIDjfZ6qXkQASvV5OZomI/Lgg457wS45E
*/
