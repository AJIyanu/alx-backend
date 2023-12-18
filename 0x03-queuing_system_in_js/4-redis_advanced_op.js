import { createClient } from "redis";


const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.toString()}`);
})

client.on('connect', () => console.log('Redis client connected to the server'));

const hashKeyValue = {
    Portland: 50,
Seattle: 80,
'New York': 20,
Bogota: 20,
Cali: 40,
Paris: 2,
}

for (const [place, numer] in Object.entries(hashKeyValue)) {
    client.HSET("HolbertonSchools", place, numer, print);
}

client.HGETALL("HolbertonSchools", (err, reply) => console.log(reply));
